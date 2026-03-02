from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from A import A
from classes.frontend.Scale import Scale
from classes.globals.widgets.FocusImage import FocusImage
from classes.globals.Colors import Colors
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import math as Math


from classes.globals.Functions import Functions 


class EndScreen(Widget):
    flash_incr = 0
    flash_label = None
    flash_timer = None 

    powerups = None

    powerup_text = ["USED", "FOUND"]

    shapes_found = None

    start = False

    end_bg = None

    low_point_range = 1000
    high_point_range = 5000

    fast_bonus = 500
    slow_penalty = 500
    win_bonus = 1000

    coins_display = None
    point_display = None
    timer_display = None
    powerup_container = None

    shapes_x = None
    shapes_y = None

    curr_x = None
    curr_y = None

    shapes_width = 15
    shapes_height = 15

    shapes_x_spacing = 20
    shapes_y_spacing = 100

    shapes = []

    container_height = 50

    adjusted_message = []
    adjusted_display = None

    shape_points = 0

    low_timer_range = None  
    medium_timer_range = None
    high_timer_range = None
    game_length = None
  


    def __init__(self, **kwargs):
        super(EndScreen, self).__init__(**kwargs)
        self.power_x = A().root().current_width * .58
        self.power_y = A().root().current_height * .55
        self.current_power_x = self.power_x
        self.current_power_y = self.power_y
        self.found_pos = (A().root().current_width * .25, A().root().current_height * .55)
        self.no_match = (A().root().current_width * .275, A().root().current_height * .45)
        self.new_pos = (A().root().current_width * .67, A().root().current_height * .05)
        self.main_pos = (A().root().current_width * .23, A().root().current_height * .05)
        self.point_pos = (A().root().current_width * .22, A().root().current_height * .05)
        self.coins_pos = (A().root().current_width * .27, A().root().current_height * .7)
        self.timer_pos = (A().root().current_width * .455, A().root().current_height * .7)
        self.adjusted_pos = (A().root().current_width * .635, A().root().current_height * .64)


        self.scale = Scale()
        self.end_bg = Image(source="")
        self.add_widget(self.end_bg)

        self.text_containers = {
            "left": [],
            "right": []
        }


    def adjust_points(self):
        adjust = 0

        if self.game_won() == True:
            adjust += self.win_bonus 
            message = Label(text="Win Game +1000", valign='middle', halign='left', size_hint=(1, 1), pos_hint={"x": .05, "center_y": 0}, color=Colors.GREEN, font_name="fonts/CANDARAB")
            message.font_size = self.scale.adjust_number(10)
            message.bind(size=lambda instance, value: setattr(instance, 'text_size', value)) 
            self.adjusted_message.append(message)

        if A().main().timer.minutes < self.low_timer_range and self.game_won() == True:
            adjust += (self.fast_bonus * self.fast_score()) 
            message = Label(text="Fast Game +500" if self.fast_score() < 2 else "Fast Game +500        x" + str(self.fast_score()), valign='middle', halign='left', size_hint=(1, 1), pos_hint={"x": .05, "center_y": 0},  color=Colors.GREEN, font_name="fonts/CANDARAB")
            message.font_size = self.scale.adjust_number(10)
            message.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
            self.adjusted_message.append(message)

        if A().main().timer.minutes > self.high_timer_range and self.game_won == True:
            adjust -= (self.slow_penalty * self.slow_score())  
            message = Label(text="Slow Game -500" if self.slow_score() < 2 else "Slow Game -500         x" + str(self.slow_score()), valign='middle', halign='left', size_hint=(1, 1), pos_hint={"x": .05, "center_y": 0}, color=Colors.WARNING, font_name="fonts/CANDARAB")
            message.font_size = self.scale.adjust_number(10)
            message.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
            self.adjusted_message.append(message)

        # adjust -= self.penalty_score()

        A().main().points.add(adjust)
        return adjust



    def show_adjusted(self):
        self.adjusted_display = FloatLayout(x=self.adjusted_pos[0], y=self.adjusted_pos[1], size=self.scale.adjust_size([400, 120]), size_hint=(None, None))

        y = .9
        for label in self.adjusted_message:
            label.pos_hint['center_y'] = y
            self.adjusted_display.add_widget(label)
            y -= .25

        self.add_widget(self.adjusted_display)


    def add_points(self):
        self.remove_widget(self.point_display)
        self.remove_widget(self.adjusted_display)
        self.adjusted_message = []
        self.point_display = Label(valign='middle', halign='left', size_hint=(1, 1), pos_hint={"x": .05, "center_y": 0}, color=self.get_color(), font_name="fonts/CANDARAB")
        self.point_display.font_size = self.scale.adjust_font(A().main().base_font_size)
        self.point_display.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.adjusted_message.append(self.point_display)
        self.adjust_points() 
        self.point_display.text = "Points: " + str(A().main().points.score)
        self.show_adjusted()


    def get_color(self):
        return Colors.DARK_RED if int(A().main().points.score) < 0 else Colors.GREEN if int(A().main().points.score) >= 2000 else  Colors.WHITE


    def penalty_score(self):
        return (A().main().strike_used + A().main().stop_used + A().main().eraser_used) * 100
    

    def fast_score(self):
        return  Math.floor(abs(A().main().timer.minutes - self.low_timer_range)) 
    

    def slow_score(self):
        return Math.ceil(abs(A().main().timer.minutes - self.high_timer_range)) 
    

    def all_used(self):
        return ((A().main().strike_used*A().main().strike_penalty) + (A().main().stop_collected*A().main().stop_penalty)+(A().main().eraser_collected*A().main().eraser_penalty))


    def display_end(self):
        self.curr_x = self.shapes_x =  A().root().current_width * .24
        self.curr_y = self.shapes_y = A().root().current_height * .5

        self.powerups = {"strikes": [A().main().strike_used, A().main().strike_collected, "ATTEMPTS", A().main().strike_penalty], "stop": [A().main().stop_used, A().main().stop_collected, "STOP", A().main().stop_penalty], "eraser": [A().main().eraser_used, A().main().eraser_collected, "ERASER", A().main().eraser_penalty]}

        if not self.start:
            try:
                title_source = f"images/screens/{App.get_running_app().screens.current_skin}/skins/game_over.png"
                button_source = f"images/screens/{App.get_running_app().screens.current_skin}/buttons/return.png"
            except Exception as e:
                print(e)
                title_source = f"images/screens/001/skins/game_over.png"
                button_source = f"images/screens/001/buttons/return.png"  

            self.end_bg = Image(pos=(0,0), width=A().root().current_width, height=A().root().current_height, source=A().root().resource_path(title_source), allow_stretch=True, keep_ratio=False)

            self.remove_widget(self.end_bg)
            self.add_widget(self.end_bg)

            self.add_widget(FocusImage(source=A().root().resource_path(f"images/screens/{App.get_running_app().screens.current_skin}/buttons/new_game.png"), size=self.scale.adjust_size([75, 13], True), pos=self.new_pos, opacity=1, allow_stretch=True, keep_ratio=False, textname="new_game"))

            self.add_widget(FocusImage(source=A().root().resource_path(f"images/screens/{App.get_running_app().screens.current_skin}/buttons/main_menu.png"), size=self.scale.adjust_size([75, 13], True), pos=self.main_pos, opacity=1, allow_stretch=True, keep_ratio=False, textname="main_menu"))

            self.shapes_found = Label(text="PATTERNS COMPLETED", x=self.found_pos[0], y=self.found_pos[1], width=200, height=50, opacity=1, color=(1,1,1,1), font_name="fonts/CANDARAB")
            self.shapes_found.font_size = self.scale.adjust_number(12)
            self.shapes_found.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            self.win_text = Label(text="YOU WIN!", x=self.found_pos[0] * 1.55, y=self.found_pos[1], width=200, height=50, opacity=1, color=Colors.GREEN, font_name="fonts/CANDARAB")
            self.win_text.font_size = self.scale.adjust_number(12)
            self.win_text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            self.quit_text = Label(text="[X] - EXIT GAME", x=A().root().current_width*.72, y=A().root().current_height*.87, color=Colors.WHITE, font_name="fonts/CANDARAB")
            self.quit_text.font_size = self.scale.adjust_number(12)
            self.quit_text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
            self.add_widget(self.quit_text)

            self.add_widget(self.shapes_found)
            self.add_widget(self.win_text) if self.game_won() else None
            self.add_coins()
            self.add_points()
            self.add_timer()
            self.add_powerups()
            self.add_shapes()
            self.demo_text()
            self.shape_points_text()
            self.freeze_points_text()
            self.explode_points_text()
            self.coin_points_text() 
            self.populate_text()
            
            self.start = True


    def demo_text(self, toggle=True):
        self.flash_label = Label(text="DEMO VERSION", font_size=Scale().adjust_number(18), color=Colors.DARK_RED, pos=(A().root().current_width * .47, A().root().current_height *.02))
        self.flash_timer = Clock.schedule_interval(self.demo_flash, 1) if toggle == True else None


    def demo_flash(self, dt):
        self.flash_incr += 1
        self.flash_label.text == "" if self.flash_incr % 2 == 0 else "DEMO VERSION"
        self.remove_widget(self.flash_label) if self.flash_incr % 2 == 0 else self.add_widget(self.flash_label)
    

    def add_coins(self):
        self.remove_widget(self.coins_display)

        self.coins_display = Label(text="Coins: " + A().main().display.coins_text, opacity=1, color=Colors.WHITE, x=self.coins_pos[0], y=self.coins_pos[1], font_name="fonts/CANDARAB")
        self.coins_display.font_size = self.scale.adjust_font(A().main().base_font_size)
        self.coins_display.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.add_widget(self.coins_display)


    def add_timer(self):
        A().main().timer.stop()
        self.remove_widget(self.timer_display)

        self.timer_display = Label(text=A().main().timer.clock_display, opacity=1, color=self.timer_color(), x=self.timer_pos[0], y=self.timer_pos[1], font_name="fonts/CANDARAB")
        self.timer_display.font_size = self.scale.adjust_font(A().main().base_font_size)
        self.timer_display.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.add_widget(self.timer_display)


    def timer_color(self):
        if self.game_won() == False:
            return Colors.WHITE
        return Colors.GREEN if A().main().timer.minutes < self.low_timer_range else Colors.WHITE if A().main().timer.minutes < self.medium_timer_range else Colors.YELLOW if A().main().timer.minutes < self.high_timer_range else Colors.WARNING
    

    def point_color(self):
        if self.game_won() == False:
            return Colors.WHITE
        return Colors.WARNING if A().main().points.score < 0 else Colors.YELLOW if A().main().points.score < self.low_point_range else Colors.GREEN if A().main().points.score > self.high_point_range else Colors.WHITE
    
    
    def game_won(self):
        self.low_timer_range = 30 if A().main().demo == False else 10  
        self.medium_timer_range = 40 if A().main().demo == False else 12
        self.high_timer_range = 50 if A().main().demo == False else 18 
        self.game_length = 30 if A().main().demo == False else 9
        return len(A().main().found_lists) >= self.game_length


    def add_powerups(self):
        x_coord = .64
        y_coord = .55

        self.powerup_container =  FloatLayout(pos=( A().root().current_width*x_coord, A().root().current_height*y_coord), size=self.scale.adjust_size([200, 50]), size_hint=(None, None))

        label = Label(text=self.powerup_text[0], opacity=1, color=(1,1,1,1), valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.05, 'y': 0.05}, font_name="fonts/CANDARAB")
        label.font_size = self.scale.adjust_number(12)
        label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.powerup_container.add_widget(label)

        label = Label(text=self.powerup_text[1], opacity=1, color=(1,1,1,1), valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': 0.05, 'y': 0.05}, font_name="fonts/CANDARAB")
        label.font_size = self.scale.adjust_number(12)
        label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.powerup_container.add_widget(label)

        self.add_widget(self.powerup_container)
        self.current_power_x -= 50
        self.current_power_y -= 75
    
        x_value = 0.05
        x_coord = .55
        y_coord = .52
        for key in self.powerups.keys():
            container =  FloatLayout(pos=( A().root().current_width*x_coord, self.current_power_y), size=(250, 70), size_hint=(None, None))

            label = Label(text=str(self.powerups[key][2]), opacity=1, color=(1,1,1,1), valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.05, 'y': 0.05}, font_name="fonts/CANDARAB")
            label.font_size = self.scale.adjust_number(A().main().base_font_size)
            label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            x_value += .3 
            container.add_widget(label)

            label = Label(text=str(self.powerups[key][0]), opacity=1, color=(1,1,1,1), valign='middle', halign='center', size_hint=(1, 1), pos_hint={'x': 0.255, 'y': 0.05}, font_name="fonts/CANDARAB")
            label.font_size = self.scale.adjust_font(A().main().base_font_size)
            label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            x_value += .3
            container.add_widget(label)

            label = Label(text=str(self.powerups[key][1]), opacity=1, color=(1,1,1,1), valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': 0.3, 'y': 0.05}, font_name="fonts/CANDARAB")
            label.font_size = self.scale.adjust_font(A().main().base_font_size)
            label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            container.add_widget(label)

            label = Label(text=(str(self.powerups[key][0]*self.powerups[key][3]) + " pts." if self.powerups[key][0] > 0 else "") , opacity=1, color=(1,1,1,1), valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': 0.9225, 'y': 0.05}, font_name="fonts/CANDARAB")
            label.font_size = self.scale.adjust_font(A().main().base_font_size)
            label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            container.add_widget(label)

            self.current_power_y -= self.scale.adjust_number(25)
            self.add_widget(container)

            label = Label(text=("________\n\n-" + str(self.all_used()) + " pts." if self.all_used() > 0 else "") , opacity=1, color=(1,1,1,1), pos=(A().root().current_width * .75, A().root().current_height * .295), font_name="fonts/CANDARAB")
            label.font_size = self.scale.adjust_font(A().main().base_font_size)
            label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

            self.add_widget(label)


    def get_bonus(self):
        return A().main().levels_unlocked if len(A().main().levels_unlocked) > 0 else None


    def add_bonus(self, level):
        container = FloatLayout(x=A().root().current_width*.42, y=A().root().current_height*.615, size=self.scale.adjust_size([200, 85]), size_hint=(None, None))
        bonus = Label(text=str(A().main().levels_unlocked.index(level)+1) + ". ", valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.0, 'center_y': .6}, color=Colors.VIOLET, font_name="fonts/CANDARAB")
        bonus.font_size = self.scale.adjust_number(11)
        bonus.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(bonus)

        unlocked = Label(text=str(level[0]), valign='middle', halign='center', size_hint=(1, 1), pos_hint={'x': 0.2, 'center_y': .6}, color=Colors.VIOLET, font_name="fonts/CANDARAB")
        unlocked.font_size = self.scale.adjust_number(11)
        unlocked.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(unlocked)

        time = Label(text=str(level[1]), valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': 0.6, 'center_y': .55}, color=Colors.VIOLET, font_name="fonts/CANDARAB")
        time.font_size = self.scale.adjust_number(11)
        time.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(time)

        self.add_widget(container)


    def add_shapes(self):
        self.scroll = ScrollView(size_hint=(1, 1), size=self.scale.adjust_size([500, 350]), center_x=A().root().current_width * .37, center_y=A().root().current_height * .39, do_scroll_y=True)

        self.outer_box = BoxLayout(width=self.scale.adjust_number(self.scroll.width),orientation='vertical', size_hint_y=None)
        self.outer_box.bind(minimum_height=self.outer_box.setter('height'))

        self.box = BoxLayout(width=self.scale.adjust_number(self.scroll.width-10), orientation='vertical', size_hint_y=None)
        self.box.bind(minimum_height=self.box.setter('height'))

        for shapes in A().main().found_lists:
            self.curr_y = self.curr_y - self.scale.adjust_number(self.shapes_y_spacing) if A().main().found_lists.index(shapes) > 0 else self.shapes_y
            self.create_shapes(shapes)

        if len(A().main().found_lists) < 1:
            self.add_widget(Label(text="No patterns matched", pos=self.no_match, font_name="fonts/CANDARAI", font_size=self.scale.adjust_number(11)))

        if self.get_bonus() and A().root().login_required == True:
            self.curr_y = self.curr_y - self.scale.adjust_number(self.shapes_y_spacing * 3)

            label = Label(text="Bonus Level(s) Unlocked!", x=A().root().current_width*.47, y=A().root().current_height *.65, color=Colors.VIOLET, font_name="fonts/CANDARAB")
            label.font_size = self.scale.adjust_number(11)

            self.add_widget(label)

            for level in A().main().levels_unlocked:
                self.add_bonus(level)

        self.outer_box.height = self.container_height * len(A().main().found_lists)
        self.outer_box.height = 300
        self.box.height = self.outer_box.height - 10
        self.outer_box.add_widget(self.box)
        self.scroll.add_widget(self.outer_box)

        Clock.schedule_once(lambda dt: self.scroll_top(self.scroll), 1) if self.scroll.scroll_y != 1 else None

        self.add_widget(self.scroll)  


    def scroll_top(self, widget):
        widget.scroll_y = 1 if widget != None else None


    def create_shapes(self, shapes):
        curr_shapes = []
        self.curr_x = self.shapes_x

        container = FloatLayout(x=self.curr_x, y=self.curr_y, size=self.scale.adjust_size([300, 85]), size_hint=(None, None))

        number = Label(text=str(A().main().found_lists.index(shapes)+1) + ". ", valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.0, 'center_y': .6}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        number.font_size = self.scale.adjust_number(A().main().base_font_size)
        number.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(number)

        self.curr_x = self.shapes_x 
        shape_x = -.0325

        for shape in shapes[0]:
            shown = Image(source=A().root().resource_path("images/shapes/"+shape+".png"), size_hint=(.35, .35), pos_hint={'x': shape_x, 'center_y': .6})
            container.add_widget(shown)
            curr_shapes.append(shown)
            shape_x += .12

        time = Label(text=str(shapes[1]), valign='bottom', halign='left', size_hint=(1, 1), pos_hint={'x': 0.1, 'center_y': .525}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        time.font_size = self.scale.adjust_number(A().main().base_font_size)
        time.bind(size=lambda instance, value: setattr(instance, 'text_size', value)) 
        container.add_widget(time)

        points = Label(text=str(shapes[2]) + " pts.", valign='bottom', halign='right', size_hint=(1, 1), pos_hint={'x': .35, 'center_y': .525}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        points.font_size = self.scale.adjust_number(A().main().base_font_size)
        points.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.shape_points += shapes[2]

        container.add_widget(points)
        self.box.add_widget(container)
        self.shapes.append(container)


    def coin_points_text(self):
        container = FloatLayout(x=A().root().current_width * .235, y=A().root().current_height * .125, size=self.scale.adjust_size([300, 85]), size_hint=(None, None))

        text = Label(text="Coins x" + A().main().display.coins_text, valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.0, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        text.font_size = self.scale.adjust_number(A().main().base_font_size)
        text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(text)

        points = Label(text=str(self.get_coin_points()) + " pts.", valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': .35, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        points.font_size = self.scale.adjust_number(A().main().base_font_size)
        points.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        container.add_widget(points)
        self.text_containers["left"].append(container) if int(A().main().display.coins_text) > 0 else None


    def get_coin_points(self):
        return int(A().main().display.coins_text) * A().main().points.gold_points
    

    def shape_points_text(self):
        container = FloatLayout(x=A().root().current_width * .235, y=A().root().current_height * .15, size=self.scale.adjust_size([300, 85]), size_hint=(None, None))

        text = Label(text="Patterns Total", valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.0, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        text.font_size = self.scale.adjust_number(A().main().base_font_size)
        text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(text)

        points = Label(text=str(self.shape_points) + " pts.", valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': .35, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        points.font_size = self.scale.adjust_number(A().main().base_font_size)
        points.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        container.add_widget(points)
        self.text_containers["left"].append(container) if len(A().main().found_lists) > 0 else None

    def freeze_points_text(self):
        container = FloatLayout(x=A().root().current_width*.545, y=A().root().current_height * .15, size=self.scale.adjust_size([300, 85]), size_hint=(None, None))

        text = Label(text="Frozen x" + str(A().main().freeze_mines), valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.075, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        text.font_size = self.scale.adjust_number(A().main().base_font_size)
        text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(text)

        points = Label(text=str(A().main().freeze_mines*A().main().freeze_penalty) + " pts.", valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': .515, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        points.font_size = self.scale.adjust_number(A().main().base_font_size)
        points.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        container.add_widget(points)
        self.text_containers["right"].append(container) if A().main().freeze_mines > 0 else None


    def explode_points_text(self):
        container = FloatLayout(x=A().root().current_width*.545, y=A().root().current_height * .125, size=self.scale.adjust_size([300, 85]), size_hint=(None, None))

        text = Label(text="Exploded x" + str(A().main().bomb_mines), valign='middle', halign='left', size_hint=(1, 1), pos_hint={'x': 0.075, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        text.font_size = self.scale.adjust_number(A().main().base_font_size)
        text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        container.add_widget(text)

        points = Label(text=str(A().main().bomb_mines*A().main().explode_penalty) + " pts.", valign='middle', halign='right', size_hint=(1, 1), pos_hint={'x': .515, 'center_y': .5}, color=(1,1,1,1), font_name="fonts/CANDARAB")
        points.font_size = self.scale.adjust_number(A().main().base_font_size)
        points.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        container.add_widget(points)
        self.text_containers["right"].append(container) if A().main().bomb_mines > 0 else None


    def populate_text(self):
        for container in self.text_containers.keys():
            y = .15
            for label in self.text_containers[container]:
                label.y = A().root().current_height * y
                self.add_widget(label)
                y -= .025

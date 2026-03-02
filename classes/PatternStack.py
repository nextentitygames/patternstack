from random import randint
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from A import A
from classes.backend.Database import Database
from classes.frontend.screens.MusicScreen import MusicScreen
from classes.frontend.screens.PauseScreen import Pause
from classes.backend.Points import Points
from classes.backend.Shape import Shape
from classes.backend.Rules import Rules
from classes.frontend.Scale import Scale
from classes.backend.Timer import Timer
from classes.backend.Display import Display
from classes.frontend.screens.EndScreen import EndScreen
from classes.frontend.screens.NewScreen import NewScreen
from classes.frontend.screens.TitleScreen import TitleScreen
from classes.frontend.screens.TutorialScreen import TutorialScreen
from classes.globals.Functions import Functions
from classes.globals.Loading import Loading
from classes.globals.Meter import Meter
from classes.globals.Sound import Sound
import sys

from classes.globals.widgets.FocusImage import FocusImage




class PatternStack(Widget):   
    title_obj = None
    new_obj = NewScreen()
    tutorial_obj = None
    statistics_obj = None
    achievements_obj = None
    inventory_obj = None
    statistics_obj = None
    store_obj = None
    leaderboard_obj = None
    profile_obj = None
    music_obj = None

    end_obj = None
    loading = None
    parse = None
    timer = None
    display = None
    
    player1 = None
    gold = 0
    strikes = 3
    shield = 0 
    word_count = 0
    found_count = 0
    on_title_screen = True
    in_game = False
    in_tutorial = False
    round_start = False
    shape = None

    grabbed = None
    symbols = []
    symbol_amount = 8
    target_amount = 4
    add_height = 50
    list_x = 60
    target_list = []
    target_symbols = []
    list_coords = []
    drop_velocity = (0, -400)
    default_velocity = (0, -100)
    slow_velocity = (0, -50)
    symbol_velocity = (0, -150)
    stop_velocity = (0, 0)
    remove_start = False
    default_spacing = 1100
    default_y = 457
    round_delay = False
    round_clock = None
    list_length = 20
    current_coords = []
    move_symbols = False
    new_y = []
    new_targets = []
    move_target_list = False
    target_spacing = 40
    symbols_y = (Window.height/2) - 30
    round = 1 
    current_round = 1
    current_word = []
    found_symbols = []
    reset_target_list = False
    solved_round = 0
    x_bounds = [Window.width * .11, Window.width * .91]
    stop_on = False
    slow_on = False

    freeze_mine = False
    bomb_mine = False
    paused = False
    pause = ObjectProperty(None)
    pause_layer = None

    widget_size = 60

    shield_collected = 0
    strike_collected = 0
    coins_collected = 0
    eraser_collected = 0
    stop_collected = 0
    slow_collected = 0

    bomb_mines = 0
    grow_mines = 0
    freeze_mines = 0
    blind_mines = 0
    shrink_mines = 0

    shield_used = 0
    strike_used = 0
    coins_used = 0
    eraser_used = 0
    stop_used = 0
    slow_used = 0

    username = None 
    name = None 
    jwt = None

    user_data = None
    statistics_data = None
    achievements_data = None
    inventory_data = None
    store_data = None
    games_data = None

    shapes_amount = 3

    explode_widget = None
    collision_widget = []

    last_touch = 0
    touch_side = None

    mouse_clicked = False
    temp_symbols = []
    
    bg_sound = None
    radio_timer = None
    music_loaded = False

    mine_texts = ["bomb", "freeze"]

    powerup_texts = {
        "bomb": "BOMB!",
        "empty": "Empty Stack...",
        "add_eraser": "Erasers +1",
        "eraser": "Eraser Used",
        "eraser3": "No Erasers",
        "freeze": "FROZEN!",
        "freeze2": "Frozen. Can't Process...",
        "gold": "GOLD +1",
        "no_match": "Not A Match...",
        "round": "Passed Round!",
        "stack": "Stack Completed!",
        "start": "START GAME!!!",
        "stop": "STOPPED",
        "add_stop": "Stops +1",
        "stop2": "No Stops",
        "strike": "Collision!",
        "add_strike": "Attempts +1",
        "reset": "",
    }

    update_timer = None
    targets_timer = None
    move_target_timer = None
    symbols_timer = None
    remove_timer = None
    fall_timer = None
          
    powerup_text = False
    mine_text = False
    found_text = False

    powerup_timer = None
    mine_timer = None
    found_timer = None

    bonus_sprites = {"eraser": "images/eraser.png",  "gold": "images/coin.gif", "strikes": "images/strike.png", "stop": "images/stop.gif",}

    mine_sprites = {"bomb": "images/bomb.gif", "freeze": "images/freeze.gif", "blind": "images/blind.gif", "grow": "images/grow.jpg"}

    mine_methods = None
    game_end = False

    current_widgets = []

    widget_spacing = 90

    time_goals = [600, 240, 180, 120, 90]
    levels_unlocked = []
    
    base_width = 800
    base_height = 457

    current_width = 800
    current_height = 457

    shapes = ["circles", "squares", "stars", "hearts", "moons", "hexagons",  "trapezoids", "arrows", "triangles", "arrows2"]

    main_hud = None
    large_plate = None

    text_color = "#000226"

    current_skin = "skin_001"
    current_avatar = ""

    stops_allowed = True

    base_font_size = 12
     
    font_colors = {
        "light": "#ffffff",
        "dark": "#000226" 
    }

    base_font_color = font_colors["dark"]

    username_size = 10

    hidden_widgets = {
        "profile": []
    }

    found_lists = []
    current_shapes = [] 

    first_game = True

    powerup_size = 40

    update_interval = 1/60

    gold_interval = 1/64
    eraser_interval = 1/150
    strike_interval = 1/150
    freeze_interval = 1/8
    stop_interval  = 1/16 
    mine_interval = 1/8
    current_time = 0

    stop_clock = None
    freeze_clock = None
    explode_clock = None
    powerup_clock = None

    freeze_meter = None
    stop_meter = None
    meter_frame = None
    explode_delay = False 

    freeze_timer = None

    stop_penalty = eraser_penalty = -100
    freeze_penalty = explode_penalty = strike_penalty = -250

    touch_bounds = {"x" : [Window.width * .03, Window.width * .94], "y": [Window.height * .12, Window.height * .88]}

    counted_targets = []
    counted_shapes = []
    possible_matches = 0
    mouse_overs = {}

    stop_duration = 250
    freeze_duration = 250
    explode_duration = 30
    powerup_duration = 250
    
    def __init__(self, **kwargs):
        super(PatternStack, self).__init__(**kwargs)
        self.app_root = A().root()
        Window.bind(on_resize=self.on_window_resize)
        # Window.bind(mouse_pos=self.on_mouse_move)

        self.demo = True
        self.debug = False
        self.total_rounds = 10 if self.demo == False else 3
        
        self.points = Points()
        self.display = None
        self.scale = Scale()
        self.functions = Functions()
        self.database = Database()
        self.sound = Sound(soundtype="", soundname="")
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        self.bg_sound = Sound(soundtype="music", soundname="underground-cavern-metaruka")
        self.bg_sound.load_music()
        self.get_bg_sound()

        self.sounds = {
            "bg": self.bg_sound,
            "block": Sound(soundtype="effects", soundname="block"),
            "coin": Sound(soundtype="effects", soundname="coin"),
            "collect": Sound(soundtype="effects", soundname="collect"),
            "erase": Sound(soundtype="effects", soundname="erase"),
            "explode": Sound(soundtype="effects", soundname="explode"),
            "found": Sound(soundtype="effects", soundname="found"),
            "freeze": Sound(soundtype="effects", soundname="freeze"),
            "frozen": Sound(soundtype="effects", soundname="frozen"),
            "grab": Sound(soundtype="effects", soundname="grab"),
            "invalid": Sound(soundtype="effects", soundname="invalid"),
            "menu_back": Sound(soundtype="effects", soundname="menu_back"),
            "menu_select": Sound(soundtype="effects", soundname="menu_select"),
            "pause": Sound(soundtype="effects", soundname="pause"),
            "round": Sound(soundtype="effects", soundname="round"),
            "stack": Sound(soundtype="effects", soundname="stack"),
            "start": Sound(soundtype="effects", soundname="start"),
            "stop": Sound(soundtype="effects", soundname="stop"),
            "win": Sound(soundtype="effects", soundname="win"),
            "wrong": Sound(soundtype="effects", soundname="wrong")
        }

        self.new_obj = NewScreen()
        self.end_obj = EndScreen()
        self.loading = Loading()
        self.title_obj = TitleScreen()

        self.title_screen()
        self.add_widget(self.title_obj)

        self.tutorial_obj = TutorialScreen()
        self.music_obj = MusicScreen()

        self.add_widget(self.loading)

        self.mine_methods = {"bomb": self.bomb_logic, "freeze": self.freeze_logic}
        
        self.pause_layer = Pause(size_hint=(1, 1))
   
        self.text_container = FloatLayout(center_x=Window.width*.145, y=Window.height*.82, size=self.scale.adjust_size((300, 75)))

        self.powerup_text_display = Label(text="", opacity=1, color=(1,1,1,1), size_hint=(1, 1), pos_hint={'center_x': .55, 'y': 0.5}, font_name="fonts/CANDARAB")
        self.powerup_text_display.font_size = self.scale.adjust_number(15)
        self.powerup_text_display.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.add_height = self.scale.adjust_number(50)
        self.default_spacing = self.scale.adjust_number(1100)
        self.default_y = self.scale.adjust_number(457)
        self.target_spacing = self.scale.adjust_number(40)
        self.symbols_y = self.scale.adjust_number((Window.height/2) - 30)
        self.x_bounds = [Window.width * .11, Window.width * .94]
        self.add_widget(self.text_container)


    def radio(self, side):
        self.radio_timer.cancel() if self.radio_timer else None
        self.radio_timer = None
        place = list(self.bg_sound.sounds["music"].keys()).index(A().root().current_sound) + (1 if side == True else -1)

        A().root().current_sound = list(self.bg_sound.sounds["music"].keys())[len(self.bg_sound.sounds["music"]) - 1 if place < 0 else 0 if place > len(self.bg_sound.sounds["music"]) - 1 else place]

        self.music_obj.music_text = A().root().current_sound

        self.bg_sound.toggle(False)
        self.get_bg_sound()
        self.bg_sound.toggle(True, True)
        
        self.remove_widget(self.music_obj)
        self.remove_texts()
        self.music_obj.show_choice(side)
        self.add_widget(self.music_obj)
        
        self.radio_timer = Clock.schedule_once(self.hide_radio, 7)


    def radio_toggle(self, play):
        self.bg_sound.resume() if play else self.bg_sound.pause()


    def hide_radio(self, dt):
        self.remove_widget(self.music_obj)
        self.radio_timer.cancel() if self.radio_timer else None
        self.radio_timer = None


    def on_touch_down(self, touch):
        self.touch_widget(touch) if not self.paused and self.in_bounds([touch.x, touch.y]) else None
        return super(PatternStack, self).on_touch_down(touch)
    

    def touch_widget(self, touch):  
        for widget in self.current_widgets:
            if widget.x != None and widget.y != None and widget.height != None and widget.width != None or len(widget.sprite_label.text > 2) and self.freeze_mine == False and self.in_game == True:
                if abs(touch.x - widget.x) < widget.width + 15 and abs(touch.y - widget.y) < widget.height:
                    if self.stop_on == True:
                        self.stop_grab(widget)
                    elif self.grabbed == None and widget.sprite_label.text.split("_")[0] in self.shapes:
                        self.check_grab(widget)  
                    
        if len(self.symbols) > 0:
            if touch.x < self.symbols[0].x:
                self.touch_side = False
            else:
                self.touch_side = True
        else:
            self.touch_side = None


    def in_bounds(self, pos):
        return pos[1] < Window.height * .98 and pos[1] > Window.height * .12 and pos[0] < Window.width * .8875 and pos[0] > Window.width * .105


    def on_window_resize(self, window, width, height):
        self.current_width = width
        self.current_height = height


    def get_bg_sound(self):
        self.bg_sound.set_sound("music", A().root().current_sound)
        self.bg_sound.random_music() if self.music_loaded == False else None 
        self.music_loaded = True 


    def screen_handler(self, current, start=None):
        screens = {
            "title": self.title_obj, 
            "hud": self.main_hud,
            "tutorial": self.tutorial_obj,
            "statistics": self.statistics_obj,
            "store": self.store_obj,
            "whats_new": self.new_obj,
            "leaderboard": self.leaderboard_obj,
            "_sfile": self.profile_obj,
            "inventory": self.inventory_obj,
            "musc": self.music_obj,
            "achievements": self.achievements_obj,
            "end": self.end_obj
        }

        for screen in screens.keys():
            self.remove_widget(screens[screen])
        
        if not start:
            self.remove_widget(screens["title"])
            self.title_obj.menu_buttons() if current == "title" else self.title_obj.demo_text(False)
            self.add_widget(screens[current]) 


    def hidden_handler(self, widget, add, screen, clear=False):
        if widget:
            self.hidden_widgets[screen] = [] if clear == True else []
            self.hidden_widgets[screen].append(widget) if widget not in self.hidden_widgets[screen] and add == True else None
            self.hidden_widgets[screen].remove(widget) if widget in self.hidden_widgets[screen] and add == False else None


    def check_screen(self):
        if A().root().login_required == True:
            if self.current_skin == self.database.get_data(self.user_data["current_skins"]):
                return True
            self.current_skin = self.database.get_data(self.user_data["current_skins"])
            return False
        return True
    

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if self.in_game and keycode[1] == "spacebar":
            self.pause_logic()
        if self.in_game and self.timer.timer > 0:
            if keycode[1] == "enter":
                if(len(self.symbols) > 0):
                    self.process_symbol()
                else:
                    self.powerup_text_start("empty")
                    self.sounds["invalid"].toggle(True)
            if keycode[1] == "escape" and self.debug == True:
                self.check_end_game()
            if keycode[1] == "e":
                self.use_eraser()
            if keycode[1] == "s" and self.stop_on == False:
                self.use_stop()
            if keycode[1] == "f" and self.debug == True:
                self.freeze_logic()

        if self.in_game and self.paused == False:
            if keycode[1] == ",":
                self.radio(False)
            if keycode[1] == ".":
                self.radio(True)
            if keycode[1] == "p":
                self.radio_toggle(True)
            if keycode[1] == "o":
                self.radio_toggle(False)

        if (self.in_game and self.paused == True) or self.end_obj.start == True or self.title_obj in self.children:
            if keycode[1] == "x":
                sys.exit(0)
            if keycode[1] == "r":
                self.restart_game()
            if keycode[1] == "m":
                self.main_menu()
        return True
    

    def main_menu(self):
        self.stop_game()
        self.reset()
        self.screen_handler("title")


    def restart_game(self):
        self.stop_game()
        self.reset()
        self.start_load()


    def randomize_assets(self):
        self.bg_sound.random_music()
        A().root().random_hud()
        A().root().random_skin()


    def tutorial_screen(self):
        self.on_title_screen = False
        self.in_tutorial = True


    def title_screen(self):
        self.in_tutorial = False
        self.on_title_screen = True


    def reset(self):
        self.gold = 0
        self.strikes = 3
        self.shield = 0 
        self.word_count = 0
        self.found_count = 0
        self.on_title_screen = True
        self.in_game = False
        self.in_tutorial = False
        self.round_start = False
        self.shape = None
        self.grabbed = None
        self.music_loaded = False
        self.symbols = []
        self.symbol_amount = 8
        self.target_amount = 4
        self.add_height = 50
        self.list_x = 60
        self.target_list = []
        self.reset_list(True)
        self.target_symbols = []
        self.list_coords = []
        self.drop_velocity = (0, -400)
        self.default_velocity = (0, -100)
        self.slow_velocity = (0, -50)
        self.symbol_velocity = (0, -150)
        self.stop_velocity = (0, 0)
        self.remove_start = False
        self.default_spacing = 1100
        self.default_y = 457
        self.round_delay = False
        self.list_length = 20
        self.current_coords = []
        self.move_symbols = False
        self.new_y = []
        self.new_targets = []
        self.move_target_list = False
        self.target_spacing = 40
        self.symbols_y = (Window.height/2) - 30
        self.round = 1 
        self.current_round = 1
        self.current_word = []
        self.found_symbols = []
        self.reset_target_list = False
        self.solved_round = 0
        self.x_bounds = [Window.width * .11, Window.width * .94]
        self.stop_on = False
        self.slow_on = False
        self.freeze_mine = False
        self.bomb_mine = False
        self.paused = False
        self.pause = ObjectProperty(None)
        self.remove_widget(self.pause_layer)
        self.remove_widget(self.pause_layer.pause_label)
        self.remove_widget(self.display.pause_display)   
        self.pause_layer.reset_pause()
        self.widget_size = 60
        self.shield_collected = 0
        self.strike_collected = 0
        self.coins_collected = 0
        self.eraser_collected = 0
        self.stop_collected = 0
        self.slow_collected = 0
        self.bomb_mines = 0
        self.grow_mines = 0
        self.freeze_mines = 0
        self.blind_mines = 0
        self.shrink_mines = 0
        self.shield_used = 0
        self.strike_used = 0
        self.coins_used = 0
        self.eraser_used = 0
        self.stop_used = 0
        self.slow_used = 0
        self.username = None 
        self.name = None 
        self.jwt = None
        self.user_data = None
        self.statistics_data = None
        self.achievements_data = None
        self.inventory_data = None
        self.store_data = None
        self.games_data = None
        self.shapes_amount = 3
        self.found_lists = []
        self.current_shapes = [] 
        self.powerup_text_display = Label(text="", opacity=1, color=(1,1,1,1), size_hint=(1, 1), pos_hint={'center_x': .55, 'y': 0.5}, font_name="fonts/CANDARAB")
        self.powerup_text_display.font_size = self.scale.adjust_number(15)
        self.powerup_text_display.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.add_height = self.scale.adjust_number(50)
        self.default_spacing = self.scale.adjust_number(1100)
        self.default_y = self.scale.adjust_number(457)
        self.target_spacing = self.scale.adjust_number(40)
        self.symbols_y = self.scale.adjust_number((Window.height/2) - 30)
        self.x_bounds = [Window.width * .11, Window.width * .94]
        self.points = Points()
        self.display = Display()
        self.end_obj = EndScreen()
        self.randomize_assets()

 
    def start_load(self):
        self.remove_widget(self.loading)
        self.add_widget(self.loading)
        self.loading.start("start_game")


    def start_game(self):
        try:
            self.paused = False
            self.round_delay = False
            self.remove_widget(self.main_hud)
            self.main_hud = Image(source=self.app_root.current_hud, pos=(0,0), width=Window.width, height=Window.height, allow_stretch=True, keep_ratio=False)
            self.set_font_color()
            self.timer = Timer()
            self.on_title_screen = False
            self.shape = Shape() 
            self.display = Display()
            self.add_widget(self.display)
            self.remove_widget(self.title_obj)
            self.add_widget(self.main_hud)
            self.timer.display.opacity = 1
            self.add_widget(self.timer)
            self.display.add_layers()
            self.set_current_widgets()
            self.set_list_coords()
            self.new_list()
            self.set_y()
            self.update_layers()
            self.bg_sound.toggle(True, True)

        except Exception as e:
            pass
            # print(e)


    def end_game(self):
        self.timer.stop()


    def set_y(self):
        self.new_y.append(self.symbols_y)
        spacing = self.add_height

        while len(self.new_y) < self.symbol_amount:
            self.new_y.append(spacing)
            spacing += self.add_height


    def check_visible(self, widget):
        if widget.sprite_label.text.split("_")[0] in self.shapes and widget not in self.symbols:
            widget.opacity = 1
            widget.sprite.opacity = 1
            widget.sprite_label.opacity = 0
        else:
            widget.opacity = 1
            widget.sprite.opacity = 1
            widget.sprite_label.opacity = 0
            try:
                widget.sprite.source = self.app_root.resource_path(self.bonus_sprites[widget.sprite_label.text])
            except:
                widget.sprite.source = self.app_root.resource_path(self.mine_sprites[widget.sprite_label.text])

        self.assign_size(widget)
        self.get_adjustments(widget)


    def round_timer(self):
        self.round_clock = Clock.schedule_once(self.round_off, 3)


    def set_font_color(self):
        self.base_font_color = self.font_colors["dark"] if "light" in self.main_hud.source else self.font_colors["light"]
    

    def round_off(self, dt):
        self.round_delay = True
        self.round_clock.cancel() if self.round_clock else None


    def opacity_handler(self, widget, condition):
        if condition:
            widget.opacity = 1
            widget.sprite_label.opacity = 0
            widget.sprite.opacity = 1
        else:
            widget.opacity = 0
            widget.sprite.opacity = 0
            widget.sprite_label.opacity = 0
        

    def count_targets(self, current):
        try:
            self.counted_targets.append(current) if current.sprite.source == self.target_list[len(self.counted_targets)].sprite.source else None
        except:
            pass

        self.counted_shapes.append(current)
        
        if len(self.counted_targets) == len(self.target_list):
            self.possible_matches +=1 
            self.counted_targets = []


    def serve_ball(self, ball, *largs): 
        if len(self.current_widgets) > 0 and self.current_widgets != None:
            ball.x = self.random_x()
            ball.y = self.random_y()        
            self.change_coords(ball) 
            self.opacity_handler(ball, True)

        if not self.round_start and ball not in self.target_list:
            ball.opacity = 0


    def checkfall(self, dt):
        if self.round_delay:
            for current in self.current_widgets[:]:
                if current != None and current not in self.symbols:
                    if current.y < -60:
                        self.new_symbol(current, self.current_widgets.index(current))  
                        self.counted_shapes.remove(current) if current in self.counted_shapes else None
                    self.count_targets(current) if current.y < 0 and current not in self.counted_targets and current not in self.counted_shapes else None


    def change_speed(self):
        if self.target_list != None:
            for widget in self.current_widgets:
                if self.word_count < 5:
                    if widget not in self.symbols:
                        widget.velocity = self.default_velocity
                    else: 
                        widget.velocity = self.stop_velocity


    def update_targets(self, dt):
        if not self.round_delay and not self.paused and self.in_game: 
            if self.remove_start:
                for widget in self.target_list:
                    widget.velocity = self.drop_velocity 
                    widget.move(dt)
                    if widget.y < -60:
                        self.target_list.remove(widget)
                    
                if len(self.target_list) < 1:
                    self.remove_start = False
                    self.reset_list(True)

                    if self.solved_round % 3 == 0:
                        self.new_round()  
                    else:
                        self.reset_round()

            else:
                spacing = self.add_height

                for widget in self.target_list:
                    widget.opacity = 1
                    widget.move(dt)

                    if widget in self.target_list and widget.y <= (Window.height * .075)  + spacing:
                        widget.velocity = self.stop_velocity
                        
                    spacing += self.add_height

                move_target = True 
                for widget in self.target_list:
                    if widget.velocity != [0, 0]:
                        move_target = False
                        break
                
                if move_target:
                    self.round_timer()     


    def move_collision(self):
        for widget in self.current_widgets[:]:
            if widget.y < self.symbols[len(self.symbols)-1].y + self.symbols[len(self.symbols)-1].height and widget.y > 0 and (widget.x >= self.last_touch.x and self.touch_side == False and self.symbols[0].x <= widget.x) or (widget.x <= self.last_touch.x and self.touch_side == True and self.symbols[0].x >= widget.x):
                self.move_symbols = False


    def update_symbols(self, dt):
        try:
            if self.move_symbols == True:
                for widget in self.symbols:
                    self.move_collision()
                    if (widget.x <= self.last_touch.x and self.touch_side == False) or (widget.x >= self.last_touch.x and self.touch_side == True):
                        widget.velocity = self.stop_velocity
                        self.move_symbols = False        
                    widget.move(dt)
        except Exception as e:
            pass
            # print("error in update symbols function: ", e)


    def update(self, dt):
        try:
            self.current_time += 1
            self.update_targets(dt)
            self.update_symbols(dt)
            self.checkfall(dt)
            self.events_check()
            if self.round_delay == True and self.in_game == True:
                self.change_speed()
                self.collect()
                if len(self.current_widgets) >= self.list_length and not self.stop_on:
                    for current in self.current_widgets[:]:
                        self.check_visible(current)
                        try:
                            if self.slow_on:
                                current.velocity = self.slow_velocity
                            else:
                                current.velocity = self.default_velocity if not self.paused else self.stop_velocity
                            current.move(dt)

                            if current.opacity == 1 and current.y < Window.height and self.timer.stopped and not self.paused:
                                self.timer.start()
                        except:
                            pass
        except Exception as e:
            pass
            # print("error in update function: ", e)
   

    def events_check(self):
        if self.explode_clock:
            if self.current_time > self.explode_clock + self.explode_duration:
                self.explode_delete()

        if self.freeze_clock:
            if self.current_time > self.freeze_clock + self.freeze_duration:
                self.freeze_delay()

        if self.stop_clock:
            if self.current_time > self.stop_clock + self.stop_duration:
                self.freeze_delay()

        if self.powerup_clock:
            if self.current_time > self.powerup_clock + self.powerup_duration:
                self.powerup_text_delay()
                

    def opacity_check(self, widget):
        if widget.opacity == 1:
            return True
        return False 
           

    def x_collision(self, widget, compare, offset=0):
        if (widget.x + offset + widget.width > compare.x) and (widget.x <= compare.x + widget.width + offset + 20):
            return True
        return False    
    

    def y_collision(self, widget, compare, offset=0):
        if widget.sprite_label.text == "bomb" or widget.sprite_label.text == "gold":
            offset -= 15 if offset > 0 else 0

        if widget.y < compare.y + compare.height + offset and (widget.y + widget.height + offset) > compare.y:
            return True
        return False
    
    
    def collection(self, widget, compare):
        if widget.y <= compare.y + compare.height + 5 and widget.y > compare.y + compare.height - 5 and widget.x + widget.width > compare.x and widget.x < compare.x + compare.width:
            return True
        return False
    

    def collect(self):
        if self.symbols != None and self.target_list != None:
            if len(self.symbols) > 0 and len(self.target_list) > 0  and len(self.current_widgets) > 0:
                place = len(self.symbols)
                
                for widget in self.current_widgets[:]:
                    if widget != None:
                    
                        if widget.y > 0 and self.opacity_check(widget) and self.collection(widget, self.symbols[place-1]) and widget not in self.symbols and self.explode_delay == False:

                            if self.mine_handler(widget):
                                return True

                            elif self.add_powerup(widget):
                                return True

                            elif widget.sprite_label.text.split("_")[0] in self.shapes:
                                self.add_to_stack(widget)

                            return True

                        if self.check_collision(widget):
                            return True
                    else:
                        self.current_widgets.remove(widget)


    def mine_handler(self, widget):
        if widget.sprite_label.text == "freeze":
            if not self.freeze_mine:
                self.new_symbol(widget, self.current_widgets.index(widget)) 
                self.freeze_logic()
                return True
            else:
                self.sounds["frozen"].toggle(True)
                self.new_symbol(widget, self.current_widgets.index(widget)) 
                return True

        if widget.sprite_label.text == "bomb":
            try:
                self.new_symbol(widget, self.current_widgets.index(widget)) 
            except:
                pass
            self.bomb_logic(widget)
            return True

        if widget.sprite_label.text in self.mine_texts:
            return True
        return False
    

    def remove_texts(self):
        self.mine_text = False
        self.found_text = False
        self.powerup_text = False
        self.mine_timer.cancel() if self.mine_timer else None
        self.mine_timer = 0
        self.found_timer.cancel() if self.found_timer else None
        self.found_timer = 0
        self.powerup_timer.cancel() if self.powerup_timer else None
        self.powerup_timer = 0
        self.powerup_text_display.text = ""
        self.text_container.remove_widget(self.powerup_text_display)
        

    def remove_meters(self):
        self.text_container.remove_widget(self.stop_meter) if self.stop_meter else None
        self.text_container.remove_widget(self.freeze_meter) if self.freeze_meter else None
        self.text_container.remove_widget(self.meter_frame) if self.meter_frame else None
        self.stop_meter = None
        self.freeze_meter = None
        self.meter_frame = None



    def bomb_logic(self, bomb):
        self.sounds["explode"].toggle(True) 
        self.powerup_text_start("bomb") 
        self.bomb_mines += 1
        self.points.add(self.explode_penalty)
        self.display.set_strikes(-1)
        self.post_collision(bomb)
        self.current_word = []
        self.grabbed = None
        self.freeze_mine = False
        self.bomb_mine = True
        

    def post_collision(self, widget):
        self.stop_freeze()
        widget.sprite.source = self.app_root.resource_path("images/animations/explode.gif")
        widget.sprite_label.opacity = 0
        widget.sprite.anim_delay = 1/32
        widget.velocity = self.stop_velocity  
        self.collision_widget.append(widget)
        self.current_widgets.remove(widget) if widget in self.current_widgets else None   
        self.update_explode()
        self.explode_delay = True
        #Clock.schedule_once(self.explode_delete, .4)
        
            

    def explode_delete(self, dt=None):
        for widget in self.symbols:
            try:
                self.delete_widget(widget) if "explode" in widget.sprite.source or "explode" in widget.sprite_label.source else None
            except:
                pass
            
        self.symbols = []
        for widget in self.collision_widget:
            self.current_widgets.append(widget) if widget not in self.current_widgets else None
            self.new_symbol(widget, self.current_widgets.index(widget))
        self.collision_widget = []
        self.bomb_mine = False
        self.explode_delay = False
        self.explode_clock = None


    def update_explode(self):
        for widget in self.symbols:
            widget.sprite.source = self.app_root.resource_path("images/animations/explode.gif")
            widget.sprite_label.opacity = 0
            widget.anim_delay = 1/32
            widget.velocity = self.stop_velocity
        # Clock.schedule_once(self.explode_delete, .4)
        self.explode_clock = self.current_time


    def freeze_logic(self):
        self.meter_frame = Meter("frame", True)
        self.freeze_meter = Meter("freeze", True)
        self.meter_frame.pos_hint={"x": 0, "y": .5}
        self.freeze_meter.pos_hint={"x": 0, "y": .5}
        self.text_container.add_widget(self.meter_frame)
        self.text_container.add_widget(self.freeze_meter)
        self.powerup_text_start("freeze")
        self.sounds["freeze"].toggle(True)
        self.temp_symbols = []
        for widget in self.symbols:
            self.temp_symbols.append(widget.sprite.source)
        self.update_freeze()
        self.freeze_mine = True
        self.freeze_mines += 1
        self.points.add(self.freeze_penalty)
        # self.freeze_timer = Clock.schedule_once(self.freeze_delay, 5)
        freeze_clock = self.current_time
        self.freeze_clock = freeze_clock



    def update_freeze(self):
        for widget in self.symbols:
            widget.sprite.source = self.app_root.resource_path("images/ice.png")


    def stop_freeze(self):
        self.freeze_timer.cancel() if self.freeze_timer else None
        self.freeze_timer = None
        self.freeze_clock = None


    def freeze_delay(self, dt=None):
        i = 0
        for widget in self.symbols:
            widget.sprite.source = self.app_root.resource_path(self.temp_symbols[i])
            i += 1
        self.freeze_mine = False
        self.freeze_clock = None
        #self.stop_freeze()


    def pause_logic(self):    
        if not self.paused: 
            self.sounds["pause"].toggle(True)
            self.bg_sound.pause()
            for widget in self.current_widgets[:]:
                widget.velocity = self.stop_velocity

            self.remove_widget(self.display.pause_display)

            if self.timer.timer > 0:
                self.timer.stopped = True
            self.paused = True 
            try:
                self.add_widget(self.pause_layer) if self else None
            except:
                pass

            self.update_layers()
            self.pause_layer.remove_widget(self.pause_layer.pause_label)
            self.remove_widget(self.pause_layer.pause_label)
            self.add_widget(self.pause_layer.pause_label)
            self.display.remove_widget(self.display.pause_display)
            self.remove_widget(self.display.pause_display)
            self.add_widget(self.display.pause_display)

        else:
            self.bg_sound.resume() if self.in_game == True else None
            for widget in self.current_widgets[:]:
                widget.velocity = self.default_velocity

            self.timer.restart()
            self.paused = False
            self.remove_widget(self.pause_layer)
            self.remove_widget(self.pause_layer.pause_label)
            self.remove_widget(self.display.pause_display)   
            self.update_layers()
            self.display.remove_widget(self.display.pause_display)
            self.display.add_widget(self.display.pause_display)
          

    def add_powerup(self, widget):
        found = False

        if widget.sprite_label.text == "strikes":
            self.sounds["found"].toggle(True)
            self.powerup_text_start("add_strike") 
            self.strike_collected += 1
            self.display.set_strikes(1)
            found = True

        if widget.sprite_label.text == "gold":
            self.sounds["coin"].toggle(True)
            self.coins_collected += 1
            self.powerup_text_start("gold")
            self.display.set_coins(1)
            self.points.add(self.points.gold_points)
            found = True

        if widget.sprite_label.text == "eraser":
            self.sounds["found"].toggle(True)
            self.powerup_text_start("add_eraser")
            self.eraser_collected += 1
            self.display.set_eraser(1)
            found = True

        if widget.sprite_label.text == "stop":
            self.sounds["found"].toggle(True)
            self.powerup_text_start("add_stop")
            self.stop_collected += 1
            self.display.set_stop(1)
            found = True

        if found:
            widget.y = -500
            self.new_symbol(widget, self.current_widgets.index(widget))

            return True
        return False


    def check_end_game(self):
        if self.current_round > self.total_rounds or self.debug==True or self.display.strikes_value < 1:
            for widget in self.current_widgets[:]:
                widget.velocity = self.stop_velocity
            Clock.schedule_once(self.end_game_delay, 1)
            return True
        return False


    def end_game_delay(self, dt):
        self.remove_texts()
        self.update_timer.cancel() if self.update_timer else None
        self.update_timer = None
        self.in_game = False
        self.game_over()

    
    def new_round(self):
        self.remove_texts()
        self.current_round += 1
        if self.check_end_game() == False:
            self.set_rules()
            self.display.set_stacks(self.solved_round)
            self.display.set_round(int(self.solved_round/3) + 1) if self.solved_round % 3 == 0 else None
            self.change_velocity(True)
            self.set_current_widgets()
            self.set_list_coords()
            self.new_list()
            self.set_y()
            Clock.schedule_once(self.set_round_delay, 3)
            # self.stop_on = False


    def set_rules(self):
        self.shapes_amount = Rules.round_rules[str(self.current_round)]["shapes"]
        self.rare_shapes = Rules.round_rules[str(self.current_round)]["rare_shapes"]

        self.change_velocity(True) if Rules.round_rules[str(self.current_round)]["rare_shapes"] == True else None

        self.strike_rules = Rules.round_rules[str(self.current_round)]["strike_limit"]

        self.display.strikes_value = Rules.round_rules[str(self.current_round)]["strike_limit"] if Rules.round_rules[str(self.current_round)]["strike_limit"] != None else self.display.strikes_value   
        
        self.shape.mine_rules = Rules.round_rules[str(self.current_round)]["mine_multiplier"]

        self.shape.freeze_rules = Rules.round_rules[str(self.current_round)]["freeze_multiplier"]

        self.stops_allowed = Rules.round_rules[str(self.current_round)]["stops_allowed"]


    def reset_round(self):
        if self.check_end_game() == False:
            self.remove_texts()
            self.display.set_stacks(self.solved_round)
            self.set_current_widgets()
            self.set_list_coords()
            self.new_list()
            self.set_y()
            Clock.schedule_once(self.set_round_delay, 3)
            

    def check_collision(self, widget):
        if self.move_symbols == False and self.symbols[0] != None and widget != None and len(self.symbols) > 0 and self.explode_delay == False:
            if widget.y < (len(self.symbols) * self.scale.adjust_number(self.widget_size)) + self.symbols[0].y and (widget.y + self.scale.adjust_number(self.widget_size)) > self.symbols[0].y and (widget.x + self.scale.adjust_number(self.widget_size)) + self.scale.adjust_number(5) > self.symbols[0].x and widget.x < self.symbols[0].x + self.scale.adjust_number(self.widget_size) and widget not in self.symbols and self.opacity_check(widget):
                
                if widget.sprite_label.text in self.mine_texts:
                    self.mine_handler(widget)
                    return True
                
                self.collision(widget) if "bomb" not in widget.sprite_label.text else None
                return True
    

    def collision(self, collide=None):
        self.stop_freeze()
        Window.set_system_cursor("arrow")
        self.post_collision(collide) if collide else None
        self.sounds["wrong"].toggle(True)
        self.strike_used += 1
        self.powerup_text_start("no_match") if not collide else self.powerup_text_start("strike") if self.display.strikes_value > 1 else None
        self.points.add(self.strike_penalty)
        self.display.set_strikes(-1)
        self.current_word = []
        self.grabbed = None
        self.freeze_mine = False
        self.stop_on = False


    def assign_size(self, widget, special=None):
        if not special:
            widget.width = self.scale.adjust_number(self.widget_size)
            widget.height = self.scale.adjust_number(self.widget_size)
            widget.sprite.width = self.scale.adjust_number(self.widget_size)
            widget.sprite.height = self.scale.adjust_number(self.widget_size)
        else:
            if special[0] == True:
                widget.width = self.scale.adjust_number(special[1])
                widget.height = self.scale.adjust_number(special[1])
            else:
                widget.sprite.width = self.scale.adjust_number(special[1])
                widget.sprite.height = self.scale.adjust_number(special[1])
                       

    def add_to_stack(self, widget):
        if self.stop_on and self.symbols != None:
            
            if self.freeze_mine == False:
                self.sounds["collect"].toggle(True) 
            else:
                self.sounds["frozen"].toggle(True)  

            self.temp_symbols.append(widget.sprite.source) if self.freeze_mine else None
            i = self.current_widgets.index(widget)
            backup = self.current_widgets[i]
            symbol = Shape()
            symbol.sprite.source = self.app_root.resource_path(backup.sprite.source)
            symbol.sprite.opacity = 1
            symbol.sprite_label.opacity = 0
            symbol.velocity = self.stop_velocity
            symbol.sprite_label.text = backup.sprite_label.text
            symbol.x = self.symbols[len(self.symbols)-1].x 
            symbol.y = self.symbols[len(self.symbols)-1].y + self.symbols[len(self.symbols)-1].height + 10
            self.assign_size(symbol)
            i = self.current_widgets.index(widget)
            self.copy_symbol(backup, i)
            self.symbols.append(symbol)
            self.update_freeze() if self.freeze_mine else None
            self.current_word.append(widget.sprite_label.text)
            self.update_layers()    
            self.collision() if self.symbols[len(self.symbols)-1].y + self.symbols[len(self.symbols)-1].height > Window.width * .84 else None
            return True
        
        if self.symbols != None:
            if self.freeze_mine == False:
                self.sounds["collect"].toggle(True) 
            else:
                self.sounds["frozen"].toggle(True)

            self.temp_symbols.append(widget.sprite.source) if self.freeze_mine else None
            i = self.current_widgets.index(widget)
            backup = self.current_widgets[i]
            symbol = Shape()
            self.assign_size(symbol)
            symbol.sprite.source = self.app_root.resource_path(backup.sprite.source)
            symbol.sprite.opacity = 1
            symbol.sprite_label.opacity = 0
            symbol.velocity = self.stop_velocity
            symbol.sprite_label.text = backup.sprite_label.text
            symbol.x = self.symbols[len(self.symbols)-1].x 
            symbol.y = self.symbols[len(self.symbols)-1].y + self.symbols[len(self.symbols)-1].height + 10
            self.add_widget(symbol)
            self.copy_symbol(backup, i)
            self.symbols.append(symbol)
            self.update_freeze() if self.freeze_mine else None
            self.current_word.append(widget.sprite_label.text)
            self.update_layers()

            if self.symbols[len(self.symbols)-1].y > Window.height:
                self.process_symbol()


    def remove_from_stack(self, widget):
        if self.symbols != None:
            self.delete_widget(widget)
            self.symbols.remove(widget)
            self.current_word.pop(len(self.current_word)-1) if len(self.current_word) > 0 else None


    def delete_widget(self, widget):
        widget.stop()
        widget.opacity = 0
        widget.sprite.source = ""
        self.remove_widget(widget)


    def copy_symbol(self, current, place):
        current.x = self.random_x()
        current.y = self.random_y()
        self.check_coords()
        self.update_layers()


    def sprite_style(self, widget):
        text = self.shape.get_text(self.current_round)
        if "shapes" in text:
            widget.sprite_label.text = text.split("/")[2].replace(".png", "")
            widget.sprite_label.opacity = 0
            widget.sprite.opacity = 1
            widget.sprite.source = self.app_root.resource_path(text)
            self.assign_size(widget)
        else:
            widget.sprite_label.text = text
            widget.sprite_label.opacity = 0
            widget.sprite.source = self.app_root.resource_path(self.bonus_sprites[text]) if text not in self.mine_sprites else self.app_root.resource_path(self.mine_sprites[text])
            self.get_adjustments(widget)

        return widget
    

    def get_adjustments(self, widget):
        self.assign_size(widget)
        if widget.sprite_label.text == "gold":
            widget.sprite.anim_delay = self.gold_interval #
            self.assign_size(widget, [False, self.powerup_size])
        if widget.sprite_label.text == "eraser": 
            widget.sprite.anim_delay = self.eraser_interval 
            self.assign_size(widget, [False, self.powerup_size])
        if widget.sprite_label.text == "strike": 
            widget.sprite.anim_delay = self.strike_interval 
            self.assign_size(widget, [False, self.powerup_size])
        if widget.sprite_label.text == "freeze": 
            widget.sprite.anim_delay = self.freeze_interval 
        if widget.sprite_label.text == "stop": 
            widget.sprite.anim_delay = self.stop_interval 
            self.assign_size(widget, [False, self.powerup_size])
        if widget.sprite_label.text == "bomb":
            widget.sprite.anim_delay = self.mine_interval 


    def new_symbol(self, current, place):   
        current = self.sprite_style(current)
        current.x = self.random_x()
        current.y = self.random_y()
        self.change_coords(current) 


    def reset_widgets(self):
        for widget in self.current_widgets:
            self.remove_widget(widget)
            self.add_widget(widget)

        for widget in self.target_list:
            self.remove_widget(widget)
            self.add_widget(widget)   

        self.update_layers()


    def set_current_widgets(self):
        for widget in self.current_widgets:
            self.delete_widget(widget)
    
        self.current_widgets = []
        self.current_widgets[:] = []
        self.shape.set_sprites()
        self.new_coords()
        self.reset_widgets()
           

    def new_coords(self):
        coords = [self.random_x(), self.random_y()]

        if len(self.current_widgets) < 1:
            widget = Shape(x=coords[0], y=coords[1], velocity=self.default_velocity, opacity=0)
            widget = self.sprite_style(widget)
            self.current_widgets.append(widget)
            self.new_coords()
        if len(self.current_widgets) < self.list_length:
            widget = Shape(x=coords[0], y=coords[1], velocity=self.default_velocity, opacity=0)
            widget = self.sprite_style(widget)
            self.current_widgets.append(widget)
            self.new_coords()
            self.check_coords()
        if len(self.current_widgets) == self.list_length:
            self.add_mines()
            self.check_coords()


    def add_mines(self):
        mines = randint(3, 7)

        i = 0
        while i < mines:
            coords = [self.random_x(), self.random_y()]
            widget = Shape(x=coords[0], y=coords[1], velocity=self.default_velocity, opacity=0)
            widget.source = self.app_root.resource_path("images/bomb.gif")

            widget.sprite_label.text = "bomb"
            widget.sprite_label.opacity = 0
            self.current_widgets.append(widget)

            i += 1


    def check_coords(self):
        current_widgets = self.current_widgets
        widget_size = self.widget_size
        window_limit = Window.height + widget_size
        x_collide, y_collide = self.x_collision, self.y_collision
        stop_velocity = self.stop_velocity
        drop_velocity = self.drop_velocity

        self.current_coords = [[w.x, w.y] for w in current_widgets]
        for w in current_widgets:
            if w.y > Window.height + 50:
                w.velocity = stop_velocity

        changed = True
        while changed:
            changed = False
            for i, wi in enumerate(current_widgets):
                if wi.y <= window_limit:
                    continue

                for j, wj in enumerate(current_widgets[i + 1:], start=i + 1):
                    if wj.y <= window_limit:
                        continue

                    if (
                        x_collide(wi, wj, widget_size * 1.5)
                        and y_collide(wi, wj, widget_size * 2)
                    ):
                        self.new_symbol(wi, i)
                        changed = True
                        break 
                if changed:
                    break

        for w in current_widgets:
            w.velocity = drop_velocity


    def change_coords(self, widget):
        i = 0
        widget.velocity = self.stop_velocity
        while i < len(self.current_widgets):
            if i == 0:
                coords = [self.random_x(), self.random_y()]
                widget.x = coords[0]
                widget.y = coords[1]
            if widget.y + self.scale.adjust_number(self.widget_size) > Window.height and self.x_collision(widget, self.current_widgets[i], self.widget_spacing) and self.y_collision(widget, self.current_widgets[i], self.widget_spacing) and widget != self.current_widgets[i]:           
                i = 0
            else:
                i += 1
                
        widget.opacity = 1
        widget.sprite.opacity = 1
        widget.velocity = self.stop_velocity


    def random_x(self):
        return randint(int(Window.width*.12), int(Window.width * .88))


    def random_y(self):
        return randint(Window.height + 300, Window.height + 3000)
    

    def check_grab(self, widget):
        self.sounds["grab"].toggle(True)
        i = self.current_widgets.index(widget)
        backup = self.current_widgets[i]
        backup.opacity = 0 
        symbol = Shape()
        self.assign_size(symbol)
        symbol.velocity = self.stop_velocity
        symbol.sprite.source = self.app_root.resource_path(backup.sprite.source)
        symbol.sprite_label.text = backup.sprite_label.text
        symbol.sprite.opacity = 1
        symbol.sprite_label.opacity = 0
        symbol.x = widget.x
        symbol.y = Window.height * .17
        self.symbols.append(symbol)
        self.add_widget(symbol)
        self.grabbed = symbol
        self.copy_symbol(backup, i)
        self.current_word.append(widget.sprite_label.text)
        return True
                    

    def reset_list(self, new_round = False):
        if self.symbols != None and self.target_list != None:

            for widget in self.symbols:
                self.delete_widget(widget)

            self.current_word = []
            self.symbols = []
            self.grabbed = None
            if new_round:
                spacing = self.add_height
                spacing += self.add_height + 40
                self.target_list = []


    def set_round_delay(self, dt):
        self.start_timer()
                
            
    def set_list_coords(self):
        start_height = Window.height - self.default_y

        while len(self.list_coords) < self.symbol_amount:
            self.list_coords.append((self.list_x, start_height))
            start_height = start_height + self.add_height 


    def new_list(self):
        spacing = self.add_height 
        
        if self.target_list != None:
            i = 0 

            while len(self.target_list) < self.shapes_amount: 
                place = randint(0, len(self.current_widgets)-1)
                self.copy_symbol(self.current_widgets[place], place)
                symbol = Shape(x=self.list_coords[len(self.target_list)][0], y=Window.height + spacing)
                self.assign_size(symbol, [True, 40])
                symbol.velocity = self.symbol_velocity 
                text = ""
                while "shapes" not in text:
                    text = self.shape.get_text(1)
                    if i == 0 and "moons" in text:
                        text = "" 
                symbol.sprite.source = self.app_root.resource_path(text)
                symbol.sprite_label.text = text.split("/")[2].replace(".png", "")
                symbol.sprite_label.opacity = 0
                symbol.sprite.opacity = 1
                self.add_widget(symbol)
                spacing += self.add_height + self.target_spacing
                self.target_list.append(symbol)  

                i+=1

            self.move_target_list = True     

        if self.in_game == False and self.game_end == False:
            interval = self.update_interval 
            self.update_timer = Clock.schedule_interval(self.update, interval)
            self.in_game = True
        else:
            pass


    def widget_timer(self):
        Clock.schedule_once(self.set_start_delay, 3)


    def set_widget_delay(self, dt):
        self.widget_delay = True


    def start_timer(self):
        Clock.schedule_once(self.set_start_delay, 3)


    def set_start_delay(self, dt):
        self.round_start = True


    def update_layers(self):
        self.remove_layers()
        self.add_layers()


    def remove_layers(self):
        self.screen_handler("", True)
        self.remove_widget(self.loading)
        for widget in self.current_widgets:
            self.remove_widget(widget)
        for widget in self.target_list:
            self.remove_widget(widget)
        for widget in self.symbols:
            self.remove_widget(widget)
        for widget in self.children:
            if "Animate" in str(widget) or "Shape" in str(widget):
                self.remove_widget(widget)

        self.remove_widget(self.timer)
        self.remove_widget(self.points)
        self.remove_widget(self.display)
        self.text_container.remove_widget(self.powerup_text_display) if self.powerup_text else None
        self.remove_widget(self.text_container)
        self.remove_widget(self.pause_layer) if self.paused else None

        
    def add_layers(self):
        for widget in self.current_widgets:
            self.add_widget(widget)

        for widget in self.symbols:
            self.add_widget(widget)

        self.screen_handler("hud")

        for widget in self.target_list:
            self.add_widget(widget)

        self.add_widget(self.timer)
        self.add_widget(self.points)
        self.add_widget(self.display)
        self.text_container.add_widget(self.powerup_text_display) if self.powerup_text else None
        self.add_widget(self.text_container)
        self.add_widget(self.pause_layer) if self.paused == True else None
        self.add_widget(self.loading)
        

    def process_symbol(self):
        if self.freeze_mine == True:
            self.powerup_text_start("freeze2")
            self.sounds["invalid"].toggle(True)
            return False
        if [item.sprite_label.text for item in self.symbols] == [item.sprite_label.text for item in self.target_list]:
            
            self.remove_texts()
            self.remove_meters()

            self.solved_round +=1
            if self.solved_round % 3 != 0:
                self.sounds["stack"].toggle(True) if self.sounds["stack"] else None
                self.powerup_text_start("stack")        
            else:
                self.sounds["round"].toggle(True) if self.sounds["round"] else None
                self.powerup_text_start("round")     
            self.current_shapes = []

            for widget in self.target_list:
                self.current_shapes.append(widget.sprite_label.text)
            self.found_lists.append([self.current_shapes, self.points.get_found_time(), self.points.new_solved(self.current_shapes)])
            self.remove_current_symbols()
            self.remove_current_widgets()
            self.remove_start = True
            self.round_delay = False
            self.stop_on = False
            Window.set_system_cursor("arrow")
    
            if len(self.target_list) < 1:
                self.remove_start = False
                self.reset_list(True)
        else: 
            self.collision()


    def remove_current_symbols(self):
        for widget in self.symbols:
            self.remove_widget(widget)
            self.delete_widget(widget)
        self.symbols = []


    def remove_current_widgets(self):
        for widget in self.current_widgets:
            self.remove_widget(widget)
            self.delete_widget(widget)
        self.current_widgets = []


    def change_velocity(self, condition):
        if condition:
            self.default_velocity = (0, self.default_velocity[1] - 50)
        else: 
            self.default_velocity = (0, self.default_velocity[1] + 50)

            for widget in self.current_widgets:
                widget = self.default_velocity

        self.update_layers()


    def use_eraser(self):
        if self.display.eraser_value > 0:
            if len(self.symbols) > 0:
                self.sounds["erase"].toggle(True)
                self.points.add(self.eraser_penalty)
                self.remove_from_stack(self.symbols[len(self.symbols)-1])
                self.display.set_eraser(-1)
                self.eraser_used += 1
                self.powerup_text_start("eraser")
                if len(self.symbols) < 1:
                    self.grabbed = None
                
            else:
                self.powerup_text_start("empty")
        else:
            self.powerup_text_start("eraser3")  


    def use_stop(self):
        if self.display.stop_value > 0 and self.stops_allowed == True:
            self.meter_frame = Meter("frame", True)
            self.stop_meter = Meter("stop", True)
            self.meter_frame.pos_hint={"x": 0, "y": .5}
            self.stop_meter.pos_hint={"x": 0, "y": .5}
            self.text_container.add_widget(self.meter_frame)
            self.text_container.add_widget(self.stop_meter)
            self.sounds["stop"].toggle(True)
            self.points.add(self.stop_penalty)
            for widget in self.current_widgets:
                widget.velocity = self.stop_velocity
            self.sounds["stop"].toggle(True)
            self.powerup_text_start("stop")
            self.display.set_stop(-1)
            self.stop_used += 1
            self.stop_on = True
        else:
            self.powerup_text_start("stop2")


    def stop_grab(self, widget):
        if widget.sprite_label.text.split("_")[0] in self.shapes:
            self.add_to_stack(widget) if len(self.symbols) > 0 else self.check_grab(widget)
            self.update_layers()
        else: 
            self.add_powerup(widget) 
            self.update_layers()


    def powerup_text_start(self, powerup):
        if self.timer.timer > 0 and self.stop_on != True and self.music_obj not in self.children:
            self.remove_texts() 
            self.remove_meters() if powerup != "freeze" and powerup != "stop" else None
            self.powerup_text_display.text = self.powerup_texts[powerup] 
            self.remove_widget(self.text_container)
            self.text_container.remove_widget(self.powerup_text_display)
            self.text_container.add_widget(self.powerup_text_display)
            self.add_widget(self.text_container)
            # self.powerup_timer = Clock.schedule_once(self.powerup_text_delay, 5) 
            powerup_clock = self.current_time
            self.powerup_clock = powerup_clock
            self.powerup_text = True
        

    def powerup_text_delay(self, dt=0):
        self.text_container.remove_widget(self.powerup_text_display)
        self.powerup_text = False
        self.freeze_mine = False 
        if self.freeze_mine == True:
            self.freeze_mine = False
        if self.stop_on == True:
            self.stop_on = False
        self.powerup_clock = None
        self.remove_meters() 


    def stop_sounds(self):
        for sound in self.sounds.keys():
            try:
                self.sounds[sound].toggle(False) if self.sounds[sound] else None
            except:
                pass
        self.bg_sound.toggle(False)
  

    def stop_game(self):
        self.explode_delete()
        self.stop_sounds()
        self.remove_texts()
        
        self.in_game = False
        self.remove_layers()
        self.powerup_text = False
        self.text_container.remove_widget(self.stop_meter) if self.stop_meter and self.text_container else None
        self.text_container.remove_widget(self.freeze_meter) if self.freeze_meter and self.text_container else None
        self.text_container.remove_widget(self.powerup_text_display)
        self.remove_widget(self.text_container)
        self.powerup_text_display.text = ""
        for widget in self.children:
            self.remove_widget(widget)
        self.timer.stop() if self.timer else None
        self.update_timer.cancel() if self.update_timer else None
        self.targets_timer.cancel() if self.targets_timer else None
        self.move_target_timer.cancel() if self.move_target_timer else None
        self.symbols_timer.cancel() if self.symbols_timer else None
        self.remove_timer.cancel() if self.remove_timer else None
        self.fall_timer.cancel() if self.fall_timer else None
        self.powerup_timer.cancel() if self.powerup_timer else None
        self.round_clock.cancel() if self.round_clock else None

        self.current_widgets = []
        self.target_list = []
        self.new_target_list = []
        self.symbols = []
        self.stop_on = False


    def game_over(self):
        self.stop_game()
        self.pause_layer.change_pause("won") if self.end_obj.game_won() == True else self.pause_layer.change_pause("lost") 
        self.display.set_stacks(self.solved_round) if self.end_obj.game_won() == True else None
        self.pause_logic()
        self.remove_widget(self.display.pause_display)
        Clock.schedule_once(self.end_delay, 4)


    def end_delay(self, dt):
        self.pause_logic()
        self.loading.start("game_win") if self.end_obj.game_won() == True else self.loading.start("game_over")
        self.add_widget(self.loading) if self.loading not in self.children else None
        self.sounds["win"].toggle(True) if self.end_obj.game_won() == True else None


    def show_end(self):
        self.end_obj.display_end()
        self.add_widget(self.end_obj)


    def get_rounds(self):
        try:
            i = 0
            data = self.user_data["unlocked"]["L"]

            for level in data:
                if self.database.get_data(level) == True:
                    i += 1
                else:
                    return i + 10
            return i + 10
        
        except Exception as e:
            pass
            # print("error ", e)    
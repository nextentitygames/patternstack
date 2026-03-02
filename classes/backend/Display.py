from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from A import A
from classes.frontend.Scale import Scale
from classes.globals.widgets.FocusImage import FocusImage




class Display(Widget):
    lower_y = Window.height * .045
    upper_y = Window.height * .9

    container_size = (170, 70)
    
    text_size = 18
    display_font = "fonts/CANDARAB"

    default_stacks = 0
    stacks_value = default_stacks
    base_stacks_text = "Stacks: "
    stacks_text = base_stacks_text + str(stacks_value)
    stacks_display = None
    stacks_pos = (Window.width*.08, upper_y)

    default_round = 1
    round_value = default_round
    base_round_text = "Round: " 
    round_text = base_round_text + str(round_value)
    round_display = None
    round_pos = (Window.width*.3, upper_y)

    default_strikes = 3
    strikes_value = default_strikes
    base_strikes_text = "Attempts: " 
    strikes_text = base_strikes_text + str(strikes_value)
    strikes_display = None
    strikes_pos = (Window.width*.08, lower_y)

    default_shield = 3
    shield_value = default_shield
    base_shield_text = "Shield: " 
    shield_text = base_shield_text + str(shield_value)
    shield_display = None

    default_eraser = 3
    eraser_value = default_eraser
    base_eraser_text = "[E]raser: " 
    eraser_text = base_eraser_text + str(eraser_value)
    eraser_display = None
    eraser_pos = (Window.width*.52, lower_y)

    default_coins = 0
    coins_value = default_coins
    base_coins_text = "" 
    coins_text = str(coins_value)
    coins_display = None
    coins_pos = (Window.width*.765, lower_y)

    default_stop = 3
    stop_value = default_stop
    base_stop_text = "[S]top: " 
    stop_text = base_stop_text + str(stop_value)
    stop_display = None
    stop_pos = (Window.width*.3, lower_y)

    default_slow = 5
    slow_value = default_slow
    base_slow_text = "Slow: " 
    slow_text = base_slow_text + str(slow_value)
    slow_display = None
    slow_pos = (Window.width*.75, Window.height*.03)

    point_pos = (Window.width*.83, upper_y)

    display = "Score: 000000"

    radio_text = {
                    "title": "Radio",
                    "adjust": "[<] back    [>] forward",
                    "power":  "[O] off      [P] on"
                }
    
    radio_display = None
    radio_pos = (Window.width*.675, lower_y)
    radio_size = (300, 100)
    radio_fonts = (11, 6)
    pause_size = 20
    pause_pos = (Window.width*.485, Window.height*.93)



    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        self.scale = Scale()
        self.image_size = self.scale.adjust_size((30, 30))
        self.app_root = A().root()
        self.app_main = A().main()


        self.top_container = FloatLayout()
        self.bottom_container = FloatLayout()

        self.stacks_display = Label(pos=self.scale.adjust_pos(self.stacks_pos), text=str(self.stacks_text), opacity=1, halign="left", text_size=(None, None), size_hint=(None, None), color=get_color_from_hex(self.app_main.base_font_color), font_size=self.scale.adjust_font(self.text_size), font_name=self.display_font)

        self.round_display = Label(pos=self.scale.adjust_pos(self.round_pos), text=str(self.round_text), text_size=(None, None), size_hint=(None, None), halign="left", color=get_color_from_hex(self.app_main.base_font_color), font_size=self.scale.adjust_font(self.text_size), font_name=self.display_font)

        self.pause_display = FocusImage(pos=self.scale.adjust_pos(self.pause_pos), width=self.scale.adjust_number(self.pause_size), height=self.scale.adjust_number(self.pause_size), source=self.app_root.resource_path("images/pause.png"), size_hint=(None, None), textname="pause")

        self.coins_display = FloatLayout(pos=self.scale.adjust_pos(self.coins_pos), size=self.scale.adjust_size(self.container_size))

        self.coins_image = Image(x=self.coins_display.x, y=self.coins_display.y, source=self.app_root.resource_path("images/coin.png"), pos_hint={'x': 0.8, 'center_y': 0.5}, size=self.image_size, size_hint=(None, None), allow_stretch=True, keep_ratio=False)

        self.coins_label = Label(text=str(self.coins_text).rjust(4), opacity=1, valign='middle', halign='right', text_size=(None, None), size_hint=(None, None), pos_hint={'x': 0.85, 'center_y': 0.5}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font, font_size = self.scale.adjust_font(self.text_size))

        self.coins_display.add_widget(self.coins_image)
        self.coins_display.add_widget(self.coins_label)

        self.strikes_display = FloatLayout(pos=self.scale.adjust_pos(self.strikes_pos), size=self.scale.adjust_size(self.container_size))

        self.strikes_image = Image(x=self.coins_display.x, y=self.coins_display.y, source=self.app_root.resource_path("images/strike.png"), pos_hint={'center_x': 0, 'center_y': 0.5}, size=self.image_size, size_hint=(None, None), allow_stretch=True, keep_ratio=False)

        self.strikes_label = Label(text=str(self.strikes_text), opacity=1, text_size=(None, None), size_hint=(1, None), pos_hint={'x': .15, 'center_y': 0.5}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font, font_size = self.scale.adjust_font(self.text_size))

        self.strikes_display.add_widget(self.strikes_image)
        self.strikes_display.add_widget(self.strikes_label)

        self.eraser_display = FloatLayout(pos=self.scale.adjust_pos(self.eraser_pos), size=self.scale.adjust_size(self.container_size))

        self.eraser_image = Image(x=self.coins_display.x, y=self.coins_display.y, source=self.app_root.resource_path("images/eraser.png"), pos_hint={'center_x': 0, 'center_y': 0.5}, size=self.image_size, size_hint=(None, None), allow_stretch=True, keep_ratio=False)

        self.eraser_label = Label(text=str(self.eraser_text), opacity=1, text_size=(None, None), size_hint=(1, None), pos_hint={'x': .07, 'center_y': 0.5}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font, font_size = self.scale.adjust_font(self.text_size))

        self.eraser_display.add_widget(self.eraser_image)
        self.eraser_display.add_widget(self.eraser_label)

        self.stop_display = FloatLayout(pos=self.scale.adjust_pos(self.stop_pos), size=self.scale.adjust_size(self.container_size))

        self.stop_image = Image(x=self.coins_display.x, y=self.coins_display.y, source=self.app_root.resource_path("images/stop.png"), pos_hint={'center_x': 0, 'center_y': 0.5}, size=self.image_size, size_hint=(None, None), allow_stretch=True, keep_ratio=False)

        self.stop_label = Label(text=str(self.stop_text), opacity=1, text_size=(None, None), size_hint=(1, None), pos_hint={'x': .02, 'center_y': 0.5}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font, font_size = self.scale.adjust_font(self.text_size))

        self.stop_display.add_widget(self.stop_image)
        self.stop_display.add_widget(self.stop_label)

        self.slow_display = Label(pos=self.scale.adjust_pos(self.slow_pos), text=str(self.slow_text), text_size=(None, None), size_hint=(None, None), opacity=1, halign="left", font_size=self.scale.adjust_font(self.app_main.base_font_size))
 
        self.point_display = Label(pos=self.scale.adjust_pos(self.point_pos), text=str(self.display), text_size=(None, None),  size_hint=(None, None), opacity=1, halign="left",  color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font, font_size=self.scale.adjust_font(self.text_size))

        self.show_radio()


    def add_layers(self):
        self.add_widget(self.stacks_display)
        self.add_widget(self.round_display)
        self.add_widget(self.pause_display)
        self.add_widget(self.strikes_display)
        self.add_widget(self.eraser_display)
        self.add_widget(self.coins_display)
        self.add_widget(self.stop_display)
        self.add_widget(self.point_display)
        self.add_widget(self.radio_display)


    def remove_layers(self):
        self.remove_widget(self.stacks_display)
        self.remove_widget(self.round_display)
        self.remove_widget(self.pause_display)
        self.remove_widget(self.strikes_display)
        self.remove_widget(self.eraser_display)
        self.remove_widget(self.point_display)
        self.remove_widget(self.coins_display)
        self.remove_widget(self.stop_display)
        self.remove_widget(self.radio_display)


    def set_stacks(self, amount, default=None):
        if not default:
            self.stacks_value = amount
        else:
            self.stacks_value = self.default_stacks
        self.stacks_text = self.base_stacks_text + str(self.stacks_value)
        self.stacks_display.text = self.stacks_text


    def set_round(self, amount, default=None):
        if not default:
            self.round_value = amount
        else:
            self.round_value = self.default_round
        self.round_text = self.base_round_text + str(self.round_value)
        self.round_display.text = self.round_text


    def set_strikes(self, amount, default=None):
        if not default:
            self.strikes_value = self.strikes_value + amount
        else:
            self.strikes_value = self.default_strikes
        self.strikes_text = self.base_strikes_text + str(self.strikes_value)
        self.strikes_label.text = self.strikes_text
        self.app_main.check_end_game() 


    def set_eraser(self, amount, default=None):
        if not default:
            self.eraser_value = self.eraser_value + amount
        else:
            self.eraser_value = self.default_eraser
        self.eraser_text = self.base_eraser_text + str(self.eraser_value)
        self.eraser_label.text = self.eraser_text


    def set_coins(self, amount, default=None):
        if not default:
            self.coins_value = self.coins_value + amount
        else:
            self.coins_value = self.default_coins
        self.coins_text = self.base_coins_text + str(self.coins_value)
        self.coins_label.text = self.coins_text


    def set_stop(self, amount, default=None):
        if not default:
            self.stop_value = self.stop_value + amount
        else:
            self.stop_value = self.default_stop
        self.stop_text = self.base_stop_text + str(self.stop_value)
        self.stop_label.text = self.stop_text


    def reset_display(self):
        functions = [self.set_stacks, self.set_round, self.set_strikes, self.set_shield, self.set_eraser, self.set_coins, self.set_stop, self.set_slow]

        for method in functions:
            method(0, True)


    def show_radio(self):
        self.radio_display = FloatLayout(pos=self.scale.adjust_pos(self.radio_pos), size=self.scale.adjust_size(self.radio_size), size_hint=(None, None))
    
        title= Label(text=str(self.radio_text["title"]), opacity=1, text_size=(None, None), size_hint=(1, 1), pos_hint={"x": 0, "center_y": .75}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font) 
        title.font_size = self.scale.adjust_number(self.radio_fonts[0])
        title.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.radio_display.add_widget(title)

        label = Label(text=str(self.radio_text["adjust"]), opacity=1, text_size=(None, None), size_hint=(1, 1), pos_hint={"x": .275, "center_y": .885}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font) 
        label.font_size = self.scale.adjust_number(self.radio_fonts[1])
        label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.radio_display.add_widget(label)

        label = Label(text=str(self.radio_text["power"]), opacity=1, text_size=(None, None), size_hint=(1, 1), pos_hint={"x": .275, "center_y": .685}, color=get_color_from_hex(self.app_main.base_font_color), font_name=self.display_font) 
        label.font_size = self.scale.adjust_number(self.radio_fonts[1])
        label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.radio_display.add_widget(label)
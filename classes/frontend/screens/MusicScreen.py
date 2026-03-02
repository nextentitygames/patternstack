from kivy.properties import (ObjectProperty)
from kivy.clock import Clock
from kivy.uix.widget import Widget
from A import A
from classes.globals.Colors import Colors
from classes.globals.widgets.FocusImage import FocusImage
from kivy.uix.image import Image 
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from classes.frontend.Scale import Scale
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


class MusicScreen(Widget):

    path = "sounds/music"
    img_path = ["images/radio_front.png", "images/radio_back.png"]
    containers = []
    radio_size = (Window.width * .25, Window.width * .075)
    radio_pos = (Window.width * .655, Window.height * .75)
    main_container = None
    image = None
    label = None
    music_text = None

    scroll_timer = None
    scroll_interval = .2
    scroll_limit = 18
    start_value = 0
    end_value = scroll_limit
    space_value = "   "




    def __init__(self, **kwargs):
        super(MusicScreen, self).__init__(**kwargs)





    def show_choice(self, side):
        self.start_value = 0
        self.end_value = self.scroll_limit
        self.scroll_timer.cancel() if self.scroll_timer else None
        self.scroll_timer = None
        self.music_text = str(A().root().current_sound) + (self.space_value if len(str(A().root().current_sound)) > self.scroll_limit else "")
        self.set_current_text()
        self.remove_widget(self.main_container) 
        self.main_container = FloatLayout(size=Scale().adjust_size(self.radio_size), pos=self.radio_pos)

        self.image = Image(source=self.img_path[0] if side == True else self.img_path[1], x=self.main_container.x, y=self.main_container.y, pos_hint={'x': 0, 'center_y': 0.5}, size=Scale().adjust_size(self.radio_size), size_hint=(None, None), allow_stretch=True, keep_ratio=False)

        self.label = Label(text=self.current_text, color=Colors.WHITE, font_name="fonts/CANDARAB", pos_hint={'x': 0.0, 'center_y': 0.5}, size_hint=(1, 1))
        self.label.font_size = Scale().adjust_number(10)
        self.label.bind(texture_size=self.label.setter('size'))
        
        self.main_container.remove_widget(self.image)
        self.main_container.remove_widget(self.label)
        self.main_container.add_widget(self.image)
        self.main_container.add_widget(self.label)
        self.add_widget(self.main_container)

        self.scroll_text() if len(str(A().root().current_sound))  > self.scroll_limit else None

    
    def scroll_text(self):
        self.scroll_timer = Clock.schedule_interval(self.move_scroll, self.scroll_interval)
        

    def move_scroll(self, dt):
        # advance the scroll indices with wrap-around
        self.start_value = (self.start_value + 1) % len(self.music_text)
        self.end_value = (self.end_value + 1) % len(self.music_text)

        # update text only
        self.set_current_text()
        self.label.text = self.current_text


    def set_current_text(self):
        # handle wrap-around in one line
        if self.start_value < self.end_value:
            self.current_text = self.music_text[self.start_value:self.end_value]
        else:
            self.current_text = self.music_text[self.start_value:] + self.music_text[:self.end_value]


from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
import math as Math
from kivy.uix.label import Label
from kivy.core.window import Window
from A import A
from classes.frontend.Scale import Scale
from kivy.utils import get_color_from_hex




class Timer(Widget):
    display = None
    stopped = True
    timer = 0
    hours = 0
    hours_display = "00"
    minutes = 0
    minutes_display = "00"
    seconds = 0
    seconds_display = "00"
    clock_display = "Time: " + hours_display + ":" + minutes_display + ":" + seconds_display
    move_timer = float(0)
    instance = None
    move_instance = None
    scale = Scale()




    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)
        self.display = Label(pos=Scale().adjust_pos([Window.width*.66, Window.height*.9]), text=str(self.clock_display), opacity=0, halign="left", text_size=(None, None), size_hint=(None, None), color=get_color_from_hex(A().main().base_font_color), font_name="fonts/CANDARAB", font_size=Scale().adjust_font(18))
        self.add_widget(self.display)

        Window.bind(on_resize=self.on_window_resize)


    def on_window_resize(self, window, width, height):
        pass


    def start(self):
        self.stopped = False
        self.timer = 0
        self.instance = Clock.schedule_interval(self.callback, 1) if not self.instance else None

    def restart(self):
        if self.timer > 0:
            self.stopped = False 


    def stop(self):
        self.stopped = True


    def set_display(self):
        self.hours = Math.floor(self.timer / 3600)
        self.minutes = Math.floor(self.timer / 60) % 60 
        self.seconds = self.timer % 60

        if(len(str(self.hours))>1):
            self.hours_display = str(self.hours)
        else:
            self.hours_display = "0" + str(self.hours) 

        if(len(str(self.minutes))>1):
            self.minutes_display = str(self.minutes)
        else:
            self.minutes_display = "0" + str(self.minutes) 

        if(len(str(self.seconds))>1):
            self.seconds_display = str(self.seconds)
        else:
            self.seconds_display = "0" + str(self.seconds) 

        self.clock_display = self.hours_display + ":" + self.minutes_display + ":" + self.seconds_display

        self.display.text = "Time: " + self.clock_display


    def callback(self, dt):
        if not self.stopped:
            self.timer = self.timer + 1
            self.set_display()


    def get_displayed_timer(self):
        return str(self.timer)


    def start_move_timer(self):
        self.move_instance = Clock.schedule_interval(self.call_move_timer, .1)


    def call_move_timer(self, dt):
        self.move_timer = float(self.move_timer + .1)


    def reset_move_timer(self):
        self.move_timer = 0
        self.start_move_timer()


    def get_move_timer(self):
        return str(self.move_timer)
    

    def get_time(self):
        return str(self.hours_display + ":" + self.minutes_display)
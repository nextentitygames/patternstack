from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from classes.frontend.Scale import Scale


class Meter(Widget):

    meter_types = {
        "frame": {
            "color": "#3f3f3f",
            "duration": 5
        },
        "stop": {
            "color": "#8b1832",
            "duration": 5
        },
        "freeze": {
            "color": "#9030cd",
            "duration": 5
        },
    }

    base_pos = current_pos = (Window.width*.11, Window.height*.8575)
    size_increment = 0
    interval = 0
    elapsed_time = 0
    timer = None
    color = None
    meter = None
    meter_type = None


    def __init__(self, meter_type, autostart=None, **kwargs):
        self.meter_type = meter_type
        super().__init__(**kwargs)

        self.full_width = Scale().adjust_number(75)
        self.full_height = Scale().adjust_number(17)
        self.base_size = self.current_size = (0, Scale().adjust_number((17)))
        with self.canvas:
            
            self.color = self.get_color() 
            self.meter = self.get_meter()
            self.bind(pos=self.update_rect, size=self.update_rect)

        self.size_increment = self.get_size_increment()
        self.interval = self.get_interval()

        self.start() if autostart and meter_type != "frame" else self.set_frame()


        

    def update_rect(self, *args):
        self.meter.pos = self.pos
        self.meter.size = self.current_size


    def change_meter(self, new):
        self.stop_timer()
        self.meter_type = new
        self.color = self.get_color()
        self.meter = self.get_meter()
        self.size_increment = self.get_size_increment()
        self.interval = self.get_interval()
        self.start()


    def get_color(self):
        return Color(*get_color_from_hex(self.meter_types[self.meter_type]["color"])) 
    

    def get_meter(self):
        self.current_size = self.base_size
        self.current_pos = self.pos
        return Rectangle(pos=self.pos, size=self.size)


    def get_size_increment(self):
        return self.full_width/100
    

    def get_interval(self):
        return self.meter_types[self.meter_type]["duration"]/100
    

    def start(self):
        self.opacity = 1
        self.elapsed_time = 0
        self.current_size = (0, self.full_height) 
        self.size = self.current_size
        self.timer = Clock.schedule_interval(self.draw, self.interval)


    def set_frame(self):
        self.opacity = .45
        self.current_size = (self.full_width, self.full_height) 
        self.update_rect()
        self.timer = Clock.schedule_interval(self.meter_off, self.meter_types[self.meter_type]["duration"]) 


    def draw(self, dt):
        self.elapsed_time += dt
        x_size = self.current_size[0] + self.size_increment
        self.current_size = (x_size, self.current_size[1])
        self.size = self.current_size
        self.update_rect()

        if self.current_size[0] >= self.full_width:
            self.meter_off()


    def meter_off(self, dt=None):
        self.stop_timer()
        self.size = self.base_size
        self.opacity = 0
        self.update_rect()


    def stop_timer(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None
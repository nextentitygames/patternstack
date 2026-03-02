import os
import ctypes
# os.environ['KIVY_NO_CONSOLELOG'] = '1'
# os.environ['KIVY_NO_FILELOG'] = '1'
# os.environ["KIVY_NO_ARGS"] = "1"

from kivy.config import Config
if not Config.has_section('audio'):
    Config.add_section('audio')

Config.set('audio', 'audio', 'sdl2') 
Config.set('audio', 'buffer', '1000') 

def get_screen_size():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

Config.set('graphics', 'width', get_screen_size()[0])
Config.set('graphics', 'height',  get_screen_size()[1])

Config.set('graphics', 'resizable', False)


import sys
import random
from random import randint
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.resources import resource_add_path
from classes.PatternStack import PatternStack
from classes.backend.Data import Data
from classes.frontend.screens.Screens import Screens



if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')

def add_meipass_resource_path():
    if hasattr(sys, "_MEIPASS"):
        resource_add_path(os.path.join(sys._MEIPASS))




class PatternStackApp(App):
    main = None
    screens = None
    login_required = False
    user_cookie = None
    new_cookie = "" 
    jwt_lifetime = 7
    jwt_test = 100
    jwt_secret = ""
    secret_length = 32
    original_ratio = 1286/724
    current_width = Window.width
    current_height = Window.height
    current_size = (Window.width, Window.height)
    base_width = 1286
    base_height = 724
    current_skin = "001"
    current_sound = "001"
    current_hud = "001.png"
    



    def on_start(self):
            Clock.schedule_interval(lambda dt: None, 0)


    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'): 
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)


    def build(self):
        self.random_hud()
        self.random_skin()
        self.main = PatternStack()
        self.main.scale.scale_widgets()
        self.bypass_login() if self.login_required is False else None
        self.screens = Screens()
        self.main.title_obj.menu_buttons() if self.login_required is False else None
        Clock.schedule_interval(lambda dt: None, 0)
        return self.main
    
        
    def random_hud(self):
        shade = random.choice(["light", "dark"])
        # shade = random.choice(["light"])
        hud = random.choice(os.listdir(self.resource_path("images/huds/" + shade)))
        self.current_hud = self.resource_path("images/huds/" + shade + "/" + hud)
    
    
    def random_skin(self):
        skin = "00"  + str(randint(1, len(os.listdir(self.resource_path("images/screens/")))))
        self.current_skin = skin
        return skin
         

    def new_game(self):
        self.main.remove_widget(self.main.end_obj)
        self.main.reset()
        self.bypass_login()
        self.main.loading.start("start_game")
        self.main.add_widget(self.main.loading) if self.main.loading not in self.main.children else None


    def bypass_login(self):
        self.main.user_data = Data().user_data
        self.main.inventory_data = Data().inventory_data
        self.main.store_data = Data().store_data
        self.main.achievements_data = Data().achievements_data
        self.main.new_obj.data = Data().whatsnew_data




if __name__ == "__main__":
    add_meipass_resource_path()
    PatternStackApp().run()
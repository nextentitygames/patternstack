import time
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from classes.globals.Colors import Colors
from kivy.clock import Clock
from kivy.uix.label import Label
import webbrowser
from kivy.uix.image import Image 




class FocusLayout(ButtonBehavior, FloatLayout):
    hand_cursor = False
    cursor_coords = None

    cursors = ["hand", "arrow"]

    return_text = "Return"

    text = None

    isclicked = False

    actions = None


    def __init__(self, textname, texttype=None, screen=None, **kwargs):
        self.textname = textname if textname else ""
        self.texttype = texttype if texttype else ""
        super().__init__(**kwargs)
        self.bind(on_press=self.on_click)
        Window.bind(mouse_pos=self.on_mouse_move)
        self.allow_stretch = True
        self.keep_ratio = False
        self.actions = {
            "profile": self.profile_handler
        }


    def on_click(self, touch):
        if self.collide_point(*touch.pos):
            self.process() 
        return True
    

    def on_mouse_move(self, window, pos):
        self.check_mouse() if App.get_running_app().main.user_data != None else None
     
    
    def process(self):
        self.actions[self.textname]()
        self.cursor_handler(False)


    def check_mouse(self, login=False):
        x, y = Window.mouse_pos

        for item in App.get_running_app().main.children:
            for obj in item.children:
                try:
                    if "FocusLayout" in str(obj) and obj.parent in App.get_running_app().main.children and App.get_running_app().main.user_data:
                        if x > obj.x and x < obj.x + obj.width and y > obj.y and y < obj.y + obj.height:    
                            self.cursor_handler(True)  
                            return True
                except:
                    pass
              

    
    def cursor_handler(self, condition):
        if condition:
            Window.set_system_cursor(self.cursors[0])
        else:
            Window.set_system_cursor(self.cursors[1])


    def profile_handler(self):
        if App.get_running_app().main != None:
            App.get_running_app().main.screen_handler("profile")
            App.get_running_app().main.profile_obj.set_text(App.get_running_app().main.user_data)
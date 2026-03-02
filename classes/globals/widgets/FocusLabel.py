from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
from classes.globals.Colors import Colors


class FocusLabel(ButtonBehavior, Label):
    hand_cursor = False
    cursor_coords = None

    cursors = ["hand", "arrow"]

    return_text = "Return"

    text = None

    isclicked = False


    def __init__(self, textname, **kwargs):
        self.textname = textname
        super().__init__(**kwargs)
        self.bind(on_press=self.on_click)
        Window.bind(mouse_pos=self.on_mouse_move)




    def on_click(self, touch):
        if self.collide_point(*touch.pos):
            self.process()
        return True
    

    def on_mouse_move(self, window, pos):
        pass       
    

    def process(self):
        if self.isclicked == False:
            App.get_running_app().main.new_obj.show_handler(True)
            self.isclicked = True 
        else:
            App.get_running_app().main.new_obj.show_handler(False)
            self.isclicked = False 
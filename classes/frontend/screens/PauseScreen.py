from kivy.properties import (
ObjectProperty
)
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from classes.frontend.Scale import Scale
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout



class Pause(Widget):
    blind = ObjectProperty(None)
    pause_label = None
    pause_label2 = None
    pause_text = {
        "pause": "Paused",
        "won": "You Won!!!",
        "lost": "You Lost..."
    }
    pause_size = 22
    quit_size = 14
     
    
    def __init__(self, **kwargs):
        super(Pause, self).__init__(**kwargs)

        with self.canvas.before:
            self.color = Color(0,0,0,1)
            self.rect = Rectangle(pos=self.pos, size=Window.size)

        with self.canvas:
            self.opacity = .7

        self.text_container = FloatLayout(pos=(Window.width * .875, Window.height * .73), size=Scale().adjust_size([300, 300]))

        self.pause_label = Label(text=self.pause_text["pause"], font_size=Scale().adjust_number(self.pause_size), font_name="fonts/CANDARALI", center_x=Window.width*.5, center_y=Window.height *.5)
        self.add_widget(self.pause_label)

        self.pause_label2 = Label(text="[SPACE] - Resume", font_size=Scale().adjust_number(self.quit_size), halign="left", font_name="fonts/CANDARA", pos_hint={"center_x": 0, "center_y": .8})
        self.pause_label2.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.text_container.add_widget(self.pause_label2)

        self.exit_label = Label(text="[X] - Quit Game", font_size=Scale().adjust_number(self.quit_size), halign="left", font_name="fonts/CANDARA", pos_hint={"center_x": 0, "center_y": .6})
        self.exit_label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.text_container.add_widget(self.exit_label)
        
        self.restart_label = Label(text="[R] - Restart Game", font_size=Scale().adjust_number(self.quit_size), halign="left", font_name="fonts/CANDARA", pos_hint={"center_x": 0, "center_y": .4})
        self.restart_label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.text_container.add_widget(self.restart_label)

        self.main_label = Label(text="[M] - Main Menu", font_size=Scale().adjust_number(self.quit_size), halign="left", font_name="fonts/CANDARA", pos_hint={"center_x": 0, "center_y": .2})
        self.main_label.bind(size=lambda instance, value: setattr(instance, 'text_size', value))
        self.text_container.add_widget(self.main_label)

        self.add_widget(self.text_container)

        self.bind(pos=self._update_rect, size=self._update_rect)
        

    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size    


    def change_pause(self, text):
        self.remove_widget(self.pause_label)
        self.remove_widget(self.text_container)
        self.pause_label.text = self.pause_text[text]
        self.add_widget(self.pause_label) if self.pause_label not in self.children else None

    
    def reset_pause(self):
        self.remove_widget(self.pause_label)
        self.remove_widget(self.text_container)
        self.pause_label.text = self.pause_text["pause"]
        self.add_widget(self.pause_label)
        self.add_widget(self.text_container)
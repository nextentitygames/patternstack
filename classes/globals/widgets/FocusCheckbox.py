from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout


class FocusCheckbox(CheckBox):

    is_checked = False
    layout = None
    bg_color = None 



    def __init__(self, boxname, **kwargs):
        self.boxname = boxname
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (15, 15)

        with self.canvas.before:
            self.bg_color = Color(.5, .5, .5, 1)
            self.layout = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self._update_rect, size=self._update_rect)
        self.bind(active=self.on_activate)




    def _update_rect(self, *args):
        self.layout.pos = self.pos
        self.layout.size = self.size


    def on_activate(self, box, active):
        App.get_running_app().main.profile_obj.toggle_edit(self.boxname, active)
        App.get_running_app().main.profile_obj.edit_fields[self.boxname].text_value = ""
        self.is_checked = active
        return active
from kivy.uix.textinput import TextInput

class FocusTextInput(TextInput):
    text_value = ""

    def __init__(self, **kwargs):
        super(FocusTextInput, self).__init__(**kwargs)
        self.bind(on_touch_down=self.on_click)
        self.bind(on_text_validate=self.on_enter)
        self.bind(text=self.on_text)
        self.bind(focus=self.on_focus)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            return super(FocusTextInput, self).on_touch_down(touch)
        return False

    def on_click(self, instance, touch):
        if self.collide_point(*touch.pos):
            self.focus = True
        if instance.collide_point(*touch.pos):
            instance.focus = True
        return False
    
    def on_enter(self, instance):
        print('Entered text: ', self.text)
        return True

    def on_text(self, instance, value):
        if value[len(value)-1 :] != " ":
            self.text_value = value
        else:
            self.text = self.text.replace(" ", "")
        self.text_value = self.text


    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User defocused', instance)
from kivy.app import App
from kivy.uix.widget import Widget

class A(Widget):

    def root(self):
        return App.get_running_app()
    
    def main(self):
        return App.get_running_app().main
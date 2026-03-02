from random import randint
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from A import A
from classes.frontend.Scale import Scale
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import (Color, Rectangle)
from kivy.clock import Clock
from kivy.uix.image import AsyncImage



class Loading(Widget):

    load_container = None
    load_text = None
    load_animation = None
    load_timer = None
    event = None
    events = None
    load_font = 18
    load_delay = 1/32
    slow_delay = 1/6
    graphics = ["images/animations/loading/load_start.gif", "images/animations/loading/load_new.gif", "images/animations/loading/load_win.gif", "images/animations/loading/load_gameover.gif", "images/animations/loading/load_tutorial.gif", "images/animations/loading/load_whatsnew.gif", "images/animations/loading/load_.gif"]



    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app_root = A().root()
        self.app_main = A().main()
        
        with self.canvas:
            self.color = Color(0,0,0,1)
            self.rect = Rectangle(pos=self.pos, size=Window.size)

        self.load_container = FloatLayout(size=Scale().adjust_size((Window.width*.5, 350)))
        self.load_container.pos = ((Window.width - self.load_container.width)/2, (Window.height - self.load_container.height)/2)

        self.load_text = Label(text="Loading...", valign='bottom', halign='center', pos_hint={"center_x": .5, "center_y": 0.05}, size_hint=(1, 1), font_name="fonts/CANDARAB")

        self.load_text.font_size = Scale().adjust_number(self.load_font)
        self.load_text.bind(size=lambda instance, value: setattr(instance, 'text_size', value))

        self.load_animation = AsyncImage(source="", size_hint=(None, None), size=Scale().adjust_size((450, 450)), pos_hint={"center_x": 0.5, "center_y": 0.7}, anim_delay=1/32)

        self.load_container.add_widget(self.load_text)
        self.load_container.add_widget(self.load_animation)
        self.add_widget(self.load_container)

    
    def start(self, event):
        
        self.events = {
            "start_game": {
                "trigger": A().main().start_game,
                "text": [
                    "Beginning Quest...",
                    "Launching Adventure...",
                    "Entering Realm...",
                    "Starting Journey...",
                    "Initiating Battle...",
                    "Unlocking Level...",
                    "Activating Mode...",
                    "Commencing Mission...",
                    "Engaging Play...",
                    "Opening World..."
                ],
            },
            "new_game": {
                "trigger": A().root().new_game,
                "text": [
                    "Fresh Start...",
                    "New Adventure...",
                    "Clean Slate...",
                    "Begin Again...",
                    "Next Journey...",
                    "Brand New...",
                    "Starting Fresh...",
                    "New Campaign...",
                    "First Quest...",
                    "Adventure Awaits..."
                ],
            },
            "game_win":{
                "trigger": A().main().show_end,
                "text": [
                    "Victory Achieved!",
                    "Mission Complete!",
                    "Champion Declared!",
                    "Triumph Earned!",
                    "Quest Finished!",
                    "Level Conquered!",
                    "Success Achieved!",
                    "Glory Won!",
                    "Goal Reached!",
                    "Battle Won!"
                ],
            },
            "game_over":{
                "trigger": A().main().show_end,
                "text": [
                    "Try Again!",
                    "Mission Failed!",
                    "Battle Lost!",
                    "Quest Ended!",
                    "Defeat Awaits!",
                    "Level Failed!",
                    "Challenge Lost!",
                    "Game Ended!",
                    "You Lost!",
                    "Better Luck!"
                ],
            },
            "tutorial":{
                "trigger": self.router,
                "text": [
                    "Preparing Guide...",
                    "Loading Instructions...",
                    "Starting Tutorial...",
                    "Initializing Lesson...",
                    "Booting Guide...",
                    "Setting Up...",
                    "Launching Tutorial...",
                    "Opening Lesson...",
                    "Tutorial Incoming...",
                    "Getting Ready..."
                ],
            },
            "whats_new":{
                "trigger": self.router,
                "text": [
                    "Fetching Updates...",
                    "Loading News...",
                    "Checking Headlines...",
                    "Retrieving Stories...",
                    "Getting Updates...",
                    "Loading Articles...",
                    "Fetching Content...",
                    "Retrieving News...",
                    "Checking Updates...",
                    "Updating Feed..."
                ],
            }
        }

        self.event = event
        self.opacity = 1
        self.load_text.text = self.random_texts()
        self.load_animation.source =  self.app_root.resource_path(self.random_graphics())
        self.load_animation.reload()
        self.remove_widget(self.load_container)
        self.add_widget(self.load_container)
        self.load_timer = Clock.schedule_once(self.turn_off, randint(5, 8))


    def router(self):
        A().main().screen_handler(self.event)


    def random_texts(self):
        return self.events[self.event]["text"][randint(0, len(self.events[self.event]["text"])-1)]


    def random_graphics(self):
        graphic = self.graphics[randint(0, len(self.graphics)-1)]
        if "_.gif" in graphic:
            self.load_animation.anim_delay = self.slow_delay
        return graphic 


    def turn_off(self, dt):
        self.remove_widget(self.load_container)
        self.load_animation.source = ""
        self.load_animation.anim_delay = self.load_delay
        self.opacity = 0
        self.load_timer.cancel()
        self.load_timer = None
        self.events[self.event]["trigger"]() 
        self.event = None
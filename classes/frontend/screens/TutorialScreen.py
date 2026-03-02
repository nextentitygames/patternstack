from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from classes.frontend.Scale import Scale
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from classes.globals.widgets.FocusImage import FocusImage



class TutorialScreen(Widget):

    label_text = {
        "basics": "BASICS\n\n- Collect falling shapes to match the target list on the left side of the screen.\n\n- To get the first shape, click on it. Afterward, click your stack and drag the mouse to move your stack across the screen. Try to catch shapes or powerups on top of your stack. Once you match a stack, press 'Enter' to process it.\n\n- Try to only collect shapes that match the pattern, any shapes that don't will prevent you from completing the stack.\n\n- Avoid mines to prevent your stack from exploding.\n\n- Powerups and coins occasionally appear. Collect them to help you win.",
        "powerups": "\n\n\nPOWERUPS\n\nStop - Press 'S' to use a stop powerup to freeze the screen. For a short time, you can touch/click any shape, powerup or coin to collect it.\n\nErase - Press 'E' to remove a shape from the stack. Use it to fix your stack in case you collect the wrong shape. \n\nStrike - Add this to increase your strike count.\n\nCoins - Can be collected to increase the amount of Gold you have in your inventory.",
        "pause": "\n\n\nPAUSE\n\n - Press 'SPACEBAR' or the pause icon at the top middle of the screen to stop/start the game.",
        "radio": "\n\n\nSTACK RADIO\n\n - During the game, choose from a variety of background music using Stack Radio!\n\n\n   Controls:\n\n    'O' - off\n    'P' - on\n\n    '<' - back\n    '>' - forward"
    }
        
    
    button_text = ["Return"]

    scale = Scale()

    title_source = None

    button_source = None

    tutorial_bg = None

    tutorial_label = None

    powerups_label = None

    return_button = None

    scroll_width = outer_box_width = 400
    scroll_height = 250
    box_width = outer_box_width - 10

    scroll_size = [scroll_width, scroll_height]

    container = None




    def __init__(self, **kwargs):
        super(TutorialScreen, self).__init__(**kwargs)

        try:
            title_source = f"images/screens/{App.get_running_app().screens.current_skin}/skins/tutorial.png"
            button_source = f"images/screens/{App.get_running_app().screens.current_skin}/buttons/return.png"
        except:
            title_source = f"images/screens/001/skins/tutorial.png"
            button_source = f"images/screens/001/buttons/return.png"  

        self.tutorial_bg = Image(pos=(0,0), size=(Window.width, Window.height), source=title_source, allow_stretch=True, keep_ratio=False)

        self.add_widget(self.tutorial_bg)
        self.show_screen()


    def show_screen(self):
        x_coord = .25
        y_coord = .5

        self.container = ScrollView(size_hint=(1, 1), width=Scale().adjust_number(self.scroll_size[0]), height=Scale().adjust_number(self.scroll_size[1]), center_x=Window.width * .5, center_y=Window.height*y_coord, do_scroll_y=True)

        outer_box = BoxLayout(width=Scale().adjust_number(self.outer_box_width), orientation='vertical', size_hint_y=None)
        outer_box.bind(minimum_height=outer_box.setter('height'))

        y_pos = .85
        for key in self.label_text.keys():
            label = Label(text=self.label_text[key], width=700, height=150, text_size=(Scale().adjust_number(self.box_width), None), size_hint_y=None,  opacity=1, color=(1,1,1,1), font_name="fonts/CANDARAB")
            label.font_size = Scale().adjust_number(14)
            label.bind(texture_size=label.setter('size'))

            box = BoxLayout(width=self.box_width, orientation='vertical', size_hint_y=None)
            box.bind(minimum_height=box.setter('height'))
            box.add_widget(label)
            outer_box.add_widget(box)

            y_pos -= .15
        
        self.container.add_widget(outer_box)

        Clock.schedule_once(lambda dt: self.scroll_top(self.container), 1) if self.container.scroll_y != 1 else None

        self.add_widget(self.container)

        x_coord = .4
        y_coord = .05

        self.return_button = FocusImage(size=Scale().calculate_scale([150, 26]), x=Scale().adjust_x(Window.width*x_coord), y=Scale().adjust_y(Window.height*y_coord), opacity=1, source="", textname="tutorial_return")

        self.add_widget(self.return_button)


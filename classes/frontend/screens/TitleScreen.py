from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from A import A
from classes.frontend.Scale import Scale
from kivy.uix.image import Image
from classes.globals.Colors import Colors
from classes.globals.widgets.FocusImage import FocusImage
from kivy.uix.label import Label
from kivy.clock import Clock



class TitleScreen(Widget):



    login_text = "Checking for existing credentials..."
    login_label = None

    pending_text = "Pending login..."
    pending_label = None

    starting_text = "Starting game..."
    starting_label = None

    request_text = "Please login..."
    request_label = None

    login = None
    start = None

    data = None

    scale = Scale()

    title_bg = None

    store_button = None

    profile_container = None

    profile_bg = None

    title_profile = None

    title_username = None

    login_timer = None

    plates = []

    title_buttons = []

    current_avatar = ""

    starting_font = 18

    login_button = None
    account_button = None

    flash_incr = 0
    flash_label = None
    flash_interval = None



    def __init__(self, **kwargs):
        super(TitleScreen, self).__init__(**kwargs)

        win_width, win_height = A().root().current_size
        login_offset = 0 if A().root().login_required else 0.04

        # Full-screen background
        self.title_bg = Image(
            pos=(0, 0),
            size=(win_width, win_height),
            source="",
            allow_stretch=True,
            keep_ratio=False
        )

        # Button sizes
        btn_width = Scale().adjust_number(150 * 1.25)
        btn_height = Scale().adjust_number(26 * 1.25)

        # X coordinate for all buttons
        x_coord = 0.515

        # Start Button
        y_coord = 0.625
        self.start_button = FocusImage(
            size=[btn_width, btn_height],
            x=(win_width * x_coord) - (btn_width / 2),
            y=(win_height * (y_coord - login_offset)) - (btn_height / 2),
            opacity=1,
            source="",
            textname="title_start",
            allow_stretch=True,
            keep_ratio=False
        )

        # Tutorial Button
        y_coord -= 0.075
        self.tutorial_button = FocusImage(
            size=[btn_width, btn_height],
            x=(win_width * x_coord) - (btn_width / 2),
            y=(win_height * (y_coord - login_offset)) - (btn_height / 2),
            opacity=1,
            source="",
            textname="title_tutorial",
            allow_stretch=True,
            keep_ratio=False
        )

        # What's New Button
        y_coord -= 0.15  # combining two decrements
        self.whats_new_button = FocusImage(
            size=[btn_width, btn_height],
            x=(win_width * x_coord) - (btn_width / 2),
            y=(win_height * (y_coord + (0.035 if not A().root().login_required else 0))) - (btn_height / 2),
            opacity=1,
            source="",
            textname="title_new",
            allow_stretch=True,
            keep_ratio=False
        )

        # # DEMO LABEL
        # demo_font_size = Scale().adjust_number(18)
        # demo_x_ratio = 0.5175
        # demo_y_ratio = 0.415 - login_offset

        # self.flash_label = Label(
        #     text="DEMO VERSION",
        #     font_size=demo_font_size,
        #     color=Colors.DARK_RED,
        #     x=(win_width * demo_x_ratio) - (demo_font_size * len("DEMO VERSION") / 4),  # approximate center by text width
        #     y=(win_height * demo_y_ratio) - (demo_font_size / 2)
        # )

        # self.flash_incr = 0
        # self.flash_interval = Clock.schedule_interval(self.demo_flash, 1)

        self.exit_text()
    # def __init__(self, **kwargs):
    #     super(TitleScreen, self).__init__(**kwargs)

    #     self.title_bg = Image(pos=(0,0), width=A().root().current_size[0], height=A().root().current_size[1], source="", allow_stretch=True, keep_ratio=False)

    #     x_coord = .515
    #     y_coord = .625

    #     self.start_button = FocusImage(size=[Scale().adjust_number(150*1.25), Scale().adjust_number(26*1.25)], center_x=Scale().adjust_center_x(A().root().current_size[0]*x_coord), center_y=Scale().adjust_center_y(A().root().current_size[1]*(y_coord-(0 if A().root().login_required == True else .04))), opacity=1, source="", textname="title_start", allow_stretch=True, keep_ratio=False)

    #     y_coord -= .075

    #     self.tutorial_button = FocusImage(size=[Scale().adjust_number(150*1.25), Scale().adjust_number(26*1.25)], center_x=Scale().adjust_center_x(A().root().current_size[0]*x_coord), center_y=Scale().adjust_center_y(A().root().current_size[1]*(y_coord-(0 if A().root().login_required == True else .04))), opacity=1, source="", textname="title_tutorial")

    #     y_coord -= .075
    #     y_coord -= .075

    #     self.whats_new_button = FocusImage(size=[Scale().adjust_number(150*1.25), Scale().adjust_number(26*1.25)], x=Scale().adjust_center_x(A().root().current_size[0]*x_coord), center_y=Scale().adjust_center_y(A().root().current_size[1]*(y_coord+(0 if A().root().login_required == True else .035))), opacity=1, source="", textname="title_new")

        self.exit_text()


    def menu_buttons(self):
        for widget in self.title_buttons:
            self.remove_widget(widget)

        self.title_buttons = []

        App.get_running_app().screens.set_skin()

        self.title_buttons = [self.start_button, self.tutorial_button, self.whats_new_button, self.exit_label] 
  
        self.remove_widget(self.title_bg)
        self.add_widget(self.title_bg)
        for widget in self.title_buttons:
            self.add_widget(widget)

        self.demo_text()


    def demo_text(self, toggle=True):
        self.remove_widget(self.flash_label)
        self.flash_incr = 0
        self.flash_label = Label(text="DEMO VERSION", font_size=Scale().adjust_number(18), color=Colors.DARK_RED, center_x=Scale().adjust_center_x(A().root().current_size[0]*.5175), center_y=Scale().adjust_center_y(A().root().current_size[1]*(.415-(0 if A().root().login_required == True else .04)))) if not self.flash_label else self.flash_label
        self.flash_interval.cancel() if self.flash_interval else None
        self.flash_interval = Clock.schedule_interval(self.demo_flash, 1) if toggle == True else None


    def demo_flash(self, dt):
        self.flash_incr += 1
        self.flash_label.text == "" if self.flash_incr % 2 == 0 else "DEMO VERSION"
        self.remove_widget(self.flash_label) if self.flash_incr % 2 == 0 else self.add_widget(self.flash_label)


    def exit_text(self):
        win_width, win_height = A().root().current_size
        font_size = Scale().adjust_number(12)

        self.exit_label = Label(
            text="[X] - Quit Game",
            font_size=font_size,
            color=Colors.WHITE,
            font_name="fonts/CANDARAB",
            size_hint=(None, None),
        )
        # Force the label to be centered at the desired ratios
        self.exit_label.texture_update()  # ensure texture_size is calculated
        self.exit_label.center_x = win_width * 0.945
        self.exit_label.center_y = win_height * 0.05











# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.floatlayout import FloatLayout
# from kivy.core.window import Window
# from A import A
# from classes.frontend.Scale import Scale
# from kivy.uix.image import Image
# from classes.globals.Colors import Colors
# from classes.globals.widgets.FocusImage import FocusImage
# from kivy.uix.label import Label
# from kivy.clock import Clock



# class TitleScreen(Widget):



#     login_text = "Checking for existing credentials..."
#     login_label = None

#     pending_text = "Pending login..."
#     pending_label = None

#     starting_text = "Starting game..."
#     starting_label = None

#     request_text = "Please login..."
#     request_label = None

#     login = None
#     start = None

#     data = None

#     scale = Scale()

#     title_bg = None

#     store_button = None

#     profile_container = None

#     profile_bg = None

#     title_profile = None

#     title_username = None

#     login_timer = None

#     plates = []

#     title_buttons = []

#     current_avatar = ""

#     starting_font = 18

#     login_button = None
#     account_button = None

#     flash_incr = 0
#     flash_label = None
#     flash_interval = None


#     def __init__(self, **kwargs):
#         super(TitleScreen, self).__init__(**kwargs)

#         self.title_bg = Image(pos=(0,0), width=A().root().current_size[0], height=A().root().current_size[1], source="", allow_stretch=True, keep_ratio=False)


#         x_coord = .515
#         y_coord = .76

#         self.title_container = FloatLayout(width=Scale().adjust_number(200), height=Scale().adjust_number(400), center_x=Scale().adjust_center_x(A().root().current_size[0]*x_coord), center_y=Scale().adjust_center_y(A().root().current_size[1]*(y_coord-(0 if A().root().login_required == True else .04)))) 

#         self.start_button = FocusImage(size=Scale().calculate_scale([150*1.05, 26*1.05]), pos_hint={"x": 0, "center_y": .37}, size_hint=(None, None), opacity=1, source="", textname="title_start", allow_stretch=True, keep_ratio=False)

#         y_coord -= .075

#         self.tutorial_button = FocusImage(size=Scale().calculate_scale([150*1.05, 26*1.05]), pos_hint={"x": 0, "center_y": .25}, size_hint=(None, None), opacity=1, source="", textname="title_tutorial", allow_stretch=True, keep_ratio=False)

#         y_coord -= .075
#         y_coord -= .075

#         self.whats_new_button = FocusImage(size=Scale().calculate_scale([150*1.05, 26*1.05]), pos_hint={"x": 0, "center_y": .13}, size_hint=(None, None), opacity=1, source="", textname="title_new", allow_stretch=True, keep_ratio=False)

#         self.exit_text()


#     def menu_buttons(self):
#         for widget in self.title_buttons:
#             self.title_container.remove_widget(widget)
        
#         self.remove_widget(self.title_container)
#         self.remove_widget(self.exit_label)

#         self.title_buttons = []

#         App.get_running_app().screens.set_skin()

#         self.title_buttons = [self.start_button, self.tutorial_button, self.whats_new_button] 
  
#         self.remove_widget(self.title_bg)
#         self.add_widget(self.title_bg)
#         for widget in self.title_buttons:
#             self.title_container.add_widget(widget)
#         self.add_widget(self.title_container)
#         self.add_widget(self.exit_label)

#         self.demo_text()


#     def demo_text(self, toggle=True):
#         self.remove_widget(self.flash_label)
#         self.flash_incr = 0
#         self.flash_label = Label(text="DEMO VERSION", font_size=Scale().adjust_number(18), color=Colors.DARK_RED, pos_hint={"x": 0, "center_y": 0.0375},) if not self.flash_label else self.flash_label
#         self.flash_interval.cancel() if self.flash_interval else None
#         self.flash_interval = Clock.schedule_interval(self.demo_flash, 1) if toggle == True else None
        

#     def demo_flash(self, dt):
#         self.flash_incr += 1
#         self.flash_label.text == "" if self.flash_incr % 2 == 0 else "DEMO VERSION"
#         self.title_container.remove_widget(self.flash_label) if self.flash_incr % 2 == 0 else self.title_container.add_widget(self.flash_label)


#     def exit_text(self):
#         self.exit_label = Label(text="[X] - Quit Game", font_size=Scale().adjust_number(12), color=Colors.WHITE, pos=(A().root().current_size[0] * .9, A().root().current_size[1] * .01), font_name="fonts/CANDARAB")
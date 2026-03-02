from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from A import A
from classes.frontend.Scale import Scale
from kivy.clock import Clock
from classes.globals.widgets.FocusImage import FocusImage
from kivy.uix.image import Image 
from kivy.uix.image import AsyncImage



class NewScreen(Widget):
    label_text = ["WHAT'S NEW SCREEN"]
    button_text = ["Return"]

    data = None
    container = None

    scale = Scale()

    new_bg = None
    return_button = None

    title_font = 15
    update_font = 13

    scroll_width = outer_box_width = 400
    scroll_height = 250
    box_width = outer_box_width - 10
    
    scroll_size = [scroll_width, scroll_height]

    return_size = [150, 26]


    def __init__(self, **kwargs):
        super(NewScreen, self).__init__(**kwargs)

        try:
            title_source = f"images/screens/{App.get_running_app().screens.current_skin}/skins/whatsnew.png"
            button_source = f"images/screens/{App.get_running_app().screens.current_skin}/buttons/return.png"
        except:
            title_source = f"images/screens/001/skins/whatsnew.png"
            button_source = f"images/screens/001/buttons/return.png"  
            
                    
        self.new_bg = Image(source="")
        
        self.add_widget(self.new_bg)

        self.return_button = FocusImage(source="", textname="new_return")


    def add_text(self):
        try:
            title_source = f"images/screens/{App.get_running_app().screens.current_skin}/skins/whatsnew.png"
            button_source = f"images/screens/{App.get_running_app().screens.current_skin}/buttons/return.png"
        except:
            title_source = f"images/screens/001/skins/whatsnew.png"
            button_source = f"images/screens/001/buttons/return.png"         

        try:
            self.new_bg = Image(source=A().root().resource_path(title_source), pos=(0,0), width=Window.width, height=Window.height, allow_stretch=True, keep_ratio=False)
        
            self.remove_widget(self.new_bg)
            self.add_widget(self.new_bg)

            x_coord = .4
            y_coord = .05

            self.return_button = FocusImage(size=Scale().calculate_scale(self.return_size), x=Scale().adjust_x(Window.width*x_coord), y=Scale().adjust_y(Window.height*y_coord), opacity=1, source=A().root().resource_path(f"images/screens/{App.get_running_app().screens.current_skin}/buttons/return.png"), allow_stretch=True, keep_ratio=False,  textname="new_return")
            self.remove_widget(self.return_button)
            self.add_widget(self.return_button)

            x_coord = .25
            y_coord = .5

            self.container = ScrollView(size_hint=(1, 1), width=Scale().adjust_number(self.scroll_size[0]), height=Scale().adjust_number(self.scroll_size[1]), center_x=Window.width * .5, center_y=Window.height*y_coord, do_scroll_y=True)

            outer_box = BoxLayout(width=Scale().adjust_number(self.outer_box_width), orientation='vertical', size_hint_y=None)
            outer_box.bind(minimum_height=outer_box.setter('height'))

            title = ""

            for news in App.get_running_app().main.new_obj.data:
                title = "" if len(title) < 1 else "\n\n\n\n"
                
                title = title + App.get_running_app().main.database.get_data(news["date"]) + ", " + App.get_running_app().main.database.get_data(news["time"]) +  " - " + App.get_running_app().main.database.get_data(news["headline"]) + "\n\n"

                image = AsyncImage(source=A().root().resource_path(App.get_running_app().main.database.get_data(news["image"])), size_hint_y=None, size=(100, 100))

                update = "\n\n" + App.get_running_app().main.database.get_data(news["text"])

                title_label = Label(text=str(title), width=700, height=150, text_size=(Scale().adjust_number(self.box_width), None), size_hint_y=None, font_size=Scale().adjust_number(self.title_font), valign="top", halign="left", font_name="fonts/CANDARAB")

                update_label = Label(text=str(update), width=700, height=150, text_size=(Scale().adjust_number(self.box_width), None), size_hint_y=None, font_size=Scale().adjust_number(self.update_font), valign="top", halign="left", font_name="fonts/CANDARAB")

                title_label.bind(texture_size=title_label.setter('size'))

                update_label.bind(texture_size=update_label.setter('size'))

                box = BoxLayout(width=self.box_width, orientation='vertical', size_hint_y=None)
                box.bind(minimum_height=box.setter('height'))
                box.add_widget(title_label)
                box.add_widget(image)
                box.add_widget(update_label)
                outer_box.add_widget(box)
                    
            self.container.add_widget(outer_box)

            Clock.schedule_once(lambda dt: self.scroll_top(self.container), 1) if self.container.scroll_y != 1 else None

            self.add_widget(self.container)  

        except Exception as e:
            print("\n\nError in NewScreen class, add_text - ", e)    


    def scroll_top(self, widget):
        widget.scroll_y = 1 if widget != None else None
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

from A import A


class Scale(Widget):
    base_width = 800
    base_height = 600
    objects = None
    



    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app_root = A().root()
        
        
        self.objects = {
            "Label": self.adjust_label,
            "Shape": self.adjust_shape,
            "FloatLayout": self.adjust_layout,
            "FocusLayout": self.adjust_layout,
            "Image": self.adjust_image,
            "FocusImage": self.adjust_image,
            "AsyncImage": self.adjust_image,
            "AchievementsScreen": self.adjust_screen,
            "InventoryScreen": self.adjust_screen,
            "TitleScreen": self.adjust_screen,
            "TutorialScreen": self.adjust_screen,
            "StatisticsScreen": self.adjust_screen,
            "StoreScreen": self.adjust_screen,
            "NewScreen": self.adjust_screen,
            "LeaderboardScreen": self.adjust_screen,
            "ProfileScreen": self.adjust_screen,
            "EndScreen": self.adjust_screen,
            "Display": self.adjust_screen,
            "Pause": self.adjust_blind,
            "FocusCheckbox": self.adjust_checkbox,
            "FocusTextInput": self.adjust_input,
            "FileScreen": None,
            "FileChooserListView": self.adjust_filescreen,
            "Player": None, 
            "Points": None,
            "ScrollView": None,
            "Timer": None,
            "Loading": None
        }

        self.current_width = 800
        self.current_height = 600


    def scale_hidden(self, hidden=False):
        pass

    def scale_widgets(self, hidden=False):
        try:
            self.app_main = A().main()
            for widget in self.app_main.children:
                self.app_main.remove_widget(widget)
                self.objects[str(widget.__class__.__name__)](widget) if self.objects[str(widget.__class__.__name__)] != None and str(widget.__class__.__name__) != "FocusTextInput" else self.objects[str(widget.__class__.__name__)](widget, True) if self.objects[str(widget.__class__.__name__)] != None and str(widget.__class__.__name__) == "FocusTextInput" else None 

                self.app_main.add_widget(widget)

            for widget in self.app_main.hidden_widgets["profile"]:
                self.app_main.remove_widget(widget)
                self.objects[str(widget.__class__.__name__)](widget) if self.objects[str(widget.__class__.__name__)] != None and str(widget.__class__.__name__) != "FocusTextInput" else self.objects[str(widget.__class__.__name__)](widget, True) if self.objects[str(widget.__class__.__name__)] != None and str(widget.__class__.__name__) == "FocusTextInput" else None 

                self.app_main.add_widget(widget)
                
            self.app_root.current_width = A().root().current_size[0]
            self.app_root.current_height = A().root().current_size[1] 

        except Exception as e:
            self.app_main.functions.get_error("Scale", "scale_widgets", e)


    def adjust_number(self, number):
        return int(number * (A().root().current_size[0]/self.base_width) * .85)
    

    def adjust_width(self, width):
        return width * (A().root().current_size[0]/self.app_root.current_width) 
    

    def adjust_height(self, height):
        return height * (A().root().current_size[1]/self.app_root.current_height)
    

    def adjust_x(self, x):
        return x * (A().root().current_size[0]/self.app_root.current_width)
    

    def adjust_y(self, y):
        return y * (A().root().current_size[1]/self.app_root.current_height)
    

    def adjust_pos(self, pos, current=None):
        if current:
            return (pos[0] * (A().root().current_size[0]/self.base_width), pos[1] * (A().root().current_size[1]/self.base_height))
        return (pos[0] * (A().root().current_size[0]/self.app_root.current_width), pos[1] * (A().root().current_size[1]/self.app_root.current_height))
    

    def adjust_center_x(self, center_x):
        return center_x * (A().root().current_size[0]/self.app_root.current_width)
    

    def adjust_center_y(self, center_y):
        return center_y * (A().root().current_size[1]/self.app_root.current_height)
    

    def adjust_font(self, font_size, current=None):
        return 14 * (A().root().current_size[1]/self.base_height) if font_size != 18 else 18 * (A().root().current_size[1]/self.base_height) 
    

    def adjust_size(self, size, current=None):
        if current:
            width = size[0] * (A().root().current_size[0]/self.current_width)
            height = size[1] * (A().root().current_size[1]/self.current_height)      
        else:
            width = size[0] * (A().root().current_size[0]/self.app_root.current_width)
            height = size[1] * (A().root().current_size[1]/self.app_root.current_height)
        return (width, height)
    

    def adjust_shape_size(self, size, current=None):
        if current:
            width = size[0] * (A().root().current_size[0]/self.base_width)
            height = size[1] * (A().root().current_size[1]/self.base_height)      
        else:
            width = size[0] * (A().root().current_size[0]/self.app_root.current_width)
            height = size[1] * (A().root().current_size[1]/self.app_root.current_height)
        return (width * .8, height * .8)
    

    def adjust_size_hint(self, hint):
        width = hint[0] * (A().root().current_size[0]/self.app_root.current_width)
        height = hint[1] * (A().root().current_size[1]/self.app_root.current_height)
        return (width, height)
    

    def adjust_text_size(self, widget):
        return (widget.width, None)
    

    def calculate_scale(self, base):
        return (base[0] * (A().root().current_size[0]/self.base_width), base[1] * (A().root().current_size[1]/self.base_height)) 
    

    def adjust_children(self, children):
        for child in children:
            if isinstance(child, Label):
                child.font_size = self.adjust_font(child.font_size) 
                child.text_size = self.adjust_text_size(child) 
                continue
            if isinstance(child, Image):
                self.adjust_image(child)
                continue

    
    def adjust_label(self, widget):
        widget.x = self.adjust_x(widget.x)
        widget.y = self.adjust_y(widget.y)
        widget.size = self.adjust_size(widget.size) if len(widget.text) > 1 else (50 * (A().root().current_size[0]/self.base_width), 50 * (A().root().current_size[1]/self.base_height)) 
        widget.font_size = self.adjust_font(widget.font_size)
        widget.text_size = self.adjust_text_size(widget) if widget.text_size[0] != None else widget.text_size


    def adjust_shape(self, widget):
        widget.x = self.adjust_x(widget.x)
        widget.y = self.adjust_y(widget.y)
        widget.size = self.adjust_size(widget.size)
        widget.sprite_label.font_size = self.adjust_font(widget.sprite_label.font_size)


    def adjust_image(self, widget):
        if widget.source != None: 
            if "skins" in widget.source:
                widget.pos = (0, 0)
                widget.size = self.adjust_size(widget.size)
            else:
                widget.pos = self.adjust_pos(widget.pos)
                widget.width = self.adjust_width(widget.width)
                widget.height = self.adjust_height(widget.height)
        

    def adjust_layout(self, widget):
        self.adjust_children(widget.children)
        widget.pos = self.adjust_pos(widget.pos)
        widget.width = self.adjust_width(widget.width)
        widget.height = self.adjust_height(widget.height)


    def adjust_screen(self, widget):
        for child in widget.children:
            self.objects[str(child.__class__.__name__)](child) if self.objects[str(child.__class__.__name__)] != None else None 


    def adjust_checkbox(self, widget):
        widget.size = self.adjust_size(widget.size)
        widget.layout.size = self.adjust_size(widget.size)
        widget.pos = self.adjust_pos(widget.pos)
        widget.layout.pos = self.adjust_pos(widget.pos)


    def adjust_blind(self, widget):
        widget.rect.size = Window.size


    def adjust_input(self, widget, current=None):
        if current:
            widget.pos = self.adjust_pos(widget.pos, True)
            widget.size = self.adjust_size(widget.size, True)
            widget.font_size = self.adjust_font(widget.font_size, True)
        widget.pos = self.adjust_pos(widget.pos)
        widget.size = self.adjust_size(widget.size)
        widget.font_size = self.adjust_font(widget.font_size)


    def reset_input(self, widget):
        widget.pos = [(self.base_width/A().root().current_size[0]) * widget.pos[0], (self.base_height/A().root().current_size[1]) * widget.pos[1]]
        widget.size = [(self.base_width/A().root().current_size[0]) * widget.size[0], (self.base_height/A().root().current_size[1]) * widget.size[1]]
        widget.font_size = 14


    def adjust_filescreen(self, widget):
        widget.size = self.adjust_size(widget.size)
        widget.pos = self.adjust_pos(widget.pos)
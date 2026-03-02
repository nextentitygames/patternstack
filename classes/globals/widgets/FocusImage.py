from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.window import Window
import webbrowser
from A import A 




class FocusImage(ButtonBehavior, AsyncImage):
    hand_cursor = False
    cursor_coords = None

    cursors = ["hand", "arrow"]

    return_text = "Return"

    text = None

    isclicked = False

    actions = None


    def __init__(self, textname, texttype=None, screen=None, **kwargs):
        self.textname = textname if textname else ""
        self.texttype = texttype if texttype else ""
        super().__init__(**kwargs)
        self.bind(on_press=self.on_click)
        Window.bind(mouse_pos=self.on_mouse_move)
        self.allow_stretch = True
        self.keep_ratio = False
        self.actions = {
            "purchase": self.purchase_handler,
            "profile_return": self.return_handler,
            "profile_achievements": self.achievements_handler,
            "profile_inventory": self.inventory_handler,
            "profile_back": self.profile_back_handler,
            "profile_confirm": self.profile_confirm_handler,
            "profile_upload": self.profile_upload_handler,
            "achievements_return": self.return_handler,
            "inventory_return": self.return_handler,
            "tutorial_return": self.return_handler,
            "statistics_return": self.return_handler,
            "new_return": self.return_handler,
            "store_return": self.return_handler,
            "title_login": self.login_handler,
            "title_store": self.store_handler,
            "title_profile": self.profile_handler,
            "title_start": self.start_handler,
            "title_tutorial": self.tutorial_handler,
            "title_statistics": self.statistics_handler,
            "title_inventory": self.inventory_handler,
            "title_new": self.whats_new_handler,
            "store_purchase": self.store_purchase_handler,
            "store_cancel": self.store_cancel_handler,
            "store_backgrounds": self.store_backgrounds_handler,
            "store_music": self.store_music_handler,
            "store_skins": self.store_skins_handler,
            "subscreen_return": self.subscreen_return_handler,
            "inventory_backgrounds": self.inventory_subscreen_handler,
            "inventory_music": self.inventory_subscreen_handler,
            "inventory_skins": self.inventory_subscreen_handler,
            "inventory_change": self.inventory_change_handler,
            "new_game": self.new_game_handler,
            "main_menu": self.main_menu_handler,
            "pause": self.pause_handler
        }



    def on_click(self, touch):
        if self.collide_point(*touch.pos) and not A().main().loading.event:
            self.process() 
        return True
    

    def on_mouse_move(self, window, pos):
        if self.collide_point(*pos) and not A().main().loading.event:
            Window.set_system_cursor(self.cursors[0])
            
        A().main().mouse_overs[self] = self.collide_point(*pos) 

        Window.set_system_cursor(self.cursors[1]) if len([i for i in list(A().main().mouse_overs.values()) if i == True]) < 1 else None
        
     
    
    def process(self):
        A().main().sounds["start"].toggle(True) if "start" in self.textname else A().main().sounds["pause"].toggle(True) if "pause" in self.textname and A().main().paused == False else A().main().sounds["menu_back"].toggle(True) if "return" in self.textname else A().main().sounds["menu_select"].toggle(True) 
        self.actions[self.textname]()
        self.cursor_handler(False)


    def check_mouse(self, login=False):
        app = App.get_running_app()
        main = app.main
        x, y = Window.mouse_pos

        # Helper: bounding-box hit test
        def hits(obj):
            return obj.x <= x <= obj.x + obj.width and obj.y <= y <= obj.y + obj.height

        # Block interaction if loading
        if A().main().loading.event:
            self.cursor_handler(False)
            return False

        # -----------------------
        # LOGIN SCREEN MODE
        # -----------------------
        if login:
            title = main.title_obj

            buttons = [
                title.login_button,
                title.account_button
            ]

            for btn in buttons:
                if hits(btn):
                    self.cursor_handler(True)
                    return True

            self.cursor_handler(False)
            return False

        # -----------------------
        # NORMAL GAME MODE
        # -----------------------
        user_data = main.user_data
        if not user_data:
            self.cursor_handler(False)
            return False

        a = A().main()

        for item in main.children:
            for obj in item.children:
                try:
                    focus_image = "FocusImage" in str(obj) and obj.parent in main.children
                    shape_obj = (
                        "Shape" in str(item)
                        and item not in a.target_list
                        and item.sprite_label.text.split("_")[0] in a.shapes
                        and not a.paused
                    )
                    bonus_obj = (
                        a.stop_on
                        and "Shape" in str(item)
                        and item not in a.target_list
                        and item.sprite_label.text.split("_")[0] in a.bonus_sprites
                    )

                    if focus_image or shape_obj or bonus_obj:
                        if hits(obj):
                            self.cursor_handler(True)
                            return True

                except Exception as e:
                    print("Mouse check error:", e)
                    continue

        self.cursor_handler(False)
        return False


    
    def cursor_handler(self, condition):
        if condition:
            Window.set_system_cursor(self.cursors[0])
        else:
            Window.set_system_cursor(self.cursors[1])


    def purchase_handler(self):
        if not isinstance(self.texttype, list):
            cost = str(App.get_running_app().main.database.get_data(App.get_running_app().main.store_obj.store_text[self.texttype]))
        else:
            cost = str(App.get_running_app().main.database.get_data(App.get_running_app().main.store_obj.store_stock[self.texttype[0]][self.texttype[1]])) 

        if "$" not in cost:            
            App.get_running_app().main.store_obj.purchase_item = self.texttype[1] if isinstance(self.texttype, list) else self.texttype
            App.get_running_app().main.store_obj.purchase_cost = cost
            App.get_running_app().main.store_obj.popup_handler(True)
        else:
            print("\n\nreal money transaction") 


    def login_handler(self):
        App.get_running_app().main.title_obj.login_pending()
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe" 
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get("chrome").open("http://127.0.0.1:5000/")      


    def achievements_handler(self):
        if App.get_running_app().main != None:
            App.get_running_app().main.achievements_obj.reset_screen()
            App.get_running_app().main.screen_handler("achievements")
            self.clear_profile()


    def inventory_handler(self):
        if App.get_running_app().main != None:
            App.get_running_app().main.inventory_obj.reset_screen()
            App.get_running_app().main.screen_handler("inventory")
            self.clear_profile()


    def return_handler(self):
        if self.textname == "achievements_return" or self.textname == "inventory_return":
            App.get_running_app().main.screen_handler("profile")          
        else:
            App.get_running_app().main.screen_handler("title")
            App.get_running_app().main.title_obj.menu_buttons()

        self.clear_profile()


    def clear_profile(self):
        if self.textname == "profile_return":
            App.get_running_app().main.profile_obj.screen_reset()


    def new_return_handler(self):
        App.get_running_app().main.new_obj.remove_widget(App.get_running_app().main.new_obj.container) 
        App.get_running_app().main.new_obj.container = None
        App.get_running_app().main.screen_handler("title")


    def start_handler(self):
        try:
            if App.get_running_app().main != None:
                App.get_running_app().main.screen_handler("", True)
                App.get_running_app().main.start_load()
                App.get_running_app().main.scale.set_widgets(App.get_running_app().main.children)
        except:
            pass


    def tutorial_handler(self):
        try:
            if App.get_running_app().main.tutorial_obj != None:

                App.get_running_app().main.remove_widget(App.get_running_app().main.loading)
                App.get_running_app().main.add_widget(App.get_running_app().main.loading)
                App.get_running_app().main.loading.start("tutorial")
        except:
            pass


    def statistics_handler(self):
        try:
            if App.get_running_app().main.statistics_obj != None:
                App.get_running_app().main.statistics_obj.reset_screen()
                App.get_running_app().main.screen_handler("statistics")
        except:
            pass

    
    def whats_new_handler(self):
        try:
            if App.get_running_app().main.new_obj != None:
                App.get_running_app().main.new_obj.add_text()
               
                App.get_running_app().main.remove_widget(App.get_running_app().main.loading)
                App.get_running_app().main.add_widget(App.get_running_app().main.loading)
                App.get_running_app().main.loading.start("whats_new")
        except:
            pass


    def store_handler(self):
        try:
            if App.get_running_app().main.store_obj != None:
                App.get_running_app().main.store_obj.reset_screen()
                App.get_running_app().main.screen_handler("store")
        except:
            pass


    def profile_handler(self):
        if App.get_running_app().main != None:
            App.get_running_app().main.screen_handler("profile")
            App.get_running_app().main.profile_obj.set_text(App.get_running_app().main.user_data)


    def profile_back_handler(self):
        try:
            if App.get_running_app().main.profile_obj != None:
                App.get_running_app().main.profile_obj.upload_widget(False)
                App.get_running_app().main.profile_obj.avatar_checkbox.active = False
                App.get_running_app().main.profile_obj.edit_avatar.text = ""
                App.get_running_app().main.profile_obj.remove_widget(App.get_running_app().main.profile_obj.edit_avatar)
                App.get_running_app().main.profile_obj.screen_reset()
        except:
            pass


    def profile_confirm_handler(self):
        try:
            if App.get_running_app().main != None:
                App.get_running_app().main.profile_obj.update_profile()
        except:
            pass


    def profile_upload_handler(self):
        try:
            if App.get_running_app().main != None:
                App.get_running_app().main.profile_obj.process_upload()
        except:
            pass


    def store_purchase_handler(self):
        App.get_running_app().main.store_obj.purchase_confirm(True)


    def store_cancel_handler(self):
        App.get_running_app().main.store_obj.popup_handler(False)


    def store_backgrounds_handler(self):
        App.get_running_app().main.store_obj.subscreen_handler(True, "backgrounds")


    def store_music_handler(self):
        App.get_running_app().main.store_obj.subscreen_handler(True, "music")


    def store_skins_handler(self):
        App.get_running_app().main.store_obj.subscreen_handler(True, "skins")


    def subscreen_return_handler(self):
        if self.texttype == "store":
            App.get_running_app().main.store_obj.subscreen_handler(False)

        if self.texttype == "inventory":
            App.get_running_app().main.inventory_obj.subscreen_handler(False)


    def inventory_subscreen_handler(self):
        App.get_running_app().main.inventory_obj.subscreen_handler(True, self.textname)


    def inventory_change_handler(self):
        App.get_running_app().main.inventory_obj.change_item(self.texttype)


    def new_game_handler(self):
        A().root().new_game()


    def main_menu_handler(self):
        A().main().end_obj.flash_timer.cancel()
        A().main().main_menu()
        

    def pause_handler(self):
        A().main().pause_logic()
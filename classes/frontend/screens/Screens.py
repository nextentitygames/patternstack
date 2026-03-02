from kivy.app import App
from kivy.uix.widget import Widget
from A import A




class Screens(Widget):
    achievements_skin = "images/screens/001/achievements.png"
    game_over_skin = "images/screens/001/game_over.png"
    inventory_skin = "images/screens/001/inventory.png"
    profile_skin = "images/screens/001/profile.png"
    statistics_skin = "images/screens/001/statistics.png"
    store_skin = "images/screens/001/store.png"
    title_skin = "images/screens/001/title.png"
    tutorial_skin = "images/screens/001/tutorial.png"
    whatsnew_skin = "images/screens/001/whatsnew.png"

    skins = None


    achievements_button = "images/screens/001/buttons/achievements.png"
    cancel_button = "images/screens/001/buttons/cancel.png"
    confirm_button = "images/screens/001/buttons/confirm.png"
    inventory_button = "images/screens/001/buttons/inventory.png"
    login_button = "images/screens/001/buttons/login.png"
    account_button = "images/screens/001/buttons/no_account.png"
    purchase_button = "images/screens/001/buttons/purchase.png"
    return_button = "images/screens/001/buttons/return.png"
    start_button = "images/screens/001/buttons/start.png"
    statistics_button = "images/screens/001/buttons/statistics.png"
    tutorial_button = "images/screens/001/buttons/tutorial.png"
    upload_button = "images/screens/001/buttons/upload.png"
    whats_new_button = "images/screens/001/buttons/whats_new.png"
    store_button = "images/screens/001/buttons/store.png"

    buttons = None

    current_plate = "images/screens/001/plates/plate.png"
    achievements_plate = "images/screens/001/plates/plate.png"
    inventory_plate = "images/screens/001/plates/plate.png"
    statistics_plate = "images/screens/001/plates/plate.png"
    store_plate = "images/screens/001/plate.png"
    profile_bg = "images/screens/001/plates/profile_bg.png"

    plates = None    

    current_skin = "001"




    def __init__(self, **kwargs):
        self.skins = {
            "game_over": [
                self.game_over_skin,
                App.get_running_app().main.end_obj.end_bg
            ],
            "title": [
                self.title_skin,
                App.get_running_app().main.title_obj.title_bg
            ],
            "tutorial": [
                self.tutorial_skin,
                App.get_running_app().main.tutorial_obj.tutorial_bg
            ],
            "whatsnew": [
                self.whatsnew_skin,
                App.get_running_app().main.new_obj.new_bg
            ]
        }


        self.buttons = {
            "login": [
                self.login_button,
                App.get_running_app().main.title_obj.login_button
            ],
            "return": [
                self.return_button,
                [
                    App.get_running_app().main.new_obj.return_button,
                    App.get_running_app().main.tutorial_obj.return_button,
                ]
            ],
            "start": [
                self.start_button,
                App.get_running_app().main.title_obj.start_button
            ],
            "tutorial": [
                self.tutorial_button,
                App.get_running_app().main.title_obj.tutorial_button
            ],
            "whats_new": [
                self.whats_new_button,
                App.get_running_app().main.title_obj.whats_new_button
            ],
        } 


        self.plates = {
        }
       

    def set_skin(self):
        try:
            current = A().root().current_skin

            try:
                current = current.split("_")[1]
            except:
                pass

        except: 
            current = "001"
            
        self.current_skin = str(current)

        for skin in self.skins.keys():
            self.skins[skin][0] = "images/screens/" + str(current) + "/skins/" + str(skin) + ".png"
            if self.skins[skin][1].source != self.skins[skin][0]:
                self.skins[skin][1].source = self.skins[skin][0]
                self.skins[skin][1].reload()

        self.set_buttons(current)
        self.set_plates(current)


    def set_buttons(self, current):
        for button in self.buttons.keys():
            self.buttons[button][0] = "images/screens/" + str(current) + "/buttons/" + str(button) + ".png"

            if not isinstance(self.buttons[button][1], list):
                if self.buttons[button][1] != None:
                    self.buttons[button][1].source = self.buttons[button][0]  
                    self.buttons[button][1].reload()
            else:
                for obj in self.buttons[button][1]:
                    if obj.source != self.buttons[button][0]:
                        obj.source = self.buttons[button][0]
                        obj.reload()


    def set_plates(self, current):
        for plate in self.plates.keys():
            self.plates[plate][0] = "images/screens/" + str(current) + "/plates/plate.png" 

            self.current_plate = self.plates[plate][0]

            if len(self.plates[plate][1].plates) > 0:
                for obj in self.plates[plate][1].plates:
                    if obj.source != self.plates[plate][0]:
                        obj.source = self.plates[plate][0]
                        obj.reload()
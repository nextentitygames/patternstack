from kivy.app import App
from kivy.uix.widget import Widget
import traceback
from kivy.core.window import Window

class Functions(Widget):
    cursors = ["hand", "arrow"]
    home = None
    base_width = 800
    base_height = 457




    def __init__(self, **kwargs):
        super(Functions).__init__(**kwargs)


    def get_error(self, file, function, e):
        print(f"\n\nerror in {file} class, {function} function: {e}")
        tb = traceback.extract_tb(e.__traceback__)[-1]
        print(f"Exception: {e}")
        print(f"Line number: {tb.lineno}")

        with open(tb.filename, 'r') as f:
            lines = f.readlines()
            error_line = lines[tb.lineno - 1] 

        column_number = error_line.find('/') + 1  
        print(f"Column number: {column_number}")


    def cursor_handler(self, condition):
        if condition:
            Window.set_system_cursor(self.cursors[0])
        else:
            Window.set_system_cursor(self.cursors[1])


    def modify_text(self, key):
        text = str(App.get_running_app().main.database.get_data(key)).split("_") 
        return (' '.join(word.capitalize() for word in text))
    

    def collection_list(self, column):
        return App.get_running_app().main.database.get_data(App.get_running_app().main.inventory_data[column]).split(",")


    def get_collections(self, column, item):
        return item in self.collection_list(column)
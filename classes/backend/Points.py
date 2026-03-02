from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from A import A
from classes.frontend.Scale import Scale
import math as Math

from classes.globals.Colors import Colors




class Points(Widget):
    bonus_letters = ["Q", "X", "Z"]
    point_display = None
    score = 0
    display_length = 6
    display = "Score: 000000"
    base_stack = 50
    stack_points = base_stack
    variable_points = 25
    multiplier = 1
    time_multiplier = 50
    base_round = 300
    base_win = 1000
    base_loss = 1000
    base_solved = 100
    win_bonus = 1000
    lose_bonus = -500
    display_pos = (Window.width*.78, Window.height*.905)
    scale = Scale()
    found_points = []
    bonus_time = 70
    last_time = 0

    length_default = 1 
    starting_length = 3 
    length_multiplier = .25 

    hours_divisor = 3600
    minutes_divisor = 60
    minute_time = 60
    gold_points = 250
    

    def __init__(self, **kwargs):
        super(Points, self).__init__(**kwargs)





    def add(self, amount):
        self.score += round(amount)
        self.set_display()


    def subtract(self, amount):
        self.score -= round(amount)
        self.set_display()


    def bonus(self, word):
        bonus = 1
        for letter in word:
            if letter in self.bonus_letters:
                bonus += 1
                print("\n\nX" + str(bonus) + " BONUS FOR LETTER: " + letter)
        return bonus
    

    def powerup(self, type):
        self.set_multiplier(self.get_round())
        self.add(type * self.variable_points)


    def hazard(self, type):
        self.set_multiplier(self.get_round())
        self.subtract(type * self.variable_points)


    def add_to_stack(self, added):
        self.set_multiplier(self.get_round())
        self.add(added * self.stack_points)


    def remove_from_stack(self, removed):
        self.set_multiplier(self.get_round())
        self.subtract(removed * self.stack_points)


    def new_solved(self, stack):
        total = round(self.time_bonus() + self.length_bonus(stack) + self.base_points())  
        self.add(total)
        return total
    

    def length_bonus(self, stack):
        return self.length_default + (len(stack) - self.starting_length * self.length_multiplier)
    

    def base_points(self):
        return self.base_solved * (A().main().current_round)
    

    def new_round(self):
        pass


    def get_round(self):
        return A().main().round 
    
    
    def get_minutes(self):
        return A().main().timer.minutes
    
    
    def time_bonus(self):
        bonus = 0
        current_time = A().main().timer.timer
        time = 100 + (A().main().current_round*10) if A().main().current_round > 1 else 100
        bonus = time - (current_time-self.last_time) 
        bonus = 0 if bonus < 0 else bonus
        self.last_time = current_time
        return bonus


    def set_multiplier(self, round):
        self.multiplier = round
        self.stack_add = self.base_stack * self.multiplier


    def change_color(self, condition=None):
        A().main().display.point_display.color = Colors.DARK_RED if self.score < 0 else A().main().base_font_color


    def get_found_time(self):
        time = A().main().timer.timer - self.last_time
        time_string = ""

        hours = Math.floor(time / self.hours_divisor)
        minutes = Math.floor(time / self.minutes_divisor) % self.minute_time 
        seconds = time % self.minute_time

        if(hours >= 1):
            hours_display = str(hours) + " hr, "
        else:
            hours_display = None

        if(minutes >= 1):
            minutes_display = str(minutes) + " min, "
        else:
            minutes_display = None 

        seconds_display = str(seconds) + " sec"

        time_string += hours_display if hours_display else ""
        time_string += minutes_display if minutes_display else "" 
        time_string += seconds_display if seconds_display else ""  
         
        return time_string


    def set_display(self):
        display = ""
        self.change_color()
        if self.score < 0:
             display = "-" 
             self.change_color(False)
        if self.score > 0:
            self.change_color(True)
        zeros = self.display_length - len(str(self.score)) + len(display)
        i = 0

        while i < zeros:
            display = display + "0"
            i+=1

        self.display = "Score: " +  display + str(abs(self.score))

        A().main().display.point_display.text = self.display


    def win_game(self):
        self.add(self.base_win + self.end_score(True))


    def lose_game(self):
        self.subtract(self.base_loss + self.end_score(False))


    def end_score(self, outcome):
        if outcome:
            return round(self.time_multiplier * ((60/self.get_minutes())*2) if self.get_minutes > 0 else self.win_bonus if self.get_minutes() < 30 else 1)
        return round(self.time_multiplier * (((60 - self.get_minutes())/10) if self.get_minutes() < 30 else self.lose_bonus))
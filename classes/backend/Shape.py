import random
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)
from kivy.vector import Vector
from kivy.core.window import Window
from random import randint
import math as Math
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior

from A import A



class Shape(ButtonBehavior, Widget):
    base_width = 800
    base_height = 457
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    sprite_label = ObjectProperty(None)
    blind = ObjectProperty(None)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    getcolor = ListProperty([0, 0, 0, 1])
    current_sprites = []
    sprite_length = 8.0
    dt = .03
    mine_rules = 15
    freeze_rules = 15
    cursors = ["hand", "arrow"]

    shapes = ["circles", "squares", "stars", "moons", "hexagons",  "trapezoids", "arrows_right", "arrows_left", "arrows_up", "arrows_down", "arrows2_left", "triangles"]

    rare_shapes = ["hearts"]

    current_shapes = []




    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_press=self.on_click)
        Window.bind(mouse_pos=self.on_mouse_move)
        Window.bind(on_mouse_up=self.on_mouse_up)
        self.set_sprites()


    def on_click(self, touch):
        if self.collide_point(*touch.pos):
            A().main().last_touch = self.x if self == A().main().symbols[0] and self.opacity == 1 else None 
        return True
    

    def on_mouse_move(self, window, pos):
        if A().main().last_touch and A().main().in_bounds(pos):
            for widget in A().main().symbols:
                if not A().main().freeze_mine and not A().main().bomb_mine:
                    widget.x = pos[0] 


        # if self.collide_point(*pos) and not A().main().loading.event:
        #     Window.set_system_cursor(self.cursors[0])
            
        # A().main().mouse_overs[self] = self.collide_point(*pos) 

        # Window.set_system_cursor(self.cursors[1]) if len([i for i in list(A().main().mouse_overs.values()) if i == True]) < 1 else None



    def on_mouse_up(self, window, x, y, button, modifiers):
        A().main().last_touch = None
        

    def on_texture(self, instance, value):
        if self.sprite._coreimage is None:
            print("Failed to load image:", self.source)


    def set_sprites(self):
        self.current_shapes = []
        while len(self.current_shapes) < 5:
            try:
                self.current_shapes.append("images/shapes/" + str(self.shapes[random.randint(0, len(self.shapes)-1)]) + "_00" + str(random.randint(1, 4)) + ".png")
            except:
                pass
        

    def set_letter_list(self, letter_list):
        self.letter_list = letter_list


    def move(self, dt):
        try:
            vx, vy = self.velocity
            new_pos = Vector(vx * dt, vy * dt) + Vector(*self.pos)
            self.pos = (float(new_pos.x), float(new_pos.y))
        except:
            pass


    def stop(self):
        self.pos = (-500, 5000)


    def area_random(self, ball_num):
        max_ceiling = ball_num * Math.ceil((100/8))
        true_ceiling = max_ceiling - 8
        floor = max_ceiling - Math.ceil((100/8)) 
        area = randint(floor, true_ceiling) * .01
        return area


    def get_color(self):
        color = (randint(0, 1), randint(0, 1), randint(0, 1), 1)
        while(color == (0, 0, 0, 1) or color == (1, 1, 0, 1)):
            color = (randint(0, 1), randint(0, 1), randint(0, 1), 1)
        return color
    

    def get_selection(self, letter):
        eraser = "eraser"
        gold = "gold"
        strike = "strikes"
        stop = "stop"
        bomb = "bomb"
        freeze = "freeze"

        random = randint(0, 100)
        frequency = self.frequency_check()

        if random < frequency:
            return letter
        elif random >= frequency and random < frequency + self.mine_rules:
            return bomb
        elif random >= frequency + self.mine_rules and random < frequency + self.mine_rules + self.freeze_rules:
            return freeze
        elif random >= frequency + self.mine_rules + self.freeze_rules and random < 97:
            return gold
        elif random < 98:
            return eraser
        elif random >= 98 and random < 99:
            return strike
        else:
            return stop
        

    def frequency_check(self):
        return 95 - (self.mine_rules + self.freeze_rules) 


    def get_text(self, round):
        try:
            return self.get_selection(self.current_shapes[random.randint(0, len(self.current_shapes)-1)])
        except:
            pass


    def get_sprite(self, start=False):
        return ""
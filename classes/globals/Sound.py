import time
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from A import A
from random import randint


class Sound:

    sounds = {
        "music": {
            "underground-cavern-metaruka": "sounds/music/002.wav",
            "stage-1-juhani-junkala": "sounds/music/003.wav",
            "stage-2-juhani-junkala": "sounds/music/004.wav",
            "boss-fight-juhani-junkala": "sounds/music/005.wav",
            "level-1-juhani-junkala": "sounds/music/006.wav",
            "title-screen-juhani-junkala": "sounds/music/007.wav",
            "356-8-bit-chiptune-game-music-357518.wav": "sounds/music/356-8-bit-chiptune-game-music-357518.wav",
            "8-bit-retro-game-music-233964.wav": "sounds/music/8-bit-retro-game-music-233964.wav",
            "8bit-theme-loop-chiptune-symphony-387749.wav": "sounds/music/8bit-theme-loop-chiptune-symphony-387749.wav",
            "bit-bit-loop-113810.wav": "sounds/music/bit-bit-loop-113810.wav",
            "byte-blast-8-bit-arcade-music-background-music-for-video-208780.wav": "sounds/music/byte-blast-8-bit-arcade-music-background-music-for-video-208780.wav",
            "chiptune-symphony-8bit-game-theme-music-381366.wav": "sounds/music/chiptune-symphony-8bit-game-theme-music-381366.wav",
            "epic-chiptune-end-credits-music-235893.wav": "sounds/music/epic-chiptune-end-credits-music-235893.wav",
            "exploration-chiptune-rpg-adventure-theme-336428.wav": "sounds/music/exploration-chiptune-rpg-adventure-theme-336428.wav",
            "game-gaming-background-music-385611.wav": "sounds/music/game-gaming-background-music-385611.wav",
            "game-background-themes-5811.wav": "sounds/music/game-background-themes-5811.wav",
            "game-music-7408.wav": "sounds/music/game-music-7408.wav",
            "game-music-teste-1-204326.wav": "sounds/music/game-music-teste-1-204326.wav",
            "game-music-teste-204327.wav": "sounds/music/game-music-teste-204327.wav",
            "puzzle-game-loop-bright-casual-video-game-music-249201.wav": "sounds/music/puzzle-game-loop-bright-casual-video-game-music-249201.wav",
            "retro-arcade-game-music-297305.wav": "sounds/music/retro-arcade-game-music-297305.wav",
            "retro-arcade-game-music-396890.wav": "sounds/music/retro-arcade-game-music-396890.wav",
            "save-as-115826.wav": "sounds/music/save-as-115826.wav",
            "spaceship-arcade-shooter-game-background-soundtrack-318508.wav": "sounds/music/spaceship-arcade-shooter-game-background-soundtrack-318508.wav",
            "win-in-the-video-game-191820.wav": "sounds/music/win-in-the-video-game-191820.wav",
        },
        "effects": {
            "block": "sounds/effects/block.wav",
            "coin": "sounds/effects/coin.wav",
            "collect": "sounds/effects/collect.wav",
            "erase": "sounds/effects/erase.wav",
            "explode": "sounds/effects/explode.wav",
            "found": "sounds/effects/found.wav",
            "freeze": "sounds/effects/freeze.wav",
            "frozen": "sounds/effects/frozen.wav",
            "grab": "sounds/effects/grab.wav",
            "invalid": "sounds/effects/invalid.wav",
            "menu_back": "sounds/effects/menu_back.wav",
            "menu_select": "sounds/effects/menu_select.wav",
            "pause": "sounds/effects/pause.wav",
            "round": "sounds/effects/round.wav",
            "stack": "sounds/effects/stack.wav",
            "start": "sounds/effects/start.wav",
            "stop": "sounds/effects/stop.wav",
            "win": "sounds/effects/win.wav",
            "wrong": "sounds/effects/wrong.wav"
        }
    }

    # sounds = {
    #     "music": {
    #         "underground-cavern-metaruka": "sounds_ogg/music/002.ogg",
    #         "stage-1-juhani-junkala": "sounds_ogg/music/003.ogg",
    #         "stage-2-juhani-junkala": "sounds_ogg/music/004.ogg",
    #         "boss-fight-juhani-junkala": "sounds_ogg/music/005.ogg",
    #         "level-1-juhani-junkala": "sounds_ogg/music/006.ogg",
    #         "title-screen-juhani-junkala": "sounds_ogg/music/007.ogg",
    #         "356-8-bit-chiptune-game-music-357518.ogg": "sounds_ogg/music/356-8-bit-chiptune-game-music-357518.ogg",
    #         "8-bit-retro-game-music-233964.ogg": "sounds_ogg/music/8-bit-retro-game-music-233964.ogg",
    #         "8bit-theme-loop-chiptune-symphony-387749.ogg": "sounds_ogg/music/8bit-theme-loop-chiptune-symphony-387749.ogg",
    #         "bit-bit-loop-113810.ogg": "sounds_ogg/music/bit-bit-loop-113810.ogg",
    #         "byte-blast-8-bit-arcade-music-background-music-for-video-208780.ogg": "sounds_ogg/music/byte-blast-8-bit-arcade-music-background-music-for-video-208780.ogg",
    #         "chiptune-symphony-8bit-game-theme-music-381366.ogg": "sounds_ogg/music/chiptune-symphony-8bit-game-theme-music-381366.ogg",
    #         "epic-chiptune-end-credits-music-235893.ogg": "sounds_ogg/music/epic-chiptune-end-credits-music-235893.ogg",
    #         "exploration-chiptune-rpg-adventure-theme-336428.ogg": "sounds_ogg/music/exploration-chiptune-rpg-adventure-theme-336428.ogg",
    #         "game-gaming-background-music-385611.ogg": "sounds_ogg/music/game-gaming-background-music-385611.ogg",
    #         "game-background-themes-5811.ogg": "sounds_ogg/music/game-background-themes-5811.ogg",
    #         "game-music-7408.ogg": "sounds_ogg/music/game-music-7408.ogg",
    #         "game-music-teste-1-204326.ogg": "sounds_ogg/music/game-music-teste-1-204326.ogg",
    #         "game-music-teste-204327.ogg": "sounds_ogg/music/game-music-teste-204327.ogg",
    #         "puzzle-game-loop-bright-casual-video-game-music-249201.ogg": "sounds_ogg/music/puzzle-game-loop-bright-casual-video-game-music-249201.ogg",
    #         "retro-arcade-game-music-297305.ogg": "sounds_ogg/music/retro-arcade-game-music-297305.ogg",
    #         "retro-arcade-game-music-396890.ogg": "sounds_ogg/music/retro-arcade-game-music-396890.ogg",
    #         "save-as-115826.ogg": "sounds_ogg/music/save-as-115826.ogg",
    #         "spaceship-arcade-shooter-game-background-soundtrack-318508.ogg": "sounds_ogg/music/spaceship-arcade-shooter-game-background-soundtrack-318508.ogg",
    #         "win-in-the-video-game-191820.ogg": "sounds_ogg/music/win-in-the-video-game-191820.ogg",
    #     },
    #     "effects": {
    #         "block": "sounds_ogg/effects/block.ogg",
    #         "coin": "sounds_ogg/effects/coin.ogg",
    #         "collect": "sounds_ogg/effects/collect.ogg",
    #         "erase": "sounds_ogg/effects/erase.ogg",
    #         "explode": "sounds_ogg/effects/explode.ogg",
    #         "found": "sounds_ogg/effects/found.ogg",
    #         "freeze": "sounds_ogg/effects/freeze.ogg",
    #         "frozen": "sounds_ogg/effects/frozen.ogg",
    #         "grab": "sounds_ogg/effects/grab.ogg",
    #         "invalid": "sounds_ogg/effects/invalid.ogg",
    #         "menu_back": "sounds_ogg/effects/menu_back.ogg",
    #         "menu_select": "sounds_ogg/effects/menu_select.ogg",
    #         "pause": "sounds_ogg/effects/pause.ogg",
    #         "round": "sounds_ogg/effects/round.ogg",
    #         "stack": "sounds_ogg/effects/stack.ogg",
    #         "start": "sounds_ogg/effects/start.ogg",
    #         "stop": "sounds_ogg/effects/stop.ogg",
    #         "win": "sounds_ogg/effects/win.ogg",
    #         "wrong": "sounds_ogg/effects/wrong.ogg"
    #     }
    # }

    pause_pos = 0
    sound = None


     

    def __init__(self, soundtype, soundname, **kwargs):
        self.soundtype = soundtype if soundtype in self.sounds.keys() else ""
        self.soundname = soundname if soundname in self.sounds["music"].keys() or soundname in self.sounds["effects"].keys() else ""
        super().__init__(**kwargs)
        self.app_root = A().root()
        self.app_main = A().main()

        self.set_sound(soundtype, soundname) if soundtype == "effects" else None
        
        




    def toggle(self, condition, loop=None):
        try:
            if condition == True and self.sound:
                self.sound.play()
                self.sound.loop = True if loop else False
            else:
                if self.sound:
                    self.sound.stop()  
                    self.sound.loop = False
                
                self.pause_pos = 0
            
        except Exception as e:
            print("Error in 'toggle' function, 'Sound' class:\n\n")
            print(e)
            
        
    def pause(self):
        self.pause_pos = self.sound.get_pos()
        self.sound.stop()


    def resume(self):
        if self.pause_pos:
            self.sound.seek(self.pause_pos) 
        self.sound.play()

    
    def set_sound(self, soundtype, soundname):
        self.soundtype = soundtype
        self.soundname = soundname
        self.load_sound()

    #split into music and effects after debug
    def load_music(self):

        self.sounds = {
            "music": {
                "underground-cavern-metaruka": SoundLoader.load("sounds/music/002.wav"),
                "stage-1-juhani-junkala": SoundLoader.load("sounds/music/003.wav"),
                "stage-2-juhani-junkala": SoundLoader.load("sounds/music/004.wav"),
                "boss-fight-juhani-junkala": SoundLoader.load("sounds/music/005.wav"),
                "level-1-juhani-junkala": SoundLoader.load("sounds/music/006.wav"),
                "title-screen-juhani-junkala": SoundLoader.load("sounds/music/007.wav"),
                "356-8-bit-chiptune-game-music-357518.wav": SoundLoader.load("sounds/music/356-8-bit-chiptune-game-music-357518.wav"),
                "8-bit-retro-game-music-233964.wav": SoundLoader.load("sounds/music/8-bit-retro-game-music-233964.wav"),
                "8bit-theme-loop-chiptune-symphony-387749.wav": SoundLoader.load("sounds/music/8bit-theme-loop-chiptune-symphony-387749.wav"),
                "bit-bit-loop-113810.wav": SoundLoader.load("sounds/music/bit-bit-loop-113810.wav"),
                "byte-blast-8-bit-arcade-music-background-music-for-video-208780.wav": SoundLoader.load("sounds/music/byte-blast-8-bit-arcade-music-background-music-for-video-208780.wav"),
                "chiptune-symphony-8bit-game-theme-music-381366.wav": SoundLoader.load("sounds/music/chiptune-symphony-8bit-game-theme-music-381366.wav"),
                "epic-chiptune-end-credits-music-235893.wav": SoundLoader.load("sounds/music/epic-chiptune-end-credits-music-235893.wav"),
                "exploration-chiptune-rpg-adventure-theme-336428.wav": SoundLoader.load("sounds/music/exploration-chiptune-rpg-adventure-theme-336428.wav"),
                "game-gaming-background-music-385611.wav": SoundLoader.load("sounds/music/game-gaming-background-music-385611.wav"),
                "game-background-themes-5811.wav": SoundLoader.load("sounds/music/game-background-themes-5811.wav"),
                "game-music-7408.wav": SoundLoader.load("sounds/music/game-music-7408.wav"),
                "game-music-teste-1-204326.wav": SoundLoader.load("sounds/music/game-music-teste-1-204326.wav"),
                "game-music-teste-204327.wav": SoundLoader.load("sounds/music/game-music-teste-204327.wav"),
                "puzzle-game-loop-bright-casual-video-game-music-249201.wav": SoundLoader.load("sounds/music/puzzle-game-loop-bright-casual-video-game-music-249201.wav"),
                "retro-arcade-game-music-297305.wav": SoundLoader.load("sounds/music/retro-arcade-game-music-297305.wav"),
                "retro-arcade-game-music-396890.wav": SoundLoader.load("sounds/music/retro-arcade-game-music-396890.wav"),
                "save-as-115826.wav": SoundLoader.load("sounds/music/save-as-115826.wav"),
                "spaceship-arcade-shooter-game-background-soundtrack-318508.wav": SoundLoader.load("sounds/music/spaceship-arcade-shooter-game-background-soundtrack-318508.wav"),
                "win-in-the-video-game-191820.wav": SoundLoader.load("sounds/music/win-in-the-video-game-191820.wav"),
            }
        }


    def load_sound(self):
        try:
            # self.sound = SoundLoader.load(self.sounds[self.soundtype][self.soundname]) 
            self.sound = self.sounds[self.soundtype][self.soundname] if self.soundtype == "music" else SoundLoader.load(self.sounds[self.soundtype][self.soundname]) 
        except:
            pass


    def random_music(self):
        try:
            music = list(self.sounds["music"].keys())[randint(0, len(list(self.sounds["music"].keys()))-1)]
            self.soundname = music
            A().root().current_sound = music
            self.load_sound()
            return music
        except:
            pass
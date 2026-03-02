from kivy.clock import Clock
from kivy.uix.image import AsyncImage
from A import A




class Animate(AsyncImage):

    path = "images/animations/"
    assets = {
        "explode": path + "explode.gif"
    }

    interval = None

    base_size = (150, 150)

    elapsed = 0

    def __init__(self, name, display_pos, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.display_pos = display_pos
        self.app_root = A().root()
        self.app_main = A().main()

        self.pos = display_pos
        self.source = self.app_root.resource_path(self.assets[name])
        self.anim_delay = 1/32
        self.size = self.base_size
        Clock.schedule_once(self.start, 0.5)
        

    def start(self, *args):
        if hasattr(self._coreimage, "anim") and self._coreimage.anim:
            self.length = len(self._coreimage.anim.frames)
            self.duration = self.length * self.anim_delay
        else:
            self.duration = 1.0
        self.app_main.add_widget(self)
        self.interval = Clock.schedule_interval(self.check_duration, .01)


    def check_duration(self, dt):
        self.elapsed += dt
        if self.elapsed >= self.duration:
            self.app_main.remove_widget(self)
            self.interval.cancel()
            self.interval = None
            self.elapsed = 0
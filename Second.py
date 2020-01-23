import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.button import Button

class MyGif(Image):
    frame_cnt = 0
    frame_no = 2
    def on_texture(self, instance, value):
        if self.frame_cnt == self.frame_no + 1:
            self._coreimage.anim_reset(True)
        self.frame_cnt += 1
        

class Emergency(App):
    def build(self):
        return MyGif(source="help.gif",size_hint=(0.5,0.5),pos_hint={'x':0.25,'y':0.45})
    
if __name__ == "__main__":
    Emergency().run()
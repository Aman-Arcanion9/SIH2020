import kivy
import math
from kivy.app import App
from kivy.animation import Animation,AnimationTransition
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView

from kivy.core.image import Image as CoreImage
from kivy.graphics import Color, Rectangle
def draw_background(widget, *args):
    widget.canvas.before.clear()
    with widget.canvas.before:
        Color(.2, .2, .2, 1)
        texture = CoreImage("logo1.PNG").texture
        texture.wrap = 'repeat'
        Rectangle(pos=widget.pos, size=(800,600), texture=texture)

class MyApp(App):
    def build(self):
        widget = Label(text="[color=#4dff4d][b]YOU ARE SAFE[/b][/color]",
                       markup=True,font_size=50,font_name='Arvo-Regular')
        draw_background(widget)
        pie = math.pi
        f = pie/180
        anim = Animation(pos=(-200,0),duration=0)
        i = 0
        while i<=2:
            i += 1
            angle = 15
            while angle<90:
                x_pos = -200*math.cos(angle*f)
                y_pos = 200*math.sin(angle*f)
                anim += Animation(pos=(x_pos,y_pos),duration=0.2)
                angle += 15
            angle = 0
            while angle<90:
                x_pos = 200*math.sin(angle*f)
                y_pos = 200*math.cos(angle*f)
                anim += Animation(pos=(x_pos,y_pos),duration=0.2)
                angle += 15
            angle = 0
            while angle<90:
                x_pos = 200*math.cos(angle*f)
                y_pos = -200*math.sin(angle*f)
                anim += Animation(pos=(x_pos,y_pos),duration=0.2)
                angle += 15
            angle = 0
            while angle<=90:
                x_pos = -200*math.sin(angle*f)
                y_pos = -200*math.cos(angle*f)
                anim += Animation(pos=(x_pos,y_pos),duration=0.2)
                angle += 15
            anim.repeat = True
            anim.start(widget)
            
        # anim.start(widget)
        return widget

if __name__ == "__main__":
    MyApp().run()

from random import randint, choice

from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import BooleanProperty, OptionProperty, NumericProperty

class Emergency(Image):
    def __init__(self, image="help.gif",**kwargs):
        self.source = image
        self.size = (50,50)
        super(Emergency, self).__init__(**kwargs)
        
        
# class Image(Widget):
    
#     # x = Button(text="Cancel",font_size=40)
#     # add_widget(x)
    
#     source = StringProperty(None)
#     texture = ObjectProperty(None, allownone=True)
#     texture_size = ListProperty([0, 0])
    
#     def get_image_ratio(self):
#         if self.texture:
#             return self.texture.width / float(self.texture.height)
#         return 1.

#     mipmap = BooleanProperty(False)
#     image_ratio = AliasProperty(get_image_ratio, bind=('texture',), cache=True)
#     color = ListProperty([1, 1, 1, 1])
#     allow_stretch = BooleanProperty(False)
#     keep_ratio = BooleanProperty(True)
#     keep_data = BooleanProperty(False)
#     anim_delay = NumericProperty(.25)
#     anim_loop = NumericProperty(0)
#     nocache = BooleanProperty(False)
    
#     def get_norm_image_size(self):
#         if not self.texture:
#             return self.size
#         ratio = self.image_ratio
#         w, h = self.size
#         tw, th = self.texture.size
#         if self.allow_stretch:
#             if not self.keep_ratio:
#                 return w, h
#             iw = w
#         else:
#             iw = min(w, tw)
#         ih = iw / ratio
#         if ih > h:
#             if self.allow_stretch:
#                 ih = h
#             else:
#                 ih = min(h, th)
#             iw = ih * ratio
#         return iw, ih

#     norm_image_size = AliasProperty(get_norm_image_size,
#                                     bind=('texture', 'size', 'allow_stretch',
#                                           'image_ratio', 'keep_ratio'),
#                                     cache=True)

#     def __init__(self, **kwargs):
#         self._coreimage = None
#         self._loops = 0
#         super(Image, self).__init__(**kwargs)
#         fbind = self.fbind
#         update = self.texture_update
#         fbind('source', update)
#         fbind('mipmap', update)
#         if self.source:
#             update()
#         self.on_anim_delay(self, kwargs.get('anim_delay', .25))
        
#         self.x = Button(text="Cancel",font_size=40)
#         self.add_widget(self.x)

#     def texture_update(self, *largs):
#         if not self.source:
#             self.texture = None
#         else:
#             filename = resource_find(self.source)
#             self._loops = 0
#             if filename is None:
#                 return Logger.error('Image: Error reading file {filename}'.
#                                     format(filename=self.source))
#             mipmap = self.mipmap
#             if self._coreimage is not None:
#                 self._coreimage.unbind(on_texture=self._on_tex_change)
#             try:
#                 if PY2 and isinstance(filename, str):
#                     filename = filename.decode('utf-8')
#                 self._coreimage = ci = CoreImage(filename, mipmap=mipmap,
#                                                  anim_delay=self.anim_delay,
#                                                  keep_data=self.keep_data,
#                                                  nocache=self.nocache)
#             except:
#                 Logger.error('Image: Error loading texture {filename}'.
#                                     format(filename=self.source))
#                 self._coreimage = ci = None

#             if ci:
#                 ci.bind(on_texture=self._on_tex_change)
#                 self.texture = ci.texture

#     def on_anim_delay(self, instance, value):
#         self._loop = 0
#         if self._coreimage is None:
#             return
#         self._coreimage.anim_delay = value
#         if value < 0:
#             self._coreimage.anim_reset(False)

#     def on_texture(self, instance, value):
#         if value is not None:
#             self.texture_size = list(value.size)

#     def _on_tex_change(self, *largs):
#         # update texture from core image
#         self.texture = self._coreimage.texture
#         ci = self._coreimage
#         if self.anim_loop and ci._anim_index == len(ci._image.textures) - 1:
#             self._loops += 1
#             if self.anim_loop == self._loops:
#                 ci.anim_reset(False)
#                 self._loops = 0

#     def reload(self):
#         try:
#             self._coreimage.remove_from_cache()

#         except AttributeError:
#             pass

#         oldsource = self.source
#         self.source = ''
#         self.source = oldsource


#     def on_nocache(self, *args):
#         if self.nocache and self._coreimage:
#             self._coreimage.remove_from_cache()
#             self._coreimage._nocache = True
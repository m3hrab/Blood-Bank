import imp
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

class Cards(MDApp):
    def build(self):
        box = Builder.load_file('labels.kv')
        return box
    
Cards().run()
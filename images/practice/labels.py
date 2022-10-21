from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel

class TestApp(MDApp):
    def build(self):
        box = Builder.load_file("labels.kv")
        # for i in range(4):
        #     box.ids.box.add_widget(
        #         MDLabel(
        #             text="Hello" + str(i)
        #             # color:
        #     ))
        return box 

TestApp().run()
from kivy.app import App
from kivy.lang.builder import Builder
helper = """
GridLayout:
    cols:1
    padding:20
    spacing:20
    TextInput:
        text:""
    TextInput:
        text:""
    Button:
        text:"login"
        on_press:root.showdata()
    Label:
        text:"amr matha"
"""


class MyApp(App):
    def build(self):
        a=Builder.load_string(helper)
        return a
    def showdata(self,obj):
        print("ok")
    
    
MyApp().run()


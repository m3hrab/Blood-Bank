from curses import window
from kivymd.app import MDApp
from kivy.lang.builder import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 

Window.size = (375,667)
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass 

class AppScreen(Screen):
    pass

class BloodBank(MDApp):

    def build(self):
        Builder.load_file("design.kv")
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(AppScreen(name="app"))
        return sm

    def login(self):
        # print(self.root.ids.password.text)
        pass

BloodBank().run()
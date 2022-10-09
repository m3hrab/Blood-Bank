from kivymd.app import MDApp
from kivy.lang.builder import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog


# Window.size = (375,667)
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass 

class AppScreen(Screen):
    pass

class BloodBank(MDApp):

    def build(self):
        Builder.load_file("design.kv")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(SignupScreen())
        sm.add_widget(AppScreen())
        return sm

    def login(self):
        login_screen = self.root.get_screen('login')
        # print("Email: " + login_screen.ids.email.text)
        # print("Password: " + login_screen.ids.password.text)
        self.show_alert_dialog()
        
    def show_alert_dialog(self):
        self.dialog = MDDialog(
            text="Discard draft?",
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
                MDFlatButton(
                    text="DISCARD",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                ),
            ],
        )
        self.dialog.open()

BloodBank().run()
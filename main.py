from kivymd.app import MDApp
from kivy.lang.builder import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import pandas as pd
from kivy.properties import ObjectProperty

Window.size = (375,667)
class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def validation(self):
        users = pd.read_csv('users.csv', sep=',')
        print(self.email.text)
        if self.email.text != '' and self.password.text != 0:
            # convert the numpy arry into a list to access the index easily ;p 
            temp_email = users['Email'].unique().tolist()
            temp_password = users['Password'].unique().tolist()
            if self.email.text in temp_email and self.password.text in temp_password:
                if temp_email.index(self.email.text) == temp_password.index(self.password.text):
                    print("Login Successfull")
                    app.root.manger.current = 'app'
                    self.email.text = ""
                    self.password.text = ""

    #     else:
    #         show_alert_dialog()

    # def show_alert_dialog(self):
    #     self.dialog = MDDialog(
    #         text="Discard draft?",
    #         buttons=[
    #             MDFlatButton(
    #                 text="CANCEL",
    #                 theme_text_color="Custom",
    #                 text_color=self.theme_cls.primary_color,
    #             ),
    #             MDFlatButton(
    #                 text="DISCARD",
    #                 theme_text_color="Custom",
    #                 text_color=self.theme_cls.primary_color,
    #             ),
    #         ],
    #     )
    #     self.dialog.open()

class SignupScreen(Screen):
    pass 

class AppScreen(Screen):
    pass

class BloodBank(MDApp):

    def build(self):
        Builder.load_file("design.kv")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen())
        self.sm.add_widget(SignupScreen())
        self.sm.add_widget(AppScreen())
        return self.sm

    def login(self):
        login_screen = self.root.get_screen('login')
        # print("Email: " + login_screen.ids.email.text)
        # print("Password: " + login_screen.ids.password.text)
        self.show_alert_dialog()
        


BloodBank().run()
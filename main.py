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
        if self.email.text != '' and self.password.text != '':
            # convert the numpy arry into a list to access the index easily ;p 
            temp_email = users['Email'].unique().tolist()
            temp_password = users['Password'].unique().tolist()
            if self.email.text in temp_email and self.password.text in temp_password:
                if temp_email.index(self.email.text) == temp_password.index(self.password.text):
                    print("Login Successfull")
                    self.parent.current = "app"
                    self.email.text = ""
                    self.password.text = ""

            else:
                n = self.parent.get_screen("login")
                msg = self.email.text
                n.show_alert_dialog(msg)
        else:
            n = self.parent.get_screen("login")
            msg = ''
            n.show_alert_dialog(msg)

    def show_alert_dialog(self, msg):

        if msg=="":
            self.dialog = MDDialog(
                text="Enter the email and password correctly",
            )
        else:
            self.dialog = MDDialog(
                text= msg + " doesn't exits",
            )
        self.dialog.open()
        

class SignupScreen(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    phone = ObjectProperty(None)
    address = ObjectProperty(None)
    bg = ObjectProperty(None)
    password = ObjectProperty(None)

    def registerbtn(self):
        # creating the Dataframe 
        user_info = pd.DataFrame([[self.username.text, self.email.text, self.phone.text,
                        self.address.text, self.bg.text, self.password.text]],
                        columns = ['Name', 'Email', 'Phone', 'Address', 'BG', 'Password'])

        user_info.to_csv('users.csv', mode = 'a', header = False, index = False)
        self.parent.current = 'login'
        self.username.text = ""
        self.email.text = ""
        self.phone.text = ""
        self.address.text = ""
        self.bg.text = ""
        self.password.text = ""
               

class AppScreen(Screen):
    pass

class BloodBank(MDApp):

    def build(self):
        Builder.load_file("design.kv")
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        sm = ScreenManager()
        sm.add_widget(LoginScreen())
        sm.add_widget(SignupScreen())
        sm.add_widget(AppScreen())
        return sm
        


BloodBank().run()
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

t = """
Screen:
    name = 'menu'
    BoxLayout:
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Quit'

Screen:
    name = 'settings'
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
"""

class TestApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        # sm.add_widget(MenuScreen(name='menu'))
        # sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()
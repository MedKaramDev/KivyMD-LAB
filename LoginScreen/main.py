from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty

class MainApp(MDApp):

    welcome_etat = StringProperty('WELCOME')
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Indigo'
        return Builder.load_file('login.kv')

    def logger(self):
        #self.root.ids.welcome_label.text = f"WELCOME {self.root.ids.user.text}"
        self.welcome_etat = f"CHEF {self.root.ids.user.text} !"

    def clear(self):
        self.root.ids.user.text = ''
        self.root.ids.password.text = ''
        self.welcome_etat = 'WELCOME'

MainApp().run()
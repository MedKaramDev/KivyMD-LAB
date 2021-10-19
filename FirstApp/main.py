from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Blue'
        return Builder.load_file('color_theme.kv')
DemoApp().run()

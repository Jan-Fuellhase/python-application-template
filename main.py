import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainWidget(BoxLayout):
    pass

class AppTemplate(App):
    def build(self):
        self.title = "My App Template"

        # Buttons
        select_file_btn = Button(text='Press me! I do nothing!')

        return MainWidget()

if __name__ == '__main__':
    AppTemplate().run()

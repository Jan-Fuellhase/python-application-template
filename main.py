import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainWidget(BoxLayout):
    pass

class AppTemplate(App):
    def build(self):
        self.title = "My App Template"

        # Tutorial how to also add buttons via python, not just via .kv file:
        
        # 1. Create an instance of your root widget.
        #    This will be populated with the widgets from your .kv file.
        main_widget = MainWidget()

        # 2. Create the button you want to add from Python.
        python_button = Button(text='Added from Python')
        
        # 3. Bind an action to the button.
        #    Let's make it call a method when pressed.
        python_button.bind(on_press=self.on_python_button_click)

        # 4. Add the new button to your main widget instance.
        #    Since MainWidget is a BoxLayout, this adds it to the layout.
        main_widget.add_widget(python_button)

        # 5. Return the modified root widget.
        return main_widget

    def on_python_button_click(self, instance):
        """This function is called when the button created in Python is clicked."""
        print(f"The button '{instance.text}' was clicked!")


if __name__ == '__main__':
    AppTemplate().run()
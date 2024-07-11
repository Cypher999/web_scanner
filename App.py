import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.textinput import TextInput  
from kivy.uix.button import Button  
from kivy.uix.label import Label

class FirstRow(GridLayout):
    def __init__(self,**kwargs):
        super(FirstRow,self).__init__(**kwargs)
        self.cols=2
        self.padding=5
        self.size_hint_y=None
        self.height=50
        self.input_web=TextInput(multiline=False,size_hint=(1.5,1))
        self.button=Button(text="Scan",size_hint=(0.5,1))
        self.add_widget(self.input_web)
        self.add_widget(self.button)
        

class MyApp(App):
    def build(self):
        layout=BoxLayout(orientation='vertical')
        textArea=TextInput(multiline=True)
        layout.add_widget(FirstRow())
        layout.add_widget(textArea)
        return layout

    def on_button_press(self):
        text_input_value = self.root.ids.text_input.text
        text_area_value = self.root.ids.text_area.text
        print(f"Text input: {text_input_value}")
        print(f"Text area: {text_area_value}")

if __name__ == '__main__':
    MyApp().run()

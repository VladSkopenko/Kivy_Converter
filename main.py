from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (250, 200)
Window.clearcolor = (0 / 255, 150 / 255, 3 / 255, 1)
Window.title = "Конвертер"


class MyApp(App):

    def __init__(self):
        super().__init__()
        self.title = 'Конвертер'
        self.label = Label(text='Введіть значення (км)')
        self.miles = Label(text='Милі')
        self.metres = Label(text='Метри')
        self.santimetres = Label(text='Сантиметрм')
        self.input_data = TextInput(hint_text='Введіть значення  (км)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.miles.text = 'Милі: ' + str(float(data) * 0.62)
            self.metres.text = 'Метри: ' + str(float(data) * 1000)
            self.santimetres.text = 'Сантиметри: ' + str(float(data) * 100000)
        else:
            self.input_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.miles)
        box.add_widget(self.metres)
        box.add_widget(self.santimetres)

        return box



if __name__ == "__main__":
    MyApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class SmartBlinds(BoxLayout):
    def __init__(self, **kwargs):
        super(SmartBlinds, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.bind(size=self._update_canvas, pos=self._update_canvas)

        # Blind Status
        self.status_label = Label(text="Blinds are CLOSED", font_size=24, color=(1, 1, 1, 1))  # White text
        self.add_widget(self.status_label)

        # The button for opening the Blinds
        open_button = Button(text='Open Blinds', font_size=24, background_color=(1, 0, 0, 1))  # Red
        open_button.bind(on_press=self.open_blinds)
        self.add_widget(open_button)

        # The button for closing the Blinds
        close_button = Button(text='Close Blinds', font_size=24, background_color=(0, 0, 1, 1))  # Blue
        close_button.bind(on_press=self.close_blinds)
        self.add_widget(close_button)

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Black background
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def open_blinds(self, instance):
        self.status_label.text = "Blinds are OPEN"
        print("Blinds opened.")

    def close_blinds(self, instance):
        self.status_label.text = "Blinds are CLOSED"
        print("Blinds closed.")

class BlindsApp(App):
    def build(self):
        return SmartBlinds()

if __name__ == '__main__':
    BlindsApp().run()

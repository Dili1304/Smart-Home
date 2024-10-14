import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button

kivy.require("2.0.0")  # kivy version

def build():
    # Creating the layout
    layout = BoxLayout(orientation='vertical')
    
    # System status label
    status_label = Label(text="System Status: Off", font_size=24)
    layout.add_widget(status_label)
    
    # TV State initially set to 'off'
    tv_state = {'is_on': False}

    # Toggle TV function that toggles the TV state each time the button is pressed
    def toggle_tv(instance):
        tv_state['is_on'] = not tv_state['is_on']
        if tv_state['is_on']:
            instance.text = "Turn TV Off"
            status_label.text = "System Status: TV On"
        else:
            instance.text = "Turn TV On"
            status_label.text = "System Status: TV Off"

    # TV button
    tv_button = Button(text="Turn TV On", on_press=toggle_tv)#pressing the button triggers the toggle
    layout.add_widget(tv_button)

    # Audio State - audio is initially off
    audio_state = {'is_on': False}

    # Toggle audio function
    def toggle_audio(instance):
        audio_state['is_on'] = not audio_state['is_on']
        if audio_state['is_on']:
            instance.text = "Turn Audio Off"
            status_label.text = "System Status: Audio On"
        else:
            instance.text = "Turn Audio On"
            status_label.text = "System Status: Audio Off"

    # Audio button
    audio_button = Button(text="Turn Audio On", on_press=toggle_audio)
    layout.add_widget(audio_button)

    # Volume Label
    volume_label = Label(text="Volume: 0%", font_size=18)
    layout.add_widget(volume_label)

    # Volume slider change function
    def on_volume_change(instance, value):#instance-The slider widget and value-The current value of the slider.
        volume_label.text = f"Volume: {int(value)}%"

    # Volume slider
    volume_slider = Slider(min=0, max=100, value=0)
    volume_slider.bind(value=on_volume_change)#
    layout.add_widget(volume_slider)

    return layout

# Kivy app definition
def run_app():
    app = App()#Creates an instance of the Kivy App class
    app.build = build# This tells Kivy to use the build function to construct the UI when the app starts.
    app.run()#Starts the Kivy event loop

if __name__ == "__main__":#run_app() is called only when the script is executed directly
    run_app()

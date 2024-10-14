import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button

kivy.require("2.0.0") #kivy version

class SmartHomeEntertainment(BoxLayout):
    def __init__(self, **kwargs):#defining the function
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # creating a lable for System status
        self.StatusLabel = Label(text="System Status: Off", font_size=24)
        self.add_widget(self.StatusLabel) #adds the StatusLabel to the SmartHomeEntertainment layout

        # creating a button for TV 
        self.TVbtn = Button(text="Turn TV On", on_press=self.toggleTV) 
        self.add_widget(self.TVbtn) #adds the TVbtn to the SmartHomeEntertainment layout

        # creating a button for Audio system
        self.AudioBtn = Button(text="Turn Audio On", on_press=self.toggleAudio)
        self.add_widget(self.AudioBtn)#adds the Audio system button to the SmartHomeEntertainment layout

        # Volume - allows users to adjust the volume from 0% to 100% 
        self.VolLabel = Label(text="Volume: 0%", font_size=18)
        self.add_widget(self.VolLabel)
        self.VolSlider = Slider(min=0, max=100, value=0)
        self.VolSlider.bind(value=self.OnVolumeChange)
        self.add_widget(self.VolSlider)

        

        # State tracking
        self.TV_ON = False
        self.Audio_ON = False

    #TV
    def toggleTV(self, instance):
        if self.TV_ON:
            instance.text = "Turn TV Off"
            self.StatusLabel.text = "System Status: TV On"
            self.TV_ON = False
        else:
            instance.text = "Turn TV On"
            self.StatusLabel.text = "System Status: TV Off"
            self.TV_ON = True

    #Audio system
    def toggleAudio(self, instance):
        if self.Audio_ON:
            instance.text = "Turn Audio Off"
            self.StatusLabel.text = "System Status: Audio On"
            self.Audio_ON = False
        else:
            instance.text = "Turn Audio On"
            self.StatusLabel.text = "System Status: Audio Off"
            self.Audio_ON = True


    def OnVolumeChange(self, instance, value): # value is the current value of the slider when it changes 
        self.VolLabel.text = f"Volume: {int(value)}%"

#Creating a new class SmartSystemApp
class SmartSystemApp(App):
    def build(self):
        return SmartHomeEntertainment()

SmartSystemApp().run()
#Features:
#TV Control: Button to toggle the TV on and off.
#Volume Adjustment: Slider to control the volume level, displayed in percentage.
#Audio System: Button to turn the audio system on and off.
#Status Display: Label that shows the current state of the system (TV, media playback, audio).
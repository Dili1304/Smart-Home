#from kivy.uix.accordion import StringProperty
import kivy
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider

class Hightemp(Popup):
    pass
class Lowtemp(Popup):
    pass
class LOPopup(Popup):
    pass
class Myboxlayout(BoxLayout):
    pass
class LFPopup(Popup):
    pass
class Sliderx(Slider):
    pass
class Temper_reset(Popup):
    pass
class MyWidget(Widget):
    #temperature_value= StringProperty("Value")
    def open_popup(self):
        pops= LOPopup()
        pops.open()
    def open_pops(self):
            popc=LFPopup()
            popc.open()
    def open_High(self):
        High=Hightemp()
        High.bind(on_dismiss=self.reset_slider)#this binds the popup to the reset once dismissed
        High.bind(on_dismiss=self.temp_reset)#This displays a popup that temperatures have been reset
        High.open()
    def temp_reset(self,on_dismiss):
        Res=Temper_reset()
        Res.open()
    def reset_slider(self,on_dismiss):#this ensures resetting the temp once dismissed
        self.ids.temperature.value=24
        
    def open_Low(self):
        Low=Lowtemp()
        Low.bind(on_dismiss=self.reset_slider)
        Low.bind(on_dismiss=self.temp_reset)#This displays a popup that temperatures have been reset
        Low.open()
    def slider_on_value(self,widget):
        print("Slider "+str(int(widget.value)))
        if widget.value>= widget.max:
            self.open_High()
        if widget.value<=widget.min:
            self.open_Low()       
        #self.temperature_value=str(int(widget.value)) this is one way of doing it
class Mylightapp(App):
    def build (self):
        return MyWidget()
Mylightapp().run()

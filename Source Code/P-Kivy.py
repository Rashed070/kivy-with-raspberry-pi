import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
import kivy
kivy.require('1.11.0')


from kivy.app import App
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock

import RPi.GPIO as GPIO


speed = 1.0


ledPin1 = 27
ledPin2 = 23
ledPin3 = 17
ledPin4 = 22
beepPin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(beepPin, GPIO.OUT)
GPIO.output(beepPin, GPIO.LOW)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.output(ledPin1, GPIO.LOW)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.output(ledPin2, GPIO.LOW)
GPIO.setup(ledPin3, GPIO.OUT)
GPIO.output(ledPin3, GPIO.LOW)
GPIO.setup(ledPin4, GPIO.OUT)
GPIO.output(ledPin4, GPIO.LOW)


def myButton1(leding):
    print("Button pressed,", leding.text)
    if leding.text == 'Alert!':
        GPIO.output(beepPin, GPIO.HIGH)
        Clock.schedule_once(noBeep, 1.0)

    if leding.text == 'Food':
       if leding.state == "down":
            print ("button on")
            GPIO.output(ledPin1, GPIO.HIGH)
            
       else:
            print ("button off")
            GPIO.output(ledPin1, GPIO.LOW)
            
            

def myButton2(leding):

    if leding.text == 'Drinks':
       if leding.state == "down":
            print ("button on")
            GPIO.output(ledPin2, GPIO.HIGH)
            
       else:
            print ("button off")
            GPIO.output(ledPin2, GPIO.LOW)
            
            

def myButton3(leding):
    if leding.text == 'Pills':
       if leding.state == "down":
            print ("button on")
            GPIO.output(ledPin3, GPIO.HIGH)
            
       else:
            print ("button off")
            GPIO.output(ledPin3, GPIO.LOW)
            
            
def myButton4(leding):
    if leding.text == 'Rest':
       if leding.state == "down":
            print ("button on")
            GPIO.output(ledPin4, GPIO.HIGH)
            
       else:
            print ("button off")
            GPIO.output(ledPin4, GPIO.LOW)
            
            
            
            
def noBeep(ded):
    GPIO.output(beepPin, GPIO.LOW)




class MyFirstKivyApp(App):
    
    def build(self):
        layout = GridLayout(cols=3, spacing=50, padding=50, row_default_height=150)
        
        opc1=ToggleButton(text="Food", background_color=(0,0,1,1), font_size=50)
        opc1.bind(on_press=myButton1)
        
        opc2=ToggleButton(text="Drinks", background_color=(0,0,1,1), font_size=50)
        opc2.bind(on_press=myButton2)
        
        opc3=ToggleButton(text="Pills", background_color=(0,0,1,1), font_size=50)
        opc3.bind(on_press=myButton3)
        
        opc4=ToggleButton(text="Rest", background_color=(0,0,1,1), font_size=50)
        opc4.bind(on_press=myButton4)
        
        opc5=ToggleButton(text="Exit", background_color=(0,0,1,1), font_size=50)
        opc5.bind(on_press=self.exitB)
        
        beepButton=Button(text="Alert!", background_color=(0,0,1,1), font_size=50)
        beepButton.bind(on_press=myButton1)
        

        layout.add_widget(beepButton)
        layout.add_widget(opc1)
        layout.add_widget(opc2)
        layout.add_widget(opc3)
        layout.add_widget(opc4)
        layout.add_widget(opc5)
        
        

        return layout
    
    
    
    def exitB(self):
        App.get_running_app().stop()
        Window.close()
    
    def on_stop(self):
        Logger.critical('Exit')
    
    

if _name_ == '_main_':
    MyFirstKivyApp().run()
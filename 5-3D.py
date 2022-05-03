from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)


ledPin = LED(18)

win = Tk()
win.title("LED controller")
myFont = tkinter.font.Font(family = 'Helvetica', size = 15)

def Dot():
    ledPin.on()
    time.sleep(0.5)
    ledPin.off()
    time.sleep(0.5)
   

def Dash():
    ledPin.on();
    time.sleep(2)
    ledPin.off()
    time.sleep(0.5)
   

def exit():
    RPi.GPIO.cleanup
    win.destroy()
 
def MorseConvert(MorseBLink):
    for letter in MorseBLink:
        if (letter.lower() == 'a'):
                Dot()
                Dash()
           
        elif (letter.lower() == 'b'):
                Dash()
                Dot()
                Dot()
                Dot()
               
        elif (letter.lower() == 'c'):
                Dash()
                Dot()
                Dash()
                Dot()
               
        elif (letter.lower() == 'd'):
                Dash()
                Dot()
                Dot()
               
        elif (letter.lower() == 'e'):
                Dot()
               
        elif (letter.lower() == 'f'):
                Dot()
                Dot()
                Dash()
                Dot()
               
        elif (letter.lower() == 'g'):
                Dash()
                Dash()
                Dot()
               
        elif (letter.lower() == 'h'):
                Dot()
                Dot()
                Dot()
                Dot()
               
        elif (letter.lower() == 'i'):
                Dot()
                Dot()
               
        elif (letter.lower() == 'j'):
                Dot()
                Dash()
                Dash()
                Dash()
           
        elif (letter.lower() == 'k'):
                Dash()
                Dot()
                Dash()
               
        elif (letter.lower() == 'l'):
                Dot()
                Dash()
                Dot()
                Dot()
               
        elif (letter.lower() == 'm'):
                Dash()
                Dash()
               
        elif (letter.lower() == 'n'):
                Dash()
                Dot()
               
        elif (letter.lower() == 'o'):
                Dash()
                Dash()
                Dash()
               
        elif (letter.lower() == 'p'):
                Dot()
                Dash()
                Dash()
                Dot()
               
        elif (letter.lower() == 'q'):
                Dash()
                Dash()
                Dot()
                Dash()
               
        elif (letter.lower() == 'r'):
                Dot()
                Dash()
                Dot()
               
        elif (letter.lower() == 's'):
                Dot()
                Dot()
                Dot()
               
        elif (letter.lower() == 't'):
                Dash()
               
        elif (letter.lower() == 'u'):
                Dot()
                Dot()
                Dash()
               
        elif (letter.lower() == 'v'):
                Dot()
                Dot()
                Dot()
                Dash()
               
        elif (letter.lower() == 'w'):
                Dot()
                Dash()
                Dash()
               
        elif (letter.lower() == 'x'):
                Dash()
                Dot()
                Dot()
                Dash()
               
        elif (letter.lower() == 'y'):
                Dash()
                Dot()
                Dash()
                Dash()
               
        elif (letter.lower() == 'z'):
                Dash()
                Dash()
                Dot()
                Dot()
def MorseBLink():
    MorseBLink = TextInput.get("1.0","end-1c")
    MorseConvert(MorseBLink)
   
TextInput = Text(win, height = 10, width = 40, bg = "white")
TextInput.grid(row=0,column=1 )

Morse=  Button(win, text = 'Blink', font = myFont, command = MorseBLink, bg = 'green', width = 30)
Morse.grid(row=1,column=1)

exitbutton = Button(win, text = 'exit', font = myFont, command = exit, bg = 'red', height = 1, width = 30)
exitbutton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW")
win.mainloop()  
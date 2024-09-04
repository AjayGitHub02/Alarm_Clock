from tkinter.ttk import * 
from tkinter import * 

from datetime import datetime
from time import sleep

from pygame import mixer 

#window
window = Tk()
window.title("h")
window.geometry("350x150")


def alarm_tone():
    mixer.music.load("alarmtone.mp3")
    mixer.music.play()
    
def alarm():
    while True:
        control = 1
        print(control)
        
        alarm_hour="11"
        alarm_minute="57"
        alarm_second="00"
        alarm_period="PM".upper()
        
        now = datetime.now()
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        if control == 1:
            if alarm_period == period: 
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("Time to take a break!")
                            alarm_tone()
                            
        sleep(1)

mixer.init()
alarm()

window.mainloop()

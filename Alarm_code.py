from threading import Thread
from tkinter.ttk import * 
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from datetime import datetime
from time import sleep


#colors
bg_color = "#ffffff"
col1 = "#ed4a4a"
col2 = "white"

#window
window = Tk()
window.title("Alarm Clock")
window.geometry("440x140")
window.configure(bg="grey")

#frame
frame_line = Frame(window, width=480, height=5, bg=col1)
frame_line.grid(row=1, column=0)

frame_body = Frame(window, width=480, height=180, bg=col2)
frame_body.grid(row=2, column=0)

#configuring from body
img = Image.open("alarmclock.png")
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=130, image=img, bg=bg_color) 
app_image.place(x=8, y=4) 


#title
name = Label(frame_body, text="Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
name.place(x=130, y=2)

#hours
hour = Label(frame_body, text="Hour", height=2, font=('Ivy 10 bold'), bg=bg_color, fg="purple")
hour.place(x=130, y=32)

c_hour = Combobox(frame_body, width=3, font=("arial 15"))
c_hour["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=130, y=58)

#minutes
minute = Label(frame_body, text="Minute", height=1, font=('Ivy 10 bold'), bg=bg_color, fg="purple")
minute.place(x=200, y=40)

c_minutes = Combobox(frame_body, width=3, font=("arial 15"))
c_minutes["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60")
c_minutes.current(0)
c_minutes.place(x=200, y=58)

#seconds
second = Label(frame_body, text="Second", height=1, font=('Ivy 10 bold'), bg=bg_color, fg="purple")
second.place(x=270, y=40)

c_second = Combobox(frame_body, width=3, font=("arial 15"))
c_second["values"] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60")
c_second.current(0)
c_second.place(x=270, y=58)

#period
period = Label(frame_body, text="Period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg="purple")
period.place(x=340, y=40)

c_period = Combobox(frame_body, width=4, font=("arial 15"))
c_period["values"] = ("AM", "PM")
c_period.current(0)
c_period.place(x=340, y=58)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

##activation
rad1 = Radiobutton(frame_body, font=("arial 10 bold"), value = 1, text="Activate", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x = 125, y=95)

def alarm_tone():
    mixer.music.load("alarmtone.mp3")
    mixer.music.play()
    selected.set(0)
    
##Deactivation
rad2 = Radiobutton(frame_body, font=("arial 10 bold"), value = 2, text="Deactivate", bg=bg_color, command=deactivate_alarm, variable=selected)
rad2.place(x = 210, y=95)

def alarm():
    while True:
        control = selected.get()
        print(control)
        
        alarm_hour=c_hour.get()
        alarm_minute=c_minutes.get()
        alarm_second=c_second.get()
        alarm_period=c_period.get()
        alarm_period=str(alarm_period).upper()
        
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

window.mainloop() 

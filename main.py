from tkinter import *
import time


#------------------------Functions---------------#
start_time = time.time()

def start_typing():
    global start_time
    start_time = time.time()
    text_entry.bind('<KeyRelease>',check_typing)

def check_typing(event):
    global start_time
    typed_text=text_entry.get()    
    if typed_text == text_to_type:
        elapsed_time = time.time() - start_time
        text_entry.unbind('<KeyRelease>')
        calculate_speed(elapsed_time)

def calculate_speed(elapsed_time):
    text_length = len(text_to_type)
    typing_speed = text_length / (elapsed_time/60)
    speed_label.config(text=f"Your typing speed: {round(typing_speed, 2)} WPM")     


#------------------------UI---------------#

window = Tk()
window.title("Typing Speed Test")

text_to_type="This is a typing speed test & im testing my typing speed "
typing_label = Label(text="Type the  following")
typing_label.pack()

text_display = Label(text=text_to_type)
text_display.pack()

text_entry=Entry()
text_entry.pack()

start_button = Button(text="Start Typing",command=start_typing)
start_button.pack()


speed_label = Label(text=" ")
speed_label.pack()

window.mainloop()
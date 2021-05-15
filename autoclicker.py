# Press f7 for start
# Press f8 for break
# mr_sajt author

import time
from tkinter.constants import ON
from typing import Text
import pyautogui as pg
from tkinter import *
import keyboard



window = Tk()
window.title("Autoclicker")
window.geometry("800x600")


def number():
    try:
        int(my_box.get())
        answer.config(text="You can turn off with F8!")
        for i in range(int(my_box.get())):
            pg.click()
            if keyboard.is_pressed("f8") == True:
                answer.config(text="):")
                break
                
    except ValueError:
        answer.config(text="ONLY NUMBER!")


my_label = Label(window, text="ENTER THE NUMBER OF CLICKS")
my_label.pack(pady=20)

my_box = Entry(window)
my_box.pack(pady=10)

my_button = Button(window, text="Start", command=number)
my_button.pack(pady=5)

answer = Label(window, text="")
answer.pack(pady=20)

window.mainloop()
time.sleep(5)

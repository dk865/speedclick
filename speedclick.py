import tkinter as tk
from tkinter import ttk
import math

global time
time = 10

global clicks
clicks = 0

global tmvalue
tmvalue = 10

def updateclock():
    if time > 0:
        root.after(1000, sub)
        clock.config(text=f"{time}", fg="black")
    if time == 0:
        global clicks
        global tmvalue
        clock.config(text=f"Time Up! You clicked about {math.ceil(clicks / tmvalue)} times per second.", fg="red")
        button.config(state="disabled")
        startbutton.config(state="active", text="Restart", command=restart)

def sub():
    global time
    time -= 1
    updateclock()

def start():
    global time
    global tmvalue
    time = tmvalue
    startbutton.config(state="disabled", text="Wait...")
    button.config(state="disabled")
    clock.config(text="Ready...", fg="red")
    root.after(1000, yellow)

def yellow():
    clock.config(text="Set...", fg="orange")
    root.after(1000, green)

def green():
    global time
    time -= 1
    clock.config(text="Go!!!", fg="green")
    startbutton.config(text="Go Go Go!")
    button.config(state="active")
    root.after(1000, updateclock)
 
def click():
    global clicks
    clicks += 1
    button.config(text=f"Clicks: {clicks}", command=click)

def restart():
    global time
    global tmvalue
    time = tmvalue
    global clicks
    clicks = 0
    button.config(text=f"Clicks: {clicks}", command=click)
    start()

def update_sec(val):
    global tmvalue
    tmvalue = int(val)

root = tk.Tk()
root.title("Speed Click!")

border1 = tk.Label(root, text="-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-", font=("Roboto", 10))
border1.pack()

title = tk.Label(root, text="Speed Click", font=("Roboyo", 15), fg="teal")
title.pack()

madebyme = tk.Label(root, text="Made by dk865", font=("Roboto", 10), fg="grey")
madebyme.pack()

ammount = tk.Scale(root, label="Seconds to Click:", from_=10, to=60, orient=tk.HORIZONTAL, command=update_sec)
ammount.pack()

clock = tk.Label(text="Press the button to start.")
clock.pack()

button = tk.Button(text=f"Clicks: {clicks}", command=click, state="disabled")
button.pack()

startbutton = tk.Button(text="Start", command=start)
startbutton.pack()

border2 = tk.Label(text="-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-", font=("Roboto", 10))
border2.pack()

root.mainloop()
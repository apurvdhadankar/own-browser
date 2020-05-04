# Make your own browser Using Python

import tkinter as tk
from tkinter import *
import webbrowser

win = tk.Tk()
win.title("WebBrowser")
win.geometry("600x600")
win.iconbitmap('icon.jpeg')

def google():
    webbrowser.open("www.google.com")

def youtube():
    webbrowser.open("www.youtube.com")

def amazon():
    webbrowser.open("www.amazon.com")

def facebook():
    webbrowser.opne("www.facebook.com")

igoogle = PhotoImage(file="google.png")
google = tk.Button(win, image=igoogle, command=google)

google.grid(row=0,column=0)

iyoutube = PhotoImage(file="youtube.png")
youtube = tk.Button(win,image=iyoutube,command=youtube)
youtube.grid(row=0,column=1)

iamazon = PhotoImage(file="amazon.png")
amazon = tk.Button(win,image=iamazon,command=google)
amazon.grid(row=1,column=0)

ifacebook = PhotoImage(file="facebook.png")
facebook = tk.Button(win, image=ifacebook,command=google)
facebook.grid(row=1,column=1)

win.mainloop()

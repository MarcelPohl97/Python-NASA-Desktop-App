import requests
import json
from tkinter import *
import os
import urllib.request
import webbrowser
from PIL import ImageTk,Image


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("NASA Daily Astronomy Picture of the day")
        self.WIDTH = 800
        self.HEIGHT = 600
        self.size = 600
        self.images()
        self.window_size()
        self.frames()
        self.labels()
        self.buttons()
        self.text_widget()

        self.mainloop()

    def images(self):
        self.nasa = PhotoImage(file="nasalogo.png")

    def frames(self):
        self.picture_frame = Frame(self.canvas, bg="lightgrey", bd=3, relief="ridge")
        self.picture_frame.place(relx=0.4, rely=0.01, relwidth=0.59, relheight=0.5)
        self.text_frame = Frame(self.canvas, bg="lightgrey", bd=3, relief="ridge")
        self.text_frame.place(relx=0.009, rely=0.52, relwidth=0.83, relheight=0.47)
        self.button_frame = Frame(self.canvas, bg="lightgrey", bd=3, relief="ridge")
        self.button_frame.place(relx=0.84, rely=0.52, relwidth=0.15, relheight=0.47)


    def buttons(self):
        self.get_information = Button(self.button_frame, text="Get Information", font="Arial 10", bg="darkgrey", relief="ridge", command= lambda: self.get_astro_data())
        self.get_information.place(relx=0.05, rely=0.004, relwidth=0.9, relheight=0.19)
        self.save_information = Button(self.button_frame, text="Save Information", font="Arial 10", bg="darkgrey", relief="ridge", command= lambda: self.save_daily_nasa_information())
        self.save_information.place(relx=0.05, rely=0.20, relwidth=0.9, relheight=0.19)
        self.download_image = Button(self.button_frame, text="Download Image", font="Arial 10", bg="darkgrey", relief="ridge", command= lambda: self.download_picture())
        self.download_image.place(relx=0.05, rely=0.40, relwidth=0.9, relheight=0.19)
        self.nasa_api = Button(self.button_frame, text="Nasa API", font="Arial 10", bg="darkgrey", relief="ridge", command= lambda: self.open_nasa_api())
        self.nasa_api.place(relx=0.05, rely=0.60, relwidth=0.9, relheight=0.19)
        self.about = Button(self.button_frame, text="About", font="Arial 10", bg="darkgrey", relief="ridge")
        self.about.place(relx=0.05, rely=0.804, relwidth=0.9, relheight=0.19)

    def text_widget(self):
        self.text_ = Text(self.text_frame, font="Arial 14", bg="darkgrey")
        self.text_.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.96)

    def labels(self):
        self.picture_label = Label(self.picture_frame, bg="darkgrey", bd=3, relief="ridge")
        self.picture_label.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def window_size(self):
        self.canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg="#333333")
        self.canvas.create_image(155,150, image=self.nasa)
        self.canvas.pack()



    def get_astro_data(self):
        try:
            Nasa_dailyinfo = "https://api.nasa.gov/planetary/apod?api_key=93IbCsql4yIRiHnSej8MEZ8BvMUr0oS4sK7k6mTC"
            r = requests.get(Nasa_dailyinfo).json()
            self.picture = r["hdurl"]
            urllib.request.urlretrieve(self.picture, "DailyNasaPicture.png")
            self.text_.insert(INSERT, "Date: " + r["date"] + " " + "Title: " + r["title"] + "\n" + "Explanation: " + r["explanation"])
            self.image = ImageTk.PhotoImage(Image.open("DailyNasaPicture.png").resize((self.size, self.size)))
            self.picture_label.configure(image=self.image)
        except:
            self.text_.insert(INSERT, "ERROR COULDNT RECEIVE DATA")


    def download_picture(self):
        Nasa_dailyinfo = "https://api.nasa.gov/planetary/apod?api_key=93IbCsql4yIRiHnSej8MEZ8BvMUr0oS4sK7k6mTC"
        r = requests.get(Nasa_dailyinfo).json()
        self.picture = r["hdurl"]
        webbrowser.open_new_tab('%s' % self.picture)
        urllib.request.urlretrieve(self.picture, r["title"] + ".png")

    def open_nasa_api(self):
        website = "https://api.nasa.gov/"
        webbrowser.open_new_tab('%s' % website)

    def save_daily_nasa_information(self):
        Nasa_dailyinfo = "https://api.nasa.gov/planetary/apod?api_key=93IbCsql4yIRiHnSej8MEZ8BvMUr0oS4sK7k6mTC"
        r = requests.get(Nasa_dailyinfo).json()
        with open("dailynasa.txt", 'a') as f:
            f.write("Date: " + r["date"] + " " + "Title: " + r["title"] + "\n" + "Explanation: " + r["explanation"])
            f.write('\n')
            f.close()

    def mainloop(self):
        self.root.mainloop()


App()
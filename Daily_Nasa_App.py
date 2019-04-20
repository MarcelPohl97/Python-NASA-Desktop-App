import requests
import urllib.request
import webbrowser
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk




class App:
    def __init__(self):
        self.root = ThemedTk()
        self.root.title("Daily Nasa Knowledge App")
        self.size = 500
        self.root.geometry("650x700")
        ttk.Style().theme_use("black")
        ttk.Style().configure("TButton", font="OpenSans 9 bold", anchor="center", background="#47d1ff", foreground="white")
        ttk.Style().configure("TFrame", relief="ridge")
        self.frames()
        self.labels()
        self.create_buttons()
        self.mainloop()

    def images(self):
        self.nasapicture = ImageTk.PhotoImage(file="nasapic.png")

    def frames(self):
        self.window_frame = ttk.Frame(self.root)
        self.window_frame.place(relheight=1, relwidth=1)
        self.buttons_frame = ttk.Frame(self.window_frame)
        self.buttons_frame.place(relx=0.015, rely=0.025, relheight=0.1, relwidth=0.97)
        self.picture_frame = ttk.Frame(self.window_frame)
        self.picture_frame.place(relx=0.18, rely=0.15, relheight=0.35, relwidth=0.65)
        self.text_frame = ttk.Frame(self.window_frame)
        self.text_frame.place(relx=0.015, rely=0.528, relheight=0.449, relwidth=0.97)

    def labels(self):
        self.picture_label = ttk.Label(self.picture_frame, relief="ridge")
        self.picture_label.place(relx=0.01, rely=0.02, relheight=0.96, relwidth=0.98)
        self.text_label = ttk.Label(self.text_frame, relief="ridge", wraplength=615, font="OpenSans 13 bold", anchor="nw")
        self.text_label.place(relx=0.01, rely=0.02, relheight=0.96, relwidth=0.98)

    def create_buttons(self):
        self.get_data = ttk.Button(self.buttons_frame, text="Get Information", command= lambda: self.get_astro_data())
        self.get_data.place(relx=0.01, rely=0.18, relheight=0.6, relwidth=0.19)
        self.save_data = ttk.Button(self.buttons_frame, text="Save Information", command= lambda: self.save_daily_nasa_information())
        self.save_data.place(relx=0.205, rely=0.18, relheight=0.6, relwidth=0.19)
        self.download_image = ttk.Button(self.buttons_frame, text="Download Image", command= lambda: self.download_picture())
        self.download_image.place(relx=0.405, rely=0.18, relheight=0.6, relwidth=0.19)
        self.nasa_api = ttk.Button(self.buttons_frame, text="Nasa API", command= lambda: self.open_nasa_api())
        self.nasa_api.place(relx=0.605, rely=0.18, relheight=0.6, relwidth=0.19)
        self.about_ = ttk.Button(self.buttons_frame, text="About")
        self.about_.place(relx=0.8, rely=0.18, relheight=0.6, relwidth=0.19)

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

    def download_picture(self):
        Nasa_dailyinfo = "https://api.nasa.gov/planetary/apod?api_key=93IbCsql4yIRiHnSej8MEZ8BvMUr0oS4sK7k6mTC"
        r = requests.get(Nasa_dailyinfo).json()
        self.picture = r["hdurl"]
        webbrowser.open_new_tab('%s' % self.picture)
        urllib.request.urlretrieve(self.picture, r["title"] + ".png")

    def get_astro_data(self):
        Nasa_dailyinfo = "https://api.nasa.gov/planetary/apod?api_key=93IbCsql4yIRiHnSej8MEZ8BvMUr0oS4sK7k6mTC"
        r = requests.get(Nasa_dailyinfo).json()
        self.picture = r["hdurl"]
        urllib.request.urlretrieve(self.picture, "DailyNasaPicture.png")
        self.text_label.configure(text= "Date: " + r["date"] + " " + "Title: " + r["title"] + "\n" + "Explanation: " + r["explanation"])
        self.image = ImageTk.PhotoImage(Image.open("DailyNasaPicture.png").resize((self.size, self.size)))
        self.picture_label.configure(image=self.image)

    def mainloop(self):
        self.root.mainloop()
App()

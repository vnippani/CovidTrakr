import tkinter as tk
from tkinter import Tk
import requests
from tkinter import Label
from functools import partial
from tkinter import PhotoImage

import requests
from bs4 import BeautifulSoup

from parseDt import getNumDataSection
import os

class Tracker:
    root = tk.Tk()
    canvas = tk.Canvas(root,height = 600, width = 900, bg="#691C1C")
    
    #default page is the main page
    def __init__(self):
        self.root.resizable(width=False, height=False)
        self.canvas.pack()  
        self.mainInterface()
        self.root.mainloop()
       
    #place an image on the canvas 
    def placeImage(self,im,xPos,yPos):
        photo = tk.PhotoImage(file = im)
        label = Label(image = photo, borderwidth=0, highlightthickness=0)
        label.image = photo
        label.place(x=xPos,y=yPos,anchor=tk.CENTER)
    
    #clear the app screen
    def clear(self):
        list = self.root.place_slaves()
        for l in list:
            l.place_forget()
            
    #change to a state
    def changeInterfaceToState(self,dropDownText):
        if(dropDownText.get() != "---"):
            #clear the screen
            self.clear()
            state = dropDownText.get() 
            
            #If state name is two words, make into one word
            if state == "New York":
                state = "New-York"
            elif state == "New Jersey":
                state = "New-Jersey"
            elif state == "New Mexico":
                state = "New-Mexico"
            elif state == "North Carolina":
                state = "North-Carolina"
            elif state == "South Carolina":
                state = "South-Carolina"
            elif state == "Rhode Island":
                state = "Rhode-Island"
            elif state == "North Dakota":
                state = "North-Dakota"
            elif state == "South Dakota":
                state = "South-Dakota"
            elif state == "New Hampshire":
                state = "New-Hampshire"
            
            state = state.lower() 
            
            #get state image
            im = r"C:\Users\vinee\Python\CovidTrakr\state" + state + ".png"
            self.placeImage(im,80,70)
            
            ###add code to create frames for data and news
            im = r"C:\Users\vinee\Python\CovidTrakr\frame1.png"
            self.placeImage(im,750,350)
            
            self.getStateInfo(state)
            
            
    #Get info for each state from the internet
    def getStateInfo(self,state):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        URL = "https://www.nytimes.com/interactive/2020/us/" + state + "-coronavirus-cases.html"
        page = requests.get(URL,headers=headers)
        html = BeautifulSoup(page.content, 'html.parser')
        text = html.find('div', {'class': 'counts svelte-9rb9hv'}).get_text()
        cases = getNumDataSection("Total cases",text)
        ###add text to get deaths and display both total cases and deaths
        
            
    
    #create main page widgits
    def mainInterface(self):
        #create main page image
        im = r"C:\Users\vinee\Python\CovidTrakr\MainScreen.png"
        self.placeImage(im,450,200)

        #drop down - user selects state from here
        state = tk.StringVar()
        state.set("---")
        drop = tk.OptionMenu(self.root,state,"---","Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Guam", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Minor Outlying Islands", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Northern Mariana Islands", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "U.S. Virgin Islands", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")
        drop.place(x=450,y=450,anchor=tk.CENTER)

        #select button - pressing will send you to desired state info
        buttonCaller = partial(self.changeInterfaceToState,state)
        sel = tk.Button(self.root,text="Select",padx = 10, pady = 5, fg = "white",bg="#691C1C",command = buttonCaller)
        sel.place(x=450,y=400,anchor=tk.CENTER)





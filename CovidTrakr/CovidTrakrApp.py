import tkinter as tk
from tkinter import Tk
import requests
from tkinter import Label
from functools import partial
from tkinter import PhotoImage


from bs4 import BeautifulSoup
import requests
import os


os.chdir("C:/Users/vinee/Python/CovidTrakr")

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'TrakrFace.png')
def stripToNum(textToStrip):
    if isinstance(textToStrip, str):
        #every "i" value is a single char in the string price. ord() gets the ascii values and sees if they
        #are in the range to be considered valid numbers
        num = ""
        for i in textToStrip:
            if (ord(i) >= 48 and ord(i) <= 57) or ord(i) == 46:
                num = num + i
        return float(num)

def getNumDataSection(dataSec,data):
    if isinstance(dataSec,str) and isinstance(data,str):
        index = data.find(dataSec)
        if index != -1:
            num = ''
            i = index + len(dataSec)
            while(i < len(data)):
                order = ord(data[i])
                if not ((order < 48 or order > 57) and order != 46):
                    break   
                i = i + 1                 
            while(i < len(data)):
                order = ord(data[i])
                if (order >= 48 and order <= 57) or order == 46 or order == 44:
                    num = num + data[i]
                else:
                    break
                i = i + 1 
            return num
        
class Tracker:
    root = tk.Tk()
    canvas = tk.Canvas(root,height = 600, width = 900, bg="#691C1C")
    
    #default page is the main page
    def __init__(self):
        self.root.resizable(width=False, height=False)
        self.canvas.pack()  
        self.mainInterface()
        self.root.mainloop()
       
    #shortcut function to place an image on the canvas 
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
    
    #switch back to main interface
    def changeInterfaceToMain(self):
        self.clear()
        self.mainInterface()
        
    #change to a state
    def changeInterfaceToState(self,dropDownText):
        if(dropDownText.get() != "---"):
            #clear the screen
            self.clear()
            state = dropDownText.get() 
            
            #get cases and deaths
            stats = self.getStateInfo(state)
            print(stats)
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
            elif state == "West Virginia":
                state = "West-Virginia"
            
            state = state.lower() 
            
            #get state image
            im = r"state" + state + ".png"
            self.placeImage(im,80,70)
            
            #create "back" button
            buttonCaller = partial(self.changeInterfaceToMain)
            sel = tk.Button(self.root,text="Back",padx = 10, pady = 5, fg = "white",bg="#691C1C",command = buttonCaller)
            sel.place(x=855,y=50,anchor=tk.CENTER)
            
            #create frames for data and news
            im = r"frame1.png"
            self.placeImage(im,750,350)
            
            #print data to screen         
            casesD = "Total Cases: " + stats[0]
            casesText = Label(text=casesD)  
            casesText.config(font=("Times New Roman", 20))
            casesText.place(x=750,y=150,anchor=tk.CENTER)  
        
            if stats[1] != '':
                nCasesD = "New Cases: " + stats[1]
                nCasesText = Label(text = nCasesD) 
                nCasesText.config(font=("Times New Roman", 20))
                nCasesText.place(x=750,y=200,anchor=tk.CENTER)
            
            deathsD = "Total Deaths: " + stats[2]
            deathsText = Label(text=deathsD)
            deathsText.config(font=("Times New Roman", 20))
            deathsText.place(x=750,y=250,anchor=tk.CENTER)
            print(stats[3])
            print("hi")
            if stats[3] != '':
                nDeathsD = "New Deaths: " + stats[3]
                nDeathsText = Label(text = nDeathsD) 
                nDeathsText.config(font=("Times New Roman", 20))
                nDeathsText.place(x=750,y=300,anchor=tk.CENTER)    
             
    #Get info for each state from the internet
    def getStateInfo(self,state):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        URL = "https://www.worldometers.info/coronavirus/country/us"
        page = requests.get(URL,headers=headers)
        html = BeautifulSoup(page.content, 'html.parser')  #get page content
        tableData = html.find(id = 'usa_table_countries_today')  #find table 
        content = tableData.find_all('td')  #get table data cells

        i = 0
        check = False
        data = []
        for entries in content:
            t = entries.text.strip()
            if state == t and not check:
                check = True
            if check:
                data.append(entries.text.strip())
                i = i + 1
                if i > 4:
                    break
        #remove state name
        data.pop(0)
        print(data)
        #remove + signs
        data[1] = data[1][1:]
        data[3] = data[3][1:]
        return data
    
    #create main page widgits
    def mainInterface(self):
        #create main page image
        im = "TrakrFace.png"
        self.placeImage(im,450,200)

        #drop down - user selects state from here
        state = tk.StringVar()
        state.set("---")
        drop = tk.OptionMenu(self.root,state,"---","Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming")
        drop.place(x=450,y=450,anchor=tk.CENTER)

        #select button - pressing will send you to desired state info
        buttonCaller = partial(self.changeInterfaceToState,state)
        sel = tk.Button(self.root,text="Select",padx = 10, pady = 5, fg = "white",bg="#691C1C",command = buttonCaller)
        sel.place(x=450,y=400,anchor=tk.CENTER)


t = Tracker()

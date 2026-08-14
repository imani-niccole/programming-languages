# Imani Candler | 11.14.2024
# Programming Languages | Modifying Temp Converter Python
# Objective: Change original Temp Converter program, so that it allows C to F and F to C

import tkinter
import tkinter.messagebox

class TempConverter:
    def __init__(self):
        self.mainWindow = tkinter.Tk() # creates main window

# two frames displayed in main window
        self.topframe = tkinter.Frame(self.mainWindow)
        self.bottomframe = tkinter.Frame(self.mainWindow)

# user's entry label
        self.entryLabel = tkinter.Label(self.topframe, text = "Enter a temperature: ")

# create entry box for entry label in top frame
        self.tempEntry = tkinter.Entry(self.topframe, width = 12)

#pack label and entry box to top frame in main window
        self.entryLabel.pack(side = 'left') # display on left side
        self.tempEntry.pack(side = 'left') # display on left side

# make 3 buttons (2 convert buttons and quit button)
        self.calc1Button = tkinter.Button(self.bottomframe, text = "F to C", command = self.convert)
        self.calc2Button = tkinter.Button(self.bottomframe, text = 'C to F', command = self.convert2)
        self.quitButton = tkinter.Button(self.bottomframe, text = "Quit!", command = self.mainWindow.destroy)

# pack buttons to screen
        self.calc1Button.pack(side = 'left') 
        self.calc2Button.pack(side = 'left')
        self.quitButton.pack(side = 'left')

# pack frames
        self.topframe.pack()
        self.bottomframe.pack()
        tkinter.mainloop() # runs the program


# create function to convert temp values
    def convert(self): # function created
        
    # default value to store conversion temp
        defaultNum = float(self.tempEntry.get()) # value will be used to find either F or C

    # convert fahrenheit to celsius
        celsius = (defaultNum - 32) * (5.00/9.00)

    # display results (F to C)
        tkinter.messagebox.showinfo("Results: ", str(defaultNum) + " Fahrenheit is equal to " + str(celsius) + " Celsius!")  


    def convert2(self): # another convert function created
        defaultNum = float(self.tempEntry.get())

    # convert celsius to fahrenheit
        fahrenheit = (defaultNum * (9.00/5.00)) + 32

    # display results (C to F)
        tkinter.messagebox.showinfo("Results: ", str(defaultNum) + " Celsius is equal to " + str(fahrenheit) + " Fahrenheit!")

# run class TempConverter
tempConvert = TempConverter()



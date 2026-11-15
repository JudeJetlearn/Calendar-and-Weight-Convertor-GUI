from tkinter import *

Screen = Tk()
Screen.title("Weight Converter")
Screen.geometry("800x200")
Screen.config(background = "light grey")

def KgConversion():
    Kg = int(KgEntry.get())

    Grams = Kg * 1000
    Ounce = round(Kg * 35.3, 1)
    Pounds = round(Kg * 2.2, 1)

    GramsEntry.config(state = "normal")
    OunceEntry.config(state = "normal")
    PoundsEntry.config(state = "normal")

    GramsEntry.delete(0,END)
    OunceEntry.delete(0,END)
    PoundsEntry.delete(0,END)

    GramsEntry.insert(0, Grams)
    OunceEntry.insert(0, Ounce)
    PoundsEntry.insert(0, Pounds)

    GramsEntry.config(state = "readonly")
    OunceEntry.config(state = "readonly")
    PoundsEntry.config(state = "readonly")

KgLabel = Label(Screen, text = "Enter Weight (Kg):", background = "light grey", font = "30")
KgLabel.place(x = 75 , y = 25)

KgEntry = Entry(Screen, font = "Arial 20")
KgEntry.place(x = 300 , y = 25)

ConvertButton = Button(Screen, text = "Convert", font = "Arial 15", command = KgConversion)
ConvertButton.place(x = 650 , y = 25)


GramsLabel = Label(Screen, text = "Grams", background = "light grey", font = "Arial 15")
GramsLabel.place(x = 100 , y = 100)

PoundsLabel = Label(Screen, text = "Pounds", background = "light grey", font = "Arial 15")
PoundsLabel.place(x = 350 , y = 100)

OunceLabel = Label(Screen, text = "Ounce", background = "light grey", font = "Arial 15")
OunceLabel.place(x = 600 , y = 100)

GramsEntry = Entry(Screen, font = "Arial 15", state = "readonly")
GramsEntry.place(x = 25 , y = 125)

PoundsEntry = Entry(Screen, font = "Arial 15", state = "readonly")
PoundsEntry.place(x = 275 , y = 125)

OunceEntry = Entry(Screen, font = "Arial 15", state = "readonly")
OunceEntry.place(x = 525 , y = 125)

Screen.mainloop()
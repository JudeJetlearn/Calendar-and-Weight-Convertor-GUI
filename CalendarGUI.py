from tkinter import *
import calendar

Screen = Tk()
Screen.title("Calendar Menu")
Screen.geometry("600x400")
Screen.config(background = "white")

def ShowCalendar():
    CalendarWindow = Tk()
    CalendarWindow.title("Calendar:")
    CalendarWindow.geometry("550x600")
    CalendarWindow.config(background = "white")

    Year = int(YearEntry.get())
    Calendar = calendar.calendar(Year)

    CalendarLabel = Label(CalendarWindow, text = Calendar, font = "Consolas 10")
    CalendarLabel.place(x = 25 , y = 25)

TitleLabel = Label(Screen, text = "CALENDAR", font = "Arial 82", background = "grey")
TitleLabel.place(x = 0 , y = 0)

YearLabel = Label(Screen, text = "Enter Year:", font = "Arial 15", background = "cyan")
YearLabel.place(x = 250 , y = 150)

YearEntry = Entry(Screen, font = "Arial 15", background = "light grey")
YearEntry.place(x = 190 , y = 185)

CalendarButton = Button(Screen,  text = "Show Calendar", font = "Arial 15", background = "green", command = ShowCalendar)
CalendarButton.place(x = 175 , y = 250)

ExitButton = Button(Screen, text = "Exit", font = "Arial 15", background = "red", command = Screen.destroy)
ExitButton.place(x = 375 , y = 250)

Screen.mainloop()
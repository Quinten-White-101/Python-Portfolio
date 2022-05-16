#Quinten White
#christmas countdown

#imports
from tkinter import *
from tkinter.ttk import Style
import datetime

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.date = "12/25/2021"
        self.initUI()

    def initUI(self):
        self.master.title("Countdown clock")
        self.master.geometry("623x372")
        self.pack(fill=BOTH, expand = 1)

        img = PhotoImage(file= "Christmas_card1.png")
        self.bg = Label(self, image = img)
        self.bg.image = img
        self.bg.place(x=0,y=0)
        time = self.time_until(self.date)


        self.cd_lbl = Label(self, text = time, fg = "WHITE",bg="green", font=("helvetica",40))
        self.cd_lbl.place( x=15,y=260)

        self.date_pick_bttn = Button(self, text="Set Date",command=self.setDate,fg="white", bg ="RED", font = ("helvetica",16))
        self.date_pick_bttn.place(x=60,y=326)

        self.moSpinner = Spinbox(self, from_=1, to =12, width=5, font= ("helvetica",16))
        self.moSpinner.place(x=160,y=326)
        self.daySpinner = Spinbox(self, from_=1, to=31, width=5, font=("helvetica", 16))
        self.daySpinner.place(x=240, y=326)
        self.yearSpinner = Spinbox(self, from_=2021, to=2030, width=5, font=("helvetica", 16))
        self.yearSpinner.place(x=320, y=326)

    def setDate(self):
        month = self.moSpinner.get()
        day = self.daySpinner.get()
        year = self.yearSpinner.get()


        self.date = str(month)+"/"+str(day)+"/"+str(year)
        print(self.date)

    def time_until(self, date):
            date = datetime.datetime.strptime(date, "%m/%d/%Y")
            now = datetime.datetime.now()
            if date > now:
                time_until = date - now
                return time_until
            else:
                return now - now





    def update(self):
        textsv = StringVar()
        textsv = self.time_until(self.date)
        self.cd_lbl.config(text = textsv)
        self.master.after(1, self.update)


def main ():
    root = Tk()
    app = Application(root)
    root.after(1,app.update)
    root.mainloop()

main()
#Quinten White
#GUI DEVELOPMENT
#2/10/2022

#IMPORTS
from tkinter import *
from tkinter.ttk import *   # .ttk gives access to the tkinter file
from settings import *
from tkinter import messagebox as mbox
from tkinter import colorchooser as cc
from tkinter import filedialog as fd

class Application(Frame):
    title = "New GUI"
    def __init__(self):
        super(Application, self).__init__()
        self.createMenus()
        self.initUI()


    def clearForm(self):
        #clear the forms to start over
        self.orderName.delete(0, END)
        self.size.set(self.sizeList[4])
        self.veggi_toppings.select_clear(0, END)
        for var in self.meattoppingsvar:
            var.set(False)
        self.crustType.set("Pick Crust")
        self.tipvar.set(0)
    def onExit(self):
        self.quit()
    def readData(selfself,file):
        with open(file, "r")as f:
            name = f.readline().strip("\n")
            size = f.readline().strip("\n")
            veg = f.readline().strip("\n")
            m = f.readline().strip("\n")
            crust = f.readline().strip("\n")
            tip = int(f.readline().strip("\n"))
            vegi = []
            topping = ""

            for i in range(len(veg)):
                if veg[i] != ",":
                    topping += veg[i]
                else:
                    vegi.append(topping)
                    topping("")
            meat = []
            topping = ""
            for i in range(len()):
                if m[i] != ",":
                    topping += m[i]
                else:
                    meat.append(topping)
                    topping("")






        return name,size,vegi,meat,crust,tip



    def loadData(self):
        #load text data from a file
        ftypes = [("Python File", "*.py"), ("Text File", "*.txt"), ("All Files", "*")]
        dlg = fd.Open(self,filetypes=ftypes)
        try:
            file = dlg.show()
        except:
            mbox.showerror("Error", "Issue with that file ")
            if file != "":
                name,size,vegi,meat,crust,tip = self.readData(file)
                data = self.readData(file)
            self.filloutform(name,size,vegi,meat,crust,tip)

    def filloutform(self,name,size,vegi,meat,crust,tip):
        print(name, size, vegi, meat, crust, tip)
        #name = data
        #clear form before filling out
        self.clearForm()
        # insert data into form
        self.orderName.insert(0,self.name)
        for i in range(len(self.sizeList)):
            if size == self.sizeList[i]:
                self.size.set(self.sizeList[i])
            else:
                self.size.set(self.sizeList[4])
        self.size.set(self.sizeList[4])
        selectedIndex = ""

        for i in range(len(vegi)):
            if vegi[i] == self.vegitoppings[i]:
                selectedIndex.append[i]
                for index in selectedIndex:
                    self.vegi_toppings.select_set(index)

        for i in range(len(meat)):
            if meat[i] == self.meattoppings[i]:
                selectedIndex.append(i)
        for index in selectedIndex:
            self.meattoppingsvar[index].set(True)

        for var in self.meattoppingsvar:
            var.set(False)
        self.crustType.set("Pick Crust")
        self.tipvar.set(0)

    def collectData(self):
        name = self.orderName.get()
        if not name:
            mbox.showerror("cant save", "name is required")
        size = self.size.get()
        vegi = []
        selected = self.veggitoppings.curselection()
        print(selected)

        for i in selected:
            x = self.vegi_toppings.get(i)

            vegi.append(x)
            print(vegi)
        meat = []
        for var in self.meattoppingsvar:
            set = var.get()

            if var:
                x = self.meattoppingsvar.index(var)
                topping = self.meattoppings[x]
                meat.append(topping)

        extras = []
        # for var in self.extrasVars:
        # if var:
        # x = self.extrasVars.index(var)
        # ext = self.extrasList[x]
        # extras.append(ext)

        crust = self.crustType.get()

        tip = self.tipvar.get()


        return name, size, vegi, meat, crust, tip



    def saveData(self):
        #collect data from form and set it to write to a file
        name, size, vegi, meat, crust, tip = self.collectData()
        if mbox.askquestion("saving"," Are you sure you want to save this order") == "yes":


            try:
                file = open("pizza_order_"+name+".txt", "w")
                file.write(name+"\n")
                file.write(size+"\n")

                file.write(str(vegi))
                file.write("\n")
                file.write(str(meat))
                file.write("\n")
                #file.write(str(extras))
                file.write("\n")
                file.write(crust+"\n")
                file.write(str(tip)+"\n")
                file.close()
            except:
                mbox.showerror("error", "something went wrong and order was not saved ")

            self.onExit()

    def orderPizza(self,pizza):
        self.clearForm
        if pizza == "pep":
            print("you ordered a Pepperoni")
            self.size.set(self.sizeList[4])
           # self.checkbuttonlist[0].state(["selected"])
            self.meattoppingsvar[0].set(True)
            self.crustType.set(self.crustList[5])
            self.tipvar.set[15]
        elif pizza == "meat":
            print("You ordered a meat lover")
            self.size.set(self.sizeList[4])
            for topping in self.meattoppingsvar:
                topping.set(True)
            self.crustType.set(self.crustList[5])
            self.tipvar.set(15)
        elif pizza == "veg":
            print("You ordered a veggie lover")
            self.size.set(self.sizeList[0])
            self.crustType.set(self.crustList[0])
            self.tipvar.set(25)
            for i in range(len(self.veggitoppings)):
                self.veggi_toppings.select_set(i)


    #def location(self,location):
       # if location == "G":
            #mbox.showinfo("Grantsville Loacation", "Address: 123 main \nPhone: 435 884 1234 \nHours 10 am to 10 pm ")
        #elif location == "S"
           # mbox.showwarning("Stansbury Loacation", "Address:456 millpond \nPhone:435 679 6543 \nHours 10 am to 10 pm")
       # elif location == "T"
            #mbox.showerror("Tooele Loacation", "Address:647 vine  \nPhone: 435 697 4004 \nHours 10 am to 10 pm")

    def help(self):
        if mbox.askquestion("Help Really", "Do you really need help")== "yes":
            mbox.showerror("Error", "We dont want your order then ")
        self.quit()

    def colorChange(self):
        rgb, hx = cc.askcolor()

        self.style.configure("TLabel",background = hx)
        self.style.configure("TFrame",background = hx)

        self.style.configure("TRadioButtons", background=hx)


    def createMenus(self):
        #setup of mai top level cascade
        self.mainMenu = Menu(self)
        self.file_Menu= Menu(self.mainMenu)
        self.edit_Menu = Menu(self.mainMenu)
        self.view_Menu = Menu(self.mainMenu)
        self.help_Menu = Menu(self.mainMenu)
        self.view_loc = Menu(self.mainMenu)
        self.cur_store = Menu(self.mainMenu)



        self.mainMenu.add_cascade(label = "file", menu = self.file_Menu)
        self.mainMenu.add_cascade(label = "Edit", menu = self.edit_Menu)
        self.mainMenu.add_cascade(label = "View", menu = self.view_Menu)
        self.mainMenu.add_cascade(label = "Help", menu = self.help_Menu)
        self.mainMenu.add_cascade(label = "Stores", menu = self.view_loc)


        #setting up file cascade
        self.file_Menu.add_command(label = "New", command = self.clearForm)
        self.file_Menu.add_command(label = "Load", command = self.loadData)
        self.file_Menu.add_command(label = "Save", command = self.saveData)


        #setup edit menu
        self.edit_Menu.add_command(label = "Pepperoni", command = lambda: self.orderPizza("pep"))
        self.edit_Menu.add_command(label="Meat lover", command=lambda: self.orderPizza("meat"))
        self.edit_Menu.add_command(label="veggie lover", command=lambda: self.orderPizza("veg"))
        self.view_Menu.add_command(label = "change Color", command = self.colorChange)
        #setup help
        self.help_Menu.add_command(label="Help", command = self.help)





        self.master.config(menu = self.mainMenu)





    def initUI(self):
        self.master.title(Application.title)
        self.style = Style()
        self.style.theme_use(theme)






        Label(self,text = "Order Name:").grid(row = 0, column = 0, sticky = "W")
        self.orderName = Entry(self, width = 40)
        self.orderName.grid(row = 0, column = 1, columnspan = 4, sticky = "E", padx = 5)

        Label(self, text = "Choose Size").grid(row = 1, column = 2)

        self.size = StringVar()
        self.sizeList = ["Small", "Medium", "Large", "XLarge", "Family"]
        self.size.set(self.sizeList[4])
        self.radioBttnList = []


        for size in self.sizeList:
            x = Radiobutton(self, text = size,variable = self.size, value = size )
            self.radioBttnList.append(x)
        for i in range(len(self.radioBttnList)):
            self.radioBttnList[i].grid(row = 2, column = i)

        Label(self, text = "select toppings").grid(row = 3)
        self.veggi_toppings = Listbox(self, selectmode = "multiple")
        self.veggitoppings = ["cheese", "pineapple", "Mushrooms", "pepper", "olives"]
        self.meattoppings = ["pepperoni","sausage","ham", "anchoivi", "chicken", "bacon", "BBQ sauce", "beef", "salami", "turkey", "Pork", "steak"]
        num = 1
        for topping in self.veggitoppings:

            self.veggi_toppings.insert(num, topping)
            num += 1
        self.veggi_toppings.grid(row = 4, columnspan = 2, rowspan = 4 )
        self.checkbuttonlist = []
        self.meattoppingsvar = []
        for i in range(len(self.meattoppings)):
            var = BooleanVar()
            self.meattoppingsvar.append(var)
        for i in range(len(self.meattoppings)):
            x = Checkbutton(self, text = self.meattoppings[i], variable = self.meattoppingsvar[i])
            self.checkbuttonlist.append(x)
        item = 0

        for row in range(4):
            for col in range(3):
                self.checkbuttonlist[item].grid(row =row+5,column = col+2, sticky = "W")
                item += 1

        Label(self, text ="extras").grid()
        Label(self, text = "extras in this row").grid(row = 9)
        Label(self, text = "crsut type").grid(row = 10)
        self.crustList = ["thin", "pan", "stuffed", "deep dish", "none", "Hand tossed"]
        self.crustType = Combobox(self,values = self.crustList)
        self.crustType.set("pick crust")
        self.crustType.grid(row = 11)

        self.tipScale = Scale(self,from_=0, to = 100, orient = HORIZONTAL)
        self.tipScale.grid(row=12, columnspan = 5)

        Label(self, text = "Tip %").grid(row =12)
        self.orderBttn = Button(self, text = "Place Order", command = self.order)
        self.orderBttn.grid(row = 13, column = 4, columnspan = 3)

        self.tipvar = IntVar()
        self.tipvar.set(0)
        self.tipScale = Scale(self, orient = HORIZONTAL, from_=0, to = 100, variable = self.tipvar, length = 150)
        self.tipScale.grid(row = 13, column = 0, columnspan = 2, rowspan = 2)





        self.pack(fill = BOTH, expand=1)
        self.centerWindow()

    def order(self):
        master = Tk()
        master.geometry("300x300")

    def topping_price(self):
        #self.veggi_toppings =
        pass






    def centerWindow(self):
        w = WIDTH
        h = HEIGHT

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.master.geometry("%dx%d+%d+%d" %(w,h,x,y))



    def __change_Title__(title):
        Application.title = title



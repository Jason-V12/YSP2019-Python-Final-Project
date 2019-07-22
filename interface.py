from tkinter import *
from tkinter.filedialog import askopenfilename

class DrawInterface(object):
    #param (none)
    def __init__(self):
        self.top = Tk()
        self.top.geometry("400x500+0+0")
        self.top.title("Spellchecker Upload Screen")
        self.choosefileimage = PhotoImage(file = "choosefile.gif")
        self.exitimage = PhotoImage(file = "exitimage.gif")
        self.browseimage = PhotoImage(file = "browseimage.gif")
        self.chosenimage = PhotoImage(file = "filechosen.gif")
        self.restartimage = PhotoImage(file = "restartimage.gif")
        self.englishimage = PhotoImage(file = "englishimage.gif")
        self.spanishimage = PhotoImage(file = "spanishimage.gif")
        self.frenchimage = PhotoImage(file = "frenchimage.gif")
        self.germanimage = PhotoImage(file = "germanimage.gif")
        self.currentlangimage = PhotoImage(file = "currentlanguageimage.gif")
        self.logoimage = PhotoImage(file = "logo.gif")
        self.language = "English"
        self.file = None
        self.file_location = ""
    #param (none)
    def make_interface(self):
        logolbl = Label(self.top, height = 167, width = 324, image = self.logoimage)
        logolbl.place(x = 38, y = 0)
        exitbtn = Button(self.top, height = 40, width = 100, image = self.exitimage, command = self.exit_interface)
        exitbtn.place(x = 300, y = 460)
        filelbl = Label(self.top, height = 40, width = 150, image = self.choosefileimage)
        filelbl.place(x = 0, y = 200)
        fileChoosebtn = Button(self.top, height = 40, width = 75, image = self.browseimage, command = self.upload_file)
        fileChoosebtn.place(x = 150, y = 200)
        restartbtn = Button(self.top, height = 40, width = 100, image = self.restartimage, command = self.make_interface)
        restartbtn.place(x = 200, y = 460)
        englishbtn = Button(self.top, height = 40, width = 150, image = self.englishimage, command = lambda: self.change_language(1))
        englishbtn.place(x = 0, y = 250)
        spanishbtn = Button(self.top, height = 40, width = 150, image = self.spanishimage, command = lambda: self.change_language(2))
        spanishbtn.place(x = 0, y = 300)
        frenchbtn = Button(self.top, height = 40, width = 150, image = self.frenchimage, command = lambda: self.change_language(3))
        frenchbtn.place(x = 0, y = 350)
        germanbtn = Button(self.top, height = 40, width = 150, image = self.germanimage, command = lambda: self.change_language(4))
        germanbtn.place(x = 0, y = 400)
        currentlanglbl = Label(self.top, height = 40, width = 200, image = self.currentlangimage)
        currentlanglbl.place(x = 200, y = 310)
    #param (none)
    def exit_interface(self):
        self.top.destroy()
    def exit_typescreen(self):
        self.filedir = self.fileEntry.get()
        self.typescreen.destroy()
        print(self.filedir)
    #param (none)
    def upload_file(self):
        self.file = askopenfilename(title = "Choose a file:", filetypes = (("Text File", "*.txt"))
        try:
            filedir = open(self.file)
            filedir.read()
            filedir.close()
            filelbl = Label(self.top, height = 40, width = 150, image = self.chosenimage)
            filelbl.place(x = 0, y = 200)
            self.file_location = str(filedir).split("\'")[1].replace("/", "\\")
        except:
            if self.file == None:
                print("Try again")
    def change_language(self, langnum):
        if langnum == 1:
            language = "English"
            self.language = "English"
            self.curlang = Label(self.top, height = 40, width = 150, image = self.englishimage)
        elif langnum == 2:
            language = "Spanish"
            self.language = "Spanish"
            self.curlang = Label(self.top, height = 40, width = 150, image = self.spanishimage)
        elif langnum == 3:
            language = "French"
            self.language = "French"
            self.curlang = Label(self.top, height = 40, width = 150, image = self.frenchimage)
        elif langnum == 4:
            language = "German"
            self.language = "German"
            self.curlang = Label(self.top, height = 40, width = 150, image = self.germanimage)
        self.curlang.place(x = 200, y = 360)

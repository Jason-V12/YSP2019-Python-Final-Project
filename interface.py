"""Creates a graphical user interface and handles input."""
from tkinter import *
from tkinter.filedialog import askopenfilename

class Language(object):
    #param (self, string)
    def __init__(self, language):
        lang = self.language
        #dictionary for language

class DrawInterface(object):
    #param (none)
    def __init__(self):
        self.top = Tk()
        self.top.geometry("400x600+0+0")
        self.choosefileimage = PhotoImage(file = "choosefile.gif")
        self.exitimage = PhotoImage(file = "exitimage.gif")
        self.browseimage = PhotoImage(file = "browseimage.gif")
        self.file = None
    #param (none)
    def make_interface(self):
        exitbtn = Button(self.top, height = 40, width = 100, image = self.exitimage, command = self.exit_interface)
        exitbtn.place(x = 300, y = 560)
        filelbl = Label(self.top, height = 55, width = 150, image = self.choosefileimage)
        filelbl.place(x = 0, y = -5)
        filebtn = Button(self.top, height = 40, width = 75, image = self.browseimage, command = self.upload_file)
        filebtn.place(x = 150, y = 0)
        #restartbtn = Button(self.top, height = 40, width = 100, text = "Restart", command = self.make_interface)
        #restartbtn.place(x = 300, y = 0)
    #param (none)
    def exit_interface(self):
        self.top.destroy()
    #param (none)
    def upload_file(self):
        while self.file == None:
            self.file = askopenfilename(title = "Choose a file:")
        try:
            with open(self.file, "r") as UseFile:
                filetext = self.file.read()
                self.file.close()
        except:
            self.file = None
            print("No such file exists")


x = DrawInterface()
x.make_interface()

# Note: PyQt or Tkinter

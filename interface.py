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
        self.chosenimage = PhotoImage(file = "filechosen.gif")
        self.restartimage = PhotoImage(file = "restartimage.gif")
        self.file = None
        self.file_location = None
    #param (none)
    def make_interface(self):
        exitbtn = Button(self.top, height = 40, width = 100, image = self.exitimage, command = self.exit_interface)
        exitbtn.place(x = 300, y = 560)
        filelbl = Label(self.top, height = 40, width = 150, image = self.choosefileimage)
        filelbl.place(x = 0, y = 0)
        fileChoosebtn = Button(self.top, height = 40, width = 75, image = self.browseimage, command = self.upload_file)
        fileChoosebtn.place(x = 155, y = 0)
        restartbtn = Button(self.top, height = 40, width = 100, image = self.restartimage, command = self.make_interface)
        restartbtn.place(x = 300, y = 0)
    #param (none)
    def exit_interface(self):
        self.top.destroy()
    #param (none)
    def upload_file(self):
        self.file = askopenfilename(title = "Choose a file:", filetypes = (("Text File", "*.txt"), ("PDF File","*.pdf"), ("Microsoft Word Document", "*.doc*")))
        try:
            filetext = open(self.file)
            filetext.read()
            self.file_location = str(filetext).split("\'")[1]
            filetext.close()
            filelbl = Label(self.top, height = 40, width = 150, image = self.chosenimage)
            filelbl.place(x = 0, y = 0)
        except:
            print("Try again")
        print(self.file_location)


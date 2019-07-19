from tkinter import *
from tkinter.filedialog import askopenfilename


class DrawInterface(object):
    # param (none)
    def __init__(self):
        self.top = Tk()
        self.top.geometry("400x300+0+0")
        self.top.title("Spellchecker Upload Screen")
        self.choosefileimage = PhotoImage(file="choosefile.gif")
        self.exitimage = PhotoImage(file="exitimage.gif")
        self.browseimage = PhotoImage(file="browseimage.gif")
        self.chosenimage = PhotoImage(file="filechosen.gif")
        self.restartimage = PhotoImage(file="restartimage.gif")
        self.englishimage = PhotoImage(file="englishimage.gif")
        self.spanishimage = PhotoImage(file="spanishimage.gif")
        self.frenchimage = PhotoImage(file="frenchimage.gif")
        self.germanimage = PhotoImage(file="germanimage.gif")
        self.currentlangimage = PhotoImage(file="currentlanguageimage.gif")
        self.file = None
        self.file_location = ""

    # param (none)
    def make_interface(self):
        exitbtn = Button(self.top, height=40, width=100, image=self.exitimage, command=self.exit_interface)
        exitbtn.place(x=300, y=260)
        filelbl = Label(self.top, height=40, width=150, image=self.choosefileimage)
        filelbl.place(x=0, y=0)
        fileChoosebtn = Button(self.top, height=40, width=75, image=self.browseimage, command=self.upload_file)
        fileChoosebtn.place(x=150, y=0)
        restartbtn = Button(self.top, height=40, width=100, image=self.restartimage, command=self.make_interface)
        restartbtn.place(x=300, y=0)
        englishbtn = Button(self.top, height=40, width=150, image=self.englishimage,
                            command=lambda: self.change_language(1))
        englishbtn.place(x=0, y=50)
        spanishbtn = Button(self.top, height=40, width=150, image=self.spanishimage,
                            command=lambda: self.change_language(2))
        spanishbtn.place(x=0, y=100)
        frenchbtn = Button(self.top, height=40, width=150, image=self.frenchimage,
                           command=lambda: self.change_language(3))
        frenchbtn.place(x=0, y=150)
        germanbtn = Button(self.top, height=40, width=150, image=self.germanimage,
                           command=lambda: self.change_language(4))
        germanbtn.place(x=0, y=200)
        currentlanglbl = Label(self.top, height=40, width=200, image=self.currentlangimage)
        currentlanglbl.place(x=200, y=110)

    # param (none)
    def exit_interface(self):
        self.top.destroy()

    # param (none)
    def upload_file(self):
        self.file = askopenfilename(title="Choose a file:", filetypes=(
        ("Text File", "*.txt"), ("PDF File", "*.pdf"), ("Microsoft Word Document", "*.doc*")))
        try:
            filedir = open(self.file)
            filedir.read()
            filedir.close()
            self.file_location = str(filedir).split("\'")[1].replace("/", "\\")
            filelbl = Label(self.top, height=40, width=150, image=self.chosenimage)
            filelbl.place(x=0, y=0)
        except:
            print("Try again")
        print(filedir)

    def change_language(self, langnum):
        if langnum == 1:
            language = "English"
            self.curlang = Label(self.top, height=40, width=150, image=self.englishimage)
        elif langnum == 2:
            language = "Spanish"
            self.curlang = Label(self.top, height=40, width=150, image=self.spanishimage)
        elif langnum == 3:
            language = "French"
            self.curlang = Label(self.top, height=40, width=150, image=self.frenchimage)
        elif langnum == 4:
            language = "German"
            self.curlang = Label(self.top, height=40, width=150, image=self.germanimage)
        self.curlang.place(x=200, y=160)
        
x = DrawInterface()
x.make_interface()


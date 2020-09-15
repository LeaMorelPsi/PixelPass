import tkinter as tk
from tkinter import ttk
import Collection
import GenPass


class PixelPass():
    def __init__(self):

        #! Main window

        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.resizable(width=False, height=False)
        self.root.title("Pixel.Pass")
        self.root.configure(bg="black")

        ################################################

        #! Password image label

        self.passImgPath = tk.StringVar()
        self.passImgLabel = tk.ttk.Label(
            self.root, textvariable=self.passImgPath, font=("Arial", 16), foreground="white", background="black")
        self.passImgPath.set("Select password image source")

        ##########################################################################

        #! Password image button

        self.passImgBtn = tk.ttk.Button(self.root, text="Password image", command=(
            lambda: [Collection.getContext(), self.changePassPath(), self.changeMax(), self.changePass(GenPass.desiredLength, self.onOrOff.get())]))

        #############################################################################################################

        #! Desired length label

        self.desiredLengthLabel = tk.ttk.Label(
            self.root, text="Enter password length:", font=("Arial", 20), foreground="white", background="black")

        ################################################################################

        #! Maximum password length label

        self.maxLengthText = tk.StringVar()
        self.maxLengthLabel = tk.ttk.Label(
            self.root, textvariable=self.maxLengthText, font=("Arial", 12), foreground="white", background="black")

        ##############################################################################

        #! Desired password length entry

        self.desLengthEntry = tk.ttk.Entry(
            self.root, width=6, font=("Arial", 16), justify="center")
        self.desLengthEntry.bind('<KeyRelease>', self.lengthBind)

        #######################################################################

        #! Outputted password label

        self.passLabel = tk.ttk.Label(self.root, font=(
            "Arial", 24), justify="center", text="Password:", foreground="white", background="black")

        ##############################################################################################

        #! Outputted password entry

        self.passText = tk.Text(self.root, height=1)
        self.passText.configure(
            inactiveselectbackground=self.passText.cget("selectbackground"))

        ###############################################################################################

        #! Special characters label

        self.specCharsLabel = tk.ttk.Label(
            self.root, text="Special characters:", font=("Arial", 16), foreground="white", background="black")

        #! Special characters option

        self.onOrOff = tk.BooleanVar()
        self.specialCharacters = tk.Checkbutton(self.root, variable=self.onOrOff, command=self.specChars,
                                                background="black", bd=0, highlightthickness=0, activebackground="black", activeforeground="white")

        ##########################################################################################

        #! Pack widgets

        self.passImgLabel.pack(pady=10)
        self.passImgBtn.pack()
        self.desiredLengthLabel.pack(pady=10)
        self.maxLengthLabel.pack()
        self.desLengthEntry.pack(pady=20)
        self.specCharsLabel.pack()
        self.specialCharacters.pack(pady=8)
        self.passLabel.pack()
        self.passText.pack()

        ################################

        #! Main loop

        self.root.mainloop()

        ########################

    # Updates the outputted password with the password gen function output
    def changePass(self, length, specialChars):
        if self.passText:
            self.passText.delete(1.0, tk.END)
            try:
                self.passText.insert(1.0, GenPass.genPass(
                    Collection.passMaxLength, length, self.onOrOff.get()), tk.END)
            except tk.TclError:
                return False
        else:
            self.passText.insert(1.0, GenPass.genPass(
                Collection.passMaxLength, length), tk.END)

    # Updates the password image file path label
    def changePassPath(self):
        self.passImgPath.set(Collection.passImgPath)

    def changeMax(self):
        self.maxLengthText.set(
            "(Maximum password length: " + str(Collection.passMaxLength) + ")")

    def lengthBind(self, event):
        newLength = self.desLengthEntry.get()
        try:
            GenPass.desiredLength = int(newLength)
            return self.changePass(GenPass.desiredLength, self.onOrOff.get())
        except ValueError:
            return False

    def specChars(self):
        self.passText.delete(1.0, tk.END)
        self.passText.insert(1.0, GenPass.genPass(
            Collection.passMaxLength, self.desLengthEntry.get(), self.onOrOff.get()), tk.END)


app = PixelPass()

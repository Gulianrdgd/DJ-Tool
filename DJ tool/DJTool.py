from tkinter import *
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


totalaction = 0
keuze =0
geslaagd = 0


root = Tk()
root.title("Automatic DJ Tool")
path =  filedialog.askdirectory(initialdir = "/",title = "Select folder")


mp3 = tk.IntVar()
my = tk.IntVar()
spatie = tk.IntVar()
keuze = tk.IntVar()
clan = tk.IntVar()
v = StringVar()

def dagmyfreemp3():
    global totalaction
    global geslaagd
    print("dag my")
    totalaction +=1
    os.chdir(path)
    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("www.myfreemp3.click","")))

        except:
            os.rename(f, f + "(1)")

    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("www.myfreemp3.space","")))

        except:
            os.rename(f, f + "(1)")

    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("www.my-free-mp3.club","")))

        except:
            os.rename(f, f + "(1)")

    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("www.my-free-mp3.net ","")))

        except:
            os.rename(f, f + "(1)")

    geslaagd +=1


def dagmp3clan():
    print("dag mp3xclan")
    global geslaagd
    global totalaction
    totalaction += 1
    os.chdir(path)
    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("[mp3clan]","")))

        except:
            os.rename(f, f + "(1)")

    geslaagd += 1


def dagmp3fiber():
    print("dag fiber")
    global geslaagd
    global totalaction
    totalaction += 1
    os.chdir(path)
    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("[www.MP3Fiber.com]","")))

        except:
            os.rename(f, f + "(1)")

    geslaagd += 1


def dagspatie():
    print("dag spatie")
    global geslaagd
    global totalaction
    totalaction += 1
    os.chdir(path)
    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace("_"," ")))

        except:
            os.rename(f, f + "(1)")
    geslaagd += 1



def dagkeuze():
    print("dag keuze")
    global geslaagd
    userold=v.get()
    global totalaction
    totalaction += 1
    os.chdir(path)

    for f in os.listdir(path):
        try:
            os.rename(os.path.join(path, f),
            os.path.join(path, f.replace(userold,"")))
        except:
            os.rename(f,f + "(1)")

    geslaagd += 1


def dagkeuzemisschien():
    userold=v.get()
    print(userold)
    if len(userold) == 0:
        return
    else:
        dagkeuze()



def start():

    dagkeuzemisschien()

    if my.get()==1:
        dagmyfreemp3()
    if mp3.get()==1:
        dagmp3fiber()
    if spatie.get()==1:
        dagspatie()

    if clan.get()==1:
        dagmp3clan()



    messagebox.showinfo("After action report", str(geslaagd)+"/"+str(totalaction)+" Geslaagd")


Banner= PhotoImage(file="Banner.png")
ban= Label(root, image=Banner).grid(rowspan=4, columnspan=3)

pasop = Label(root, text="Pas op als je deze software toepast op al ingeladen mp3's in je DJ Software, kan de software deze Mp3's niet meer vinden \n en zult u ze weer opnieuw in moeten laden.", bg="white", fg="black").grid(row=2, column=0, columnspan=4)


check1= Checkbutton(root, text= "myfreeMp3", variable=my, onvalue=1,offvalue=0).grid(row=5, column=0, sticky=W, padx=185)
check2= Checkbutton(root, text= "Mp3Fiber", variable=mp3, onvalue=1,offvalue=0).grid(row=6, column=0, sticky=W, padx=185)
check3= Checkbutton(root, text= "Spatie's", variable=spatie, onvalue=1,offvalue=0).grid(row=7, column=0, sticky=W, padx=185)

check4= Checkbutton(root, text= "mp3clan", variable=clan, onvalue=1,offvalue=0).grid(row=5, column=1)
entry = Entry(root, state= tk.NORMAL, textvariable=v).grid(row=6, column=1)
userold=v.get()
nex= Button(root, text="Next", command=start).grid(row=7, column=1)


root.mainloop()

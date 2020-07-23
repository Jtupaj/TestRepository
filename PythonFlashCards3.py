from tkinter import *
from tkinter import messagebox
import random

#This is the help popup
def popupHelp ():
    messagebox.showinfo("Need Help?", "Press the start button to generate a number, then type your answer in the box and click check answer. Use the buttons on the bottom to chainge the min. And max. Numbers for the equasion.")
    #myLabel.grid(row=1, column=4)


root = Tk()
root.title("FlashCards")
root.iconbitmap("c:/Users/jtupa/Downloads/hnet.com-image.ico")
#myLabel = help button(disabled)
#myLabel = Button(root, text="Press the start button to generate a number, then type your answer in the box and click check answer", fg="gray")
textvar = StringVar()
varx = StringVar()
vary = StringVar()
labelx = Label(root, textvariable=varx, anchor="e", width=10)
labelx.grid(row=6,column=1)
labely = Label(root, textvariable=vary, anchor="e", width=10)


labely.grid(row=7,column=1)
resultLabel = Label(root, textvariable=textvar)
resultLabel.grid(row=8,column=1)

#this controls the size of the flash card box
root.geometry("608x280")

def myClickClear():
    #myLabel.grid_forget()
    answerBox.grid_forget()
    varx.set("")
    vary.set("")

def destroy():
    answer1.config(text=" ")

x = 0
y = 0

#z is the variable im using for my equasion tracker
global z
z=IntVar
z = 0

#This is the "correct"/"incorrect"
def checkAnswer():
    global z
    try:
        result = int(answerBox.get())
        if result==x+y:
            answer1.config(text="Coooorect!")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
            z=z + 1
            
           
        else:
            answer1.config(text="incorrect.")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
            z=z+1

    except ValueError:
        answer1.config(text="Type in a number")
        answer1.after(3000, destroy)

    
def statusNumber1():
    text=str(x)
    


answerBox = Entry(root, text="Enter your answer here.", validatecommand=checkAnswer)

bottom = IntVar()
top = IntVar()

#startBox makes the entry(Entry) appear after you press the start button
def startButton():
    answer1.config(text=" ")
    global x
    global bottom
    global top
    global y
    y = random.randint(bottom.get(),top.get())
    vary.set("+" + str(y))
    x = random.randint(bottom.get(),top.get())
    varx.set(" " + str(x))
    answerBox.grid(row=5, column=1)
    
    #textvar.set(x+y)
    

answer = Entry(root)




#This are the min addend max addend radiobuttons
Radiobutton(root, text="Max addend: 100", variable=top, value=100).grid(row=13, column=1)
Radiobutton(root, text="Max addend: 1000", variable=top, value=1000).grid(row=13, column=2)
Radiobutton(root, text="Max addend: 10,000", variable=top, value=10000).grid(row=13, column=3)

Radiobutton(root, text="Min addend: 0", variable=bottom, value=0).grid(row=12, column=1)
Radiobutton(root, text="Min addend: 100", variable=bottom, value=100).grid(row=12, column=2)
Radiobutton(root, text="Min addend: 1000", variable=bottom, value=1000).grid(row=12, column=3)

#top and botton are parts of x and y im  using for my radio buttons
top.set(100)
bottom.set(0)

#these are more buttons and labels
helpButton = Button(root, text="HELP", command=popupHelp, borderwidth=2, padx=30, pady=10, fg="orange", bg="gray32")
helpButton.grid(row=1, column=1)

buttonClear = Button(root, text="CLEAR", command=myClickClear, borderwidth=2, padx=30, pady=10, fg="blue", bg="gray32")
buttonClear.grid(row=1, column=3)

buttonStart = Button(root, text="START", command=startButton, borderwidth=2, padx=30, pady=10, fg="black", bg="gray32")
buttonStart.grid(row=3, column=1)

buttonQuit = Button(root, text="QUIT", command=root.quit, borderwidth=2, padx=30, pady=10, fg="black", bg="gray20")
buttonQuit.grid(row=3, column=3)

answer1 = Label(root, text=" ",)
answer1.grid(row=8, column=1)

checkAnswer = Button(root, text="CHECK ANSWER", command=checkAnswer, bg="gray20", borderwidth=6 )
checkAnswer.grid(row=5, column=3)



status = Label(root, text = "you have completed " +str(z)+" equations")
status.grid(row=14, column=1)


#Title
title = Label(root, text="Flash Cards", padx=150, pady=10, fg="gray15", bg="LavenderBlush3")
title.grid(row=1, column=2)

#Changes the background color
root.configure(background='gray27')

#Makes the window unresizable
root.resizable(0,0)

root.mainloop()



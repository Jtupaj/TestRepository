from tkinter import *
from tkinter import messagebox
import random
import tkinter.font as font


#Ive commented out winTracker while I figure out what the bug is


#This is the help popup
def popupHelp ():
    messagebox.showinfo("Need Help?", "Press the START button to generate a number, then type your answer in the box and click check answer, if you want even more of a challenge press START MULT to get a multiplication equation, or try START SUB for a subtraction equation. Use the buttons on the bottom to change the min. And max. Numbers for the equation.")
    #myLabel.grid(row=1, column=4)

    #This is the Icon
root = Tk()
root.title("fc")
root.iconbitmap("c:/Users/jtupa/Downloads/hnet.com-image.ico")

#C = Canvas(root, bg="blue", height=250, width=300)
#This is the background image
background_image = PhotoImage(file = "c:\\Users\\jtupa\\Downloads\\BG2.png").zoom(1, 1)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#C.pack()

#myLabel = help button(disabled)
varx = StringVar()
vary = StringVar()
labelx = Label(root, textvariable=varx, anchor="e", width=10)
labelx.grid(row=8,column=1)
labely = Label(root, textvariable=vary, anchor="e", width=10)

#myLabel = Button(root, text="Press the start button to generate a number, then type your answer in the box and click check answer", fg="gray")
textvar = StringVar()

labely.grid(row=9,column=1)
resultLabel = Label(root, textvariable=textvar)
resultLabel.grid(row=10,column=1)

#this controls the size of the flash card box
root.geometry("735x400")



def destroy():
    answer1.config(text=" ")

#winTracker = 0

x = 0
y = 0

# is the variable im using for my equation tracker
answerTracker = 0

#This is the "correct"/"incorrect" (for addition, subtraction and multiplication)
def checkAnswer():
    global answerTracker, completedString
    try:
        result = int(answerBox.get())
        if result==x+y:
            answer1.config(text="Coooorect!")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
            answerTracker=answerTracker + 1
            #winTracker=winTracker + 1
            completedString.set("you have completed " +str(answerTracker)+" equations")
        elif result==x*y:
            answer1.config(text="coooorect!")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
            answerTracker=answerTracker + 1
            #winTracker=winTracker + 1
            completedString.set("you have completed " +str(answerTracker)+" equations")
        elif result==x-y:
            answer1.config(text="coooorect!")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
            answerTracker=answerTracker + 1
            #winTracker=winTracker + 1
            completedString.set("you have completed " +str(answerTracker)+" equations")
        else:
            answer1.config(text="incorrect.")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
            answerTracker=answerTracker + 1
            completedString.set("you have completed " +str(answerTracker)+" equations")

    except ValueError:
        answer1.config(text="Type in a number")
        answer1.after(3000, destroy)

        



    
def statusNumber1():
    text=str(x)
    


answerBox = Entry(root, text="Enter your answer here.", validatecommand=checkAnswer)

bottom = IntVar()
top = IntVar()

#startBox makes the entry(Entry) appear after you press the start button (for addition subtraction and multiplication)
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
    answerBox.grid(row=7, column=1)

    #multiplication
def startButtonMult():
    answer1.config(text=" ")
    global x
    global bottom
    global top
    global y
    y = random.randint(bottom.get(),top.get())
    vary.set("×" + str(y))
    x = random.randint(bottom.get(),top.get())
    varx.set(" " + str(x))
    answerBox.grid(row=7, column=1)

    #subtraction
def startButtonSub():
    answer1.config(text=" ")
    global x
    global bottom
    global top
    global y
    y = random.randrange(0, top.get)
    vary.set("-" + str(y))
    x = random.randrange(0, y)
    varx.set(" " + str(x))
    answerBox.grid(row=7, column=1)
    



    
    #textvar.set(x+y)
    #Heres the thing that checks if the minimum is larger than the max number
answer = Entry(root)

def fixup():
    if top.get() < bottom.get():
        prevTop = top.get()
        top.set(bottom.get())
        bottom.set(prevTop)


#This are the min addend max addend radiobuttons
mn10 = Radiobutton(root, text="Max number: 10", variable=top, command=fixup, value=10).grid(row=13, column=1)
mn100 = Radiobutton(root, text="Max number: 100", variable=top, command=fixup, value=100).grid(row=13, column=2)
mn1000 = Radiobutton(root, text="Max number: 1000", variable=top,command=fixup, value=1000).grid(row=13, column=3)

mx1 = Radiobutton(root, text="Min number: 1", variable=bottom, value=1).grid(row=12, column=1)
mx10 = Radiobutton(root, text="Min number: 10", variable=bottom, command=fixup, value=10).grid(row=12, column=2)
mx100 = Radiobutton(root, text="Min number: 100", variable=bottom, command=fixup, value=100).grid(row=12, column=3)

def startButtonSub():
    answer1.config(text=" ")
    global x
    global bottom
    global top
    global y
    x = random.randrange(bottom.get(), top.get())
    y = random.randrange(bottom.get(), x)
    varx.set(" " + str(x))
    vary.set("-" + str(y))
    answerBox.grid(row=7, column=1)

#top and botton are parts of x and y im  using for my radio buttons
top.set(100)
bottom.set(1)

#this is the clear button (function)
def myClickClear():
    answerBox.grid_forget()
    varx.set("")
    vary.set("")





  
            




#these are more buttons and labels
columnLabel = Label(root, text="   ", bg="gray27")

helpButton = Button(root, text="HELP", command=popupHelp, borderwidth=2, padx=30, pady=10, fg="orange", bg="gray32")
helpButton.grid(row=1, column=1)

buttonClear = Button(root, text="CLEAR", command=myClickClear, borderwidth=2, padx=30, pady=10, fg="blue", bg="gray32")
buttonClear.grid(row=1, column=3)

buttonStart = Button(root, text="START ADD", command=startButton, borderwidth=2, padx=8, pady=5, fg="black", bg="gray32")
buttonStart.grid(row=3, column=1)

buttonStartMult = Button(root, text="START MULT", command=startButtonMult, borderwidth=2, padx=5, pady=5, fg="black", bg="gray32")
buttonStartMult.grid(row=4, column=1)

buttonStartSub = Button(root, text="START SUB", command=startButtonSub, borderwidth=2, padx=5, pady=5, fg="black", bg="gray32")
buttonStartSub.grid(row=5, column=1)

buttonQuit = Button(root, text="QUIT", command=root.quit, borderwidth=2, padx=30, pady=10, fg="black", bg="gray32")
buttonQuit.grid(row=3, column=3)

answer1 = Label(root, text=" ",)
answer1.grid(row=10, column=1)

checkAnswer = Button(root, text="CHECK ANSWER", command=checkAnswer, bg="gray23", borderwidth=6 )
checkAnswer.grid(row=6, column=3, columnspan=2)

#winTracker = Label(root, text="You have gotten " +str(winTracker)+ " equations correct") 
#winTracker.grid(row=14, column=1)

completedString = StringVar()
status = Label(root, textvariable = completedString)
status.grid(row=15, column=1)

#Changes the title font
myFont = font.Font(family='FreeMono')
#Title
title = Label(root, text="Flash Cards", padx=150, pady=10, fg="gray80", bg="gray32")
title.grid(row=1, column=2)
title['font'] = myFont
#Changes the background color
root.configure(background='gray27')

#Makes the window unresizable
root.resizable(0,0)

root.mainloop()



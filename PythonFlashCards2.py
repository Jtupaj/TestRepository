from tkinter import *

root = Tk()
root.title("FlashCards")
#myLable is the Help button's
myLabel = Label(root, text="Press the start button to generate a number, then type your answer in the box and click check answer", fg="gray")
textvar = StringVar()
varx = StringVar()
vary = StringVar()
labelx = Label(root, textvariable=varx, anchor="e", width=10)
labelx.grid(row=6,column=1)
labely = Label(root, textvariable=vary, anchor="e", width=10)


labely.grid(row=7,column=1)
resultLabel = Label(root, textvariable=textvar)
resultLabel.grid(row=8,column=1)

root.geometry("345x215")

def myClick():
    myLabel.grid(row=1, column=4)

def myClickClear():
    myLabel.grid_forget()
    answerBox.grid_forget()
    varx.set("")
    vary.set("")

def destroy():
    answer1.config(text=" ")

x = 0
y = 0

def checkAnswer():
    try:
        result = int(answerBox.get())
        if result==x+y:
            answer1.config(text="Coooorect!")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
           
        else:
            answer1.config(text="incorrect.")
            answerBox.delete(0, "end")
            answer1.after(3000, destroy)
    except ValueError:
        answer1.config(text="Type in a number")
        answer1.after(3000, destroy)

    

    


answerBox = Entry(root, text="Enter your answer here.", validatecommand=checkAnswer)
#startBox makes the entry(Entry) appear after you press the start button
def startButton():
    answer1.config(text=" ")
    import random 
    global x
    global y
    y = random.randint(0,100)
    vary.set("+" + str(y))
    x = random.randint(0,100)
    varx.set(" " + str(x))
    answerBox.grid(row=5, column=1)
    #textvar.set(x+y)
    

answer = Entry(root)




Radiobutton(root, text="Top addend: 0-500", variable=x, value=1).grid(row=12, column=1)
Radiobutton(root, text="Top addend: 100-1000", variable=x, value=1).grid(row=12, column=2)
Radiobutton(root, text="Top addend: 100-10,000", variable=x, value=1).grid(row=12, column=3)

Radiobutton(root, text="Bottom addend: 0-500", variable=y, value=1).grid(row=13, column=1)
Radiobutton(root, text="Bottom addend: 100-1000", variable=y, value=1).grid(row=13, column=2)
Radiobutton(root, text="Bottom addend: 100-10,000", variable=y, value=1).grid(row=13, column=3)

helpButton = Button(root, text="HELP", command=myClick, borderwidth=2, padx=30, pady=10, fg="orange", bg="white")
helpButton.grid(row=1, column=1)

buttonClear = Button(root, text="CLEAR", command=myClickClear, borderwidth=2, padx=30, pady=10, fg="blue", bg="white")
buttonClear.grid(row=1, column=3)

buttonStart = Button(root, text="START", command=startButton, borderwidth=2, padx=30, pady=10, fg="black", bg="white")
buttonStart.grid(row=3, column=1)

buttonQuit = Button(root, text="QUIT", command=root.quit, borderwidth=2, padx=30, pady=10, fg="black", bg="white")
buttonQuit.grid(row=3, column=3)

answer1 = Label(root, text=" ",)
answer1.grid(row=8, column=1)

checkAnswer = Button(root, text="CHECK ANSWER", command=checkAnswer, bg="white" )
checkAnswer.grid(row=5, column=3)







root.mainloop()



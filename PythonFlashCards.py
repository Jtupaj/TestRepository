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

#ERROR, ERROR, ERROR, ERROR, ERROR.
def difficulty1():
    x=x+500
    y=y+500

def difficulty2():

    x=x+1000
    y=y+1000

def difficulty3 ():

    x=x+5000
    y=y+5000

    #ERROR, ERROR, ERROR, ERROR, ERROR.
    difBox1 = Checkbutton(root, text=("EASY"), command=difficulty1)
    difBox1.grid(row=9, column=1)

    difBox2 = Checkbutton(root, text=("MEDIUM"), command=difficulty2)
    difBox2.grid(row=10, column=1)

    difBox3 = Checkbutton(root, text=("HARD"), command=difficulty3)
    difBOx3.grid(row=11, column=1)

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



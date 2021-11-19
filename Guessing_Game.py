import tkinter as tk
import random


#variable initialization

number = random.randint(0,1000)
running = True
num = 0
n_maxn = 1000
n_minn = 0

#Exit
def e_BtnClose(event):
    root.destroy()

    #Game Rule and main game function
def e_BtnGuess(eent):
    global n_maxn
    global n_minn
    global num
    global running
    if running:
        var_a = int(entry_a.get())
        if var_a == number:
            labelqval("Congratulations Your Answer is Correct！")
            num += 1
            running = False
            numGuess()
        elif var_a < number:
            if var_a > n_minn:
                n_minn = var_a
                num += 1
                
                labelqval("Your number is smaller!, please enter any number between "+str(n_minn)+" and "+str(n_maxn)+" : ")
        else:
            if var_a < n_maxn:
                n_maxn = var_a
                num +=1
                
                labelqval("Your number is bigger!, please enter any number between "+str(n_minn)+" and "+str(n_maxn)+" : ")
    else:labelqval('You already answered!')


#Count the number of Guesses
def numGuess():
    if num == 1:
        labelqval('Congratulations! Your answer is correct in the first attempt.')

    print("You use : "+str(num)+ " number of gusses.")
   
#Main GUI structure 
def labelqval(Teeext):
    label_val_q.config(label_val_q,text = Teeext)

root = tk.Tk(className="The Number Game")
root.geometry("400x90+200+200")
label_val_q = tk.Label(root,width = "80")
label_val_q.pack(side = "top")

entry_a = tk.Entry(root,width = "40")
btnGuess = tk.Button(root,text = "Guess")
entry_a.pack(side = "left")
entry_a.bind('<Return>',e_BtnGuess)
btnGuess.bind('<Button-1>',e_BtnGuess)
btnGuess.pack(side = "left")
btnClose = tk.Button(root,text = "Exit")
btnClose.bind('<Button-1>',e_BtnClose)
btnClose.pack(side = "left")
labelqval("Please enter any integer between 0 and 1000: ")
entry_a.focus_get()
print(number)
root.mainloop()
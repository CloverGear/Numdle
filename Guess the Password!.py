import random
import tkinter as tk

window = tk.Tk()

window.geometry("500x500")
window.title("Password Guessing Game")

e = tk.Entry(window)
e.pack()

nPassword = str(random.randrange(1000, 10000))
# print(nPassword)

def clickGuess():
    nGuess = e.get()
    if nGuess == nPassword:
        myLabel  = tk.Label(window, text = "The password is correct!")
        myLabel.pack()
        
        labelFrame = tk.Frame(window)
        labelFrame.columnconfigure(0, weight = 1)
        labelFrame.columnconfigure(1, weight = 1)
        labelFrame.columnconfigure(2, weight = 1)
        labelFrame.columnconfigure(3, weight = 1)
        
        guessedNum0 = tk.Label(labelFrame, text = nGuess[0], font = ('Comic Sans', 18), bg='green')
        guessedNum0.grid(row = 0, column = 0)
            
        guessedNum1 = tk.Label(labelFrame, text = nGuess[1], font = ('Comic Sans', 18), bg='green')
        guessedNum1.grid(row = 0, column = 1)
        
        guessedNum2 = tk.Label(labelFrame, text = nGuess[2], font = ('Comic Sans', 18), bg='green')
        guessedNum2.grid(row = 0, column = 2)
        
        guessedNum3 = tk.Label(labelFrame, text = nGuess[3], font = ('Comic Sans', 18), bg='green')
        guessedNum3.grid(row = 0, column = 3)
        
        labelFrame.pack()
        
    else:
        myLabel  = tk.Label(window, text = "The password is incorrect. Here is the hint:")
        myLabel.pack()
        
        labelFrame = tk.Frame(window)
        labelFrame.columnconfigure(0, weight = 1)
        labelFrame.columnconfigure(1, weight = 1)
        labelFrame.columnconfigure(2, weight = 1)
        labelFrame.columnconfigure(3, weight = 1)
        
        guessedNum0 = tk.Label(labelFrame, text = nGuess[0], font = ('Comic Sans', 18))
        guessedNum0.grid(row = 0, column = 0)
            
        guessedNum1 = tk.Label(labelFrame, text = nGuess[1], font = ('Comic Sans', 18))
        guessedNum1.grid(row = 0, column = 1)
        
        guessedNum2 = tk.Label(labelFrame, text = nGuess[2], font = ('Comic Sans', 18))
        guessedNum2.grid(row = 0, column = 2)
        
        guessedNum3 = tk.Label(labelFrame, text = nGuess[3], font = ('Comic Sans', 18))
        guessedNum3.grid(row = 0, column = 3)
        
        if nGuess[0] == nPassword[0]:
            guessedNum0.config(bg='green')
        elif nGuess[0] in nPassword:
            guessedNum0.config(bg='yellow')
        
        if nGuess[1] == nPassword[1]:
            guessedNum1.config(bg='green')
        elif nGuess[1] in nPassword:
            guessedNum1.config(bg='yellow')
             
        if nGuess[2] == nPassword[2]:
            guessedNum2.config(bg='green')
        elif nGuess[2] in nPassword:
            guessedNum2.config(bg='yellow')
        
        if nGuess[3] == nPassword[3]:
            guessedNum3.config(bg='green')
        elif nGuess[3] in nPassword:
            guessedNum3.config(bg='yellow')
        
        labelFrame.pack()
        
myButton = tk.Button(window, text = "Lock Guess", command = lambda: clickGuess())
myButton.pack()

def button_click(a_nNum):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str (a_nNum))

def button_clear():
    e.delete(0, tk.END)

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.columnconfigure(2, weight = 1)

btn1 = tk.Button(buttonframe, text = "1", font = ('Comic Sans', 18), command = lambda: button_click(1))
btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

btn2 = tk.Button(buttonframe, text = "2", font = ('Comic Sans', 18), command = lambda: button_click(2))
btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

btn3 = tk.Button(buttonframe, text = "3", font = ('Comic Sans', 18), command = lambda: button_click(3))
btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

btn4 = tk.Button(buttonframe, text = "4", font = ('Comic Sans', 18), command = lambda: button_click(4))
btn4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

btn5 = tk.Button(buttonframe, text = "5", font = ('Comic Sans', 18), command = lambda: button_click(5))
btn5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = "6", font = ('Comic Sans', 18), command = lambda: button_click(6))
btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E)

btn7 = tk.Button(buttonframe, text = "7", font = ('Comic Sans', 18), command = lambda: button_click(7))
btn7.grid(row = 2, column = 0, sticky = tk.W + tk.E)

btn8 = tk.Button(buttonframe, text = "8", font = ('Comic Sans', 18), command = lambda: button_click(8))
btn8.grid(row = 2, column = 1, sticky = tk.W + tk.E)

btn9 = tk.Button(buttonframe, text = "9", font = ('Comic Sans', 18), command = lambda: button_click(9))
btn9.grid(row = 2, column = 2, sticky = tk.W + tk.E)

btn0 = tk.Button(buttonframe, text = "0", font = ('Comic Sans', 18), command = lambda: button_click(0))
btn0.grid(row = 3, column = 1, sticky = tk.W + tk.E)

btnClear = tk.Button(buttonframe, text = "Clear", font = ('Comic Sans', 18), command = button_clear)
btnClear.grid(row = 3, column = 2, sticky = tk.W + tk.E)

buttonframe.pack(fill = 'x')

window.mainloop()


'''
nPassword = str(random.randrange(1000, 10000))
nPreNumOfGuesses = int(input("How many guesses do you think you need: "))
nNumOfGuesses = 0
bGuessed = False

while bGuessed == False:
    nGuess = input("Please enter the password: ")
    if nGuess == nPassword:
        bGuessed = True
        print("The password is correct")
        
    else:
        print()
        print("The password is incorrect. Here are some hints:")
        for j in range(0, 4):
            if nGuess[j] == nPassword[j]:
                if j + 1 == 1:
                    print("The 1st number is correct,")
                elif j + 1 == 2:
                    print("The 2nd number is correct,")
                elif j + 1 == 3:
                    print("The 3rd number is correct,")
                else:
                    print("The " + str(j + 1) + "th number is correct,")
                    
            elif nGuess[j] in nPassword:
                print("The number", nGuess[j], "appeared at least once in the password")
                
            else:
                print("The number", nGuess[j], "is not in the password")
        
        if int(nPassword) < int(nGuess):
            print("The password is smaller than your guess")
        else:
            print("The password is bigger than your guess")
    
    print()
    nNumOfGuesses += 1
            
if nNumOfGuesses < nPreNumOfGuesses:
    print("You guessed the numebr in", nNumOfGuesses, "tires, faster than you thought")
elif nNumOfGuesses == nPreNumOfGuesses:
    print("You guessed the numebr in", nNumOfGuesses, "tires, just as you predicted")
else:
    print("You guessed the numebr in", nNumOfGuesses, "tires, slower than you thought")
'''
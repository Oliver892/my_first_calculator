from tkinter import *
from math import sin, cos, tan, pow, log, sqrt, factorial

# all functions goes here
def write(x):
	display.config(state=NORMAL)
	global clear
	if clear == True:
		display.delete(0,END)
		if x == '-' or x == '+' or x == '*' or x == '/':
			display.insert(END, displayAns.get())
		clear = False
	display.insert(END, x)
	display.config(state=DISABLED)

def backspace():
	display.config(state=NORMAL)
	display.delete(len(display.get())-1)
	display.config(state=DISABLED)

def ac():
	display.config(state=NORMAL)
	display.delete(0, END)
	display.config(state=DISABLED)

def exe():
	displayAns.config(state=NORMAL)
	global clear
	try:
		result = eval(display.get())
	except:
		displayAns.delete(0, END)
		displayAns.insert(END, 'ERROR')
		displayAns.config(state=DISABLED)
		return
	if len(displayAns.get()) != 0:
		displayAns.delete(0, END)
	displayAns.insert(END, result)
	clear = True
	displayAns.config(state=DISABLED)

def ans():
	display.config(state=NORMAL)
	global clear
	if clear == True:
		display.delete(0,END)
		clear = False
	if displayAns.get() == 'ERROR':
		display.config(state=DISABLED)
		return
	display.insert(END, displayAns.get())
	display.config(state=DISABLED)

# initialization
root = Tk()
root.title('Calculator')
root.geometry('600x400')
clear = False
buttonHeight = 0.15
buttonWidth = 0.2

# set up display for operation
display = Entry(root, bd=3, state=DISABLED)
display.place(relheight=0.1, relwidth=0.75)

#set up display for answer
displayAns = Entry(root, bd=3, state=DISABLED)
displayAns.place(relheight=0.1, relwidth=0.25, relx=0.75)

# define buttons
buttonOpenBrac = Button(root, text='(', command=lambda: write('('))
buttonCloseBrac = Button(root, text=')', command=lambda: write(')'))
buttonComma = Button(root, text=',', command=lambda: write(','))
buttonSqrt = Button(root, text='sqrt', command=lambda: write('sqrt('))
buttonFac = Button(root, text='!', command=lambda: write('factorial('))

buttonSin = Button(root, text='sin', command=lambda: write('sin('))
buttonCos = Button(root, text='cos', command=lambda: write('cos('))
buttonTan = Button(root, text='tan', command=lambda: write('tan('))
buttonPow = Button(root, text='pow', command=lambda: write('pow('))
buttonLog = Button(root, text='log', command=lambda: write('log('))

button7 = Button(root, text='7', command=lambda: write('7'))
button8 = Button(root, text='8', command=lambda: write('8'))
button9 = Button(root, text='9', command=lambda: write('9'))
buttonDel = Button(root, text='DEL', fg='red', command=backspace)
buttonAc = Button(root, text='AC', fg='red', command=ac)

button4 = Button(root, text='4', command=lambda: write('4'))
button5 = Button(root, text='5', command=lambda: write('5'))
button6 = Button(root, text='6', command=lambda: write('6'))
buttonMultiply = Button(root, text='*', command=lambda: write('*'))
buttonDivide = Button(root, text='/', command=lambda: write('/'))

button1 = Button(root, text='1', command=lambda: write('1'))
button2 = Button(root, text='2', command=lambda: write('2'))
button3 = Button(root, text='3', command=lambda: write('3'))
buttonAdd = Button(root, text='+', command=lambda: write('+'))
buttonMinus = Button(root, text='-', command=lambda: write('-'))

button0 = Button(root, text='0', command=lambda: write('0'))
buttonDot = Button(root, text='.', command=lambda: write('.'))
buttonExp = Button(root, text='EXP', command=lambda: write('e'))
buttonAns = Button(root, text='ANS', command=ans)
buttonExe = Button(root, text='EXE', command= exe)

# place buttons
buttonOpenBrac.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.1, relx=0)
buttonCloseBrac.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.1, relx=0.2)
buttonComma.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.1, relx=0.4)
buttonSqrt.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.1, relx=0.6)
buttonFac.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.1, relx=0.8)

buttonSin.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.25, relx=0)
buttonCos.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.25, relx=0.2)
buttonTan.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.25, relx=0.4)
buttonPow.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.25, relx=0.6)
buttonLog.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.25, relx=0.8)

button7.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.4, relx=0)
button8.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.4, relx=0.2)
button9.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.4, relx=0.4)
buttonDel.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.4, relx=0.6)
buttonAc.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.4, relx=0.8)

button4.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.55, relx=0)
button5.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.55, relx=0.2)
button6.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.55, relx=0.4)
buttonMultiply.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.55, relx=0.6)
buttonDivide.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.55, relx=0.8)

button1.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.7, relx=0)
button2.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.7, relx=0.2)
button3.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.7, relx=0.4)
buttonAdd.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.7, relx=0.6)
buttonMinus.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.7, relx=0.8)

button0.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.85, relx=0)
buttonDot.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.85, relx=0.2)
buttonExp.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.85, relx=0.4)
buttonAns.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.85, relx=0.6)
buttonExe.place(relwidth=buttonWidth, relheight=buttonHeight, rely=0.85, relx=0.8)

# loop the whole program
root.mainloop()
from tkinter import *
import numpy as np
import math

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = " "

def btnSquare():
    i = int(text_Input.get())
    sq = str(i * i)
    text_Input.set(sq)

def btnSin():
    x = int((text_Input.get())) * 2 * math.pi / 360.0
    y2 = math.sin(x)
    text_Input.set(y2)

def btnLog():
    x = int((text_Input.get()))
    y2 = math.log10(x)
    text_Input.set(y2)

def btnSqrt():
    x = int((text_Input.get()))
    y2 = math.sqrt(x)
    text_Input.set(y2)

def btnCos():
    x = int((text_Input.get())) * 2 * math.pi / 360.0
    y2 = math.cos(x)
    text_Input.set(y2)

def checkInput(Input):
    if type(text_Input) == 'int':
        return True
    else:
        return False

cal = Tk()
cal.title("MyCalc")
operator = " "
text_Input = StringVar()
checkInput(text_Input)

entry = Entry(cal, font=('calibri', 20, 'bold'), bd=30, insertwidth=3, bg='black',
              textvariable=text_Input, justify='right', state=DISABLED)
entry.grid(columnspan=4)

button7 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='7',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(7))
button7.grid(row=1, column=0)
button8 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='8',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(8))
button8.grid(row=1, column=1)
button9 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='9',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(9))
button9.grid(row=1, column=2)
buttonadd = Button(cal, padx=16, pady=16, bd=8, fg='black',
                   text='+',
                   font=('calibri', 20, 'bold'), command=lambda: btnclick('+'))
buttonadd.grid(row=1, column=3)

button4 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='4',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(4))
button4.grid(row=2, column=0)
button5 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='5',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(5))
button5.grid(row=2, column=1)
button6 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='6',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(6))
button6.grid(row=2, column=2)
buttonsub = Button(cal, padx=16, pady=16, bd=8, fg='black',
                   text='-',
                   font=('calibri', 20, 'bold'), command=lambda: btnclick('-'))
buttonsub.grid(row=2, column=3)

button1 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='1',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(1))
button1.grid(row=3, column=0)
button2 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='2',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(2))
button2.grid(row=3, column=1)
button3 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='3',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(3))
button3.grid(row=3, column=2)
buttonmul = Button(cal, padx=16, pady=16, bd=8, fg='black',
                   text='*',
                   font=('calibri', 20, 'bold'), command=lambda: btnclick('*'))
buttonmul.grid(row=3, column=3)

buttonSq = Button(cal, padx=10, pady=16, bd=8, fg='black',
                  text='x^2',
                  font=('calibri', 16, 'bold'), command=btnSquare)
buttonSq.grid(row=4, column=0)
buttonex = Button(cal, padx=10, pady=16, bd=8, fg='black',
                  text='x^x',
                  font=('calibri', 16, 'bold'), command=lambda: btnclick('**'))
buttonex.grid(row=4, column=1)
buttonsin = Button(cal, padx=10, pady=16, bd=8, fg='black',
                   text='sin',
                   font=('calibri', 16, 'bold'), command=btnSin)
buttonsin.grid(row=4, column=2)
buttonlog = Button(cal, padx=10, pady=16, bd=8, fg='black',
                   text='log',
                   font=('calibri', 16, 'bold'), command=btnLog)
buttonlog.grid(row=4, column=3)

button0 = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='0',
                 font=('calibri', 20, 'bold'), command=lambda: btnclick(0))
button0.grid(row=5, column=0)
buttonC = Button(cal, padx=16, pady=16, bd=8, fg='black',
                 text='C',
                 font=('calibri', 20, 'bold'), command=btnClear)
buttonC.grid(row=5, column=1)
buttonEqual = Button(cal, padx=16, pady=16, bd=8, fg='black',
                     text='=',
                     font=('calibri', 20, 'bold'), command=btnEquals)
buttonEqual.grid(row=5, column=2)
buttondiv = Button(cal, padx=16, pady=16, bd=8, fg='black',
                   text='/',
                   font=('calibri', 20, 'bold'), command=lambda: btnclick('/'))
buttondiv.grid(row=5, column=3)

buttonSqrt = Button(cal, padx=10, pady=16, bd=8, fg='black',
                    text='√',
                    font=('calibri', 20, 'bold'), command=btnSqrt)
buttonSqrt.grid(row=6, column=0)
buttonCos = Button(cal, padx=10, pady=16, bd=8, fg='black',
                   text='cos',
                   font=('calibri', 20, 'bold'), command=btnCos)
buttonCos.grid(row=6, column=1)
buttonPercent = Button(cal, padx=10, pady=16, bd=8, fg='black',
                       text='%',
                       font=('calibri', 20, 'bold'), command=lambda: btnclick('%'))
buttonPercent.grid(row=6, column=2)
buttonDecimal = Button(cal, padx=10, pady=16, bd=8, fg='black',
                       text='.',
                       font=('calibri', 20, 'bold'), command=lambda: btnclick('.'))
buttonDecimal.grid(row=6, column=3)

cal.mainloop()
from tkinter import *

val = ''
def prs(num):
    global val
    val = val + str(num)
    display['text'] = val


def clear(num):
    global val
    val = ''
    display['text'] = val

def equal(num):
    global val
    if num == str(num):
        try:
            val = str(eval(val))
        except:
            val = 'Syntax Error'
            display['text'] = val
        display['text'] = val


window = Tk()
window.geometry('500x520')
window.title('Calculator')

display = Label(window, width=60, height=5, bg='black', fg='white')
display.grid(row=0, columnspan=10, padx=8, pady=10)

buttonclr = Button(window, width=10, height=3, bg='#cfcfcf', text='Clear', command=lambda :clear(0))
buttonclr.grid(row=1, column=5, padx=10)

button9 = Button(window, width=5, height=3, bg='#cfcfcf', text='9', command=lambda  :prs(9))
button9.grid(row=2, column=1, padx=10, pady=10)

button8 = Button(window, width=5, height=3, bg='#cfcfcf', text='8', command=lambda  :prs(8))
button8.grid(row=2, column=2, padx=10, pady=10)

button7 = Button(window, width=5, height=3, bg='#cfcfcf', text='7', command=lambda  :prs(7))
button7.grid(row=2, column=3, padx=10, pady=10)

buttondiv = Button(window, width=10, height=3, bg='#cfcfcf', text='/', command=lambda  :prs('/'))
buttondiv.grid(row=2, column=5, padx=10, pady=10)

button6 = Button(window, width=5, height=3, bg='#cfcfcf', text='6', command=lambda  :prs(6))
button6.grid(row=3, column=1, padx=10, pady=10)

button5 = Button(window, width=5, height=3, bg='#cfcfcf', text='5', command=lambda  :prs(5))
button5.grid(row=3, column=2, padx=10, pady=10)

button4 = Button(window, width=5, height=3, bg='#cfcfcf', text='4', command=lambda  :prs(4))
button4.grid(row=3, column=3, padx=10, pady=10)

buttonmul = Button(window, width=10, height=3, bg='#cfcfcf', text='X', command=lambda  :prs('*'))
buttonmul.grid(row=3, column=5, padx=10, pady=10)

button3 = Button(window, width=5, height=3, bg='#cfcfcf', text='3', command=lambda  :prs(3))
button3.grid(row=4, column=1, padx=10, pady=10)

button2 = Button(window, width=5, height=3, bg='#cfcfcf', text='2', command=lambda  :prs(2))
button2.grid(row=4, column=2, padx=10, pady=10)

button1 = Button(window, width=5, height=3, bg='#cfcfcf', text='1', command=lambda  :prs(1))
button1.grid(row=4, column=3, padx=10, pady=10)

buttonsub = Button(window, width=10, height=3, bg='#cfcfcf', text='-', command=lambda  :prs('-'))
buttonsub.grid(row=4, column=5, padx=10, pady=10)

buttonpt = Button(window, width=5, height=3, bg='#cfcfcf', text='.', command=lambda  :prs('.'))
buttonpt.grid(row=5, column=1, padx=10, pady=10)

button0 = Button(window, width=5, height=3, bg='#cfcfcf', text='0', command=lambda  :prs(0))
button0.grid(row=5, column=2, padx=10, pady=10)

buttoneq = Button(window, width=5, height=3, bg='#cfcfcf', text='=', command=lambda  :equal(''))
buttoneq.grid(row=5, column=3, padx=10, pady=10)

buttonadd = Button(window, width=10, height=3, bg='#cfcfcf', text='+', command=lambda  :prs('+'))
buttonadd.grid(row=5, column=5, padx=10, pady=10)


window.mainloop()
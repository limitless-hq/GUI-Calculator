import tkinter as tk
import sys

m = tk.Tk()
m.title('Calculator')
m.geometry("350x275")

def buttons():
    # Button Grid:
    # 7 8 9 %
    # 4 5 6 X
    # 1 2 3 -
    # 0 . = +
    b7 = tk.Button(m, text = '7')
    b7.grid(row = 0, column = 0)
    b8 = tk.Button(m, text='8')
    b8.grid(row = 0, column = 1)
    b9 = tk.Button(m, text='9')
    b9.grid(row = 0, column = 2)
    b10 = tk.Button(m, text='%')
    b10.grid(row = 0, column = 3)
    b4 = tk.Button(m, text='4')
    b4.grid(row = 1, column = 0)
    b5 = tk.Button(m, text='5')
    b5.grid(row = 1, column = 1)
    b6 = tk.Button(m, text='6')
    b6.grid(row = 1, column = 2)
    b11 = tk.Button(m, text='X')
    b11.grid(row = 1, column = 3)
    b1 = tk.Button(m, text='1')
    b1.grid(row = 2, column = 0)
    b2 = tk.Button(m, text='2')
    b2.grid(row = 2, column = 1)
    b3 = tk.Button(m, text='3')
    b3.grid(row = 2, column = 2)
    b12 = tk.Button(m, text='-')
    b12.grid(row = 2, column = 3)
    b0 = tk.Button(m, text='0')
    b0.grid(row = 3, column = 0)
    b13 = tk.Button(m, text='.')
    b13.grid(row = 3, column = 1)
    b14 = tk.Button(m, text='=')
    b14.grid(row = 3, column = 2)
    b15 = tk.Button(m, text='+')
    b15.grid(row = 3, column = 3)

buttons() 

m.mainloop()
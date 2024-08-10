import tkinter as tk
import sys

m = tk.Tk()
m.title('Calculator')
m.configure(background='black')
entry_expression = ''

entry = tk.Entry(m, font=("ariel", 20, 'bold'), justify='right', bg='black', fg='white',bd=5, highlightcolor='white')
entry.grid(row=0, column=0, columnspan=4, pady=50)


def update_entry(value):
    global entry_expression
    entry_expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, entry_expression)


def clear_entry():
    global entry_expression
    entry_expression = ''
    entry.delete(0, tk.END)


def calculate():
    global entry_expression
    final_arr = []
    for value in entry_expression:
        final_arr.append(value)
    for value in final_arr:
        if value == '+':
            answer = int(final_arr[0]) + int(final_arr[2])
            entry.delete(0, tk.END)
            entry.insert(tk.END, answer)
        if value == '-':
            answer = int(final_arr[0]) - int(final_arr[2])
            entry.delete(0, tk.END)
            entry.insert(tk.END, answer)
        if value == 'x':
            answer = int(final_arr[0]) * int(final_arr[2])
            entry.delete(0, tk.END)
            entry.insert(tk.END, answer)
        if value == '/':
            answer = int(final_arr[0]) / int(final_arr[2])
            entry.delete(0, tk.END)
            entry.insert(tk.END, answer)



def buttons():
    # Button Grid:
    # 7 8 9 %
    # 4 5 6 X
    # 1 2 3 -
    # 0 . = +
    b7 = tk.Button(m, text = '7', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(7))
    b7.grid(row = 1, column = 0, padx=5, pady=5)
    b8 = tk.Button(m, text='8', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(8))
    b8.grid(row = 1, column = 1, padx=5, pady=5)
    b9 = tk.Button(m, text='9', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(9))
    b9.grid(row = 1, column = 2, padx=5, pady=5)
    b10 = tk.Button(m, text='%', padx = 10, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry('/'))
    b10.grid(row = 1, column = 3, padx=5, pady=5)
    b4 = tk.Button(m, text='4', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(4))
    b4.grid(row = 2, column = 0, padx=5, pady=5)
    b5 = tk.Button(m, text='5', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(5))
    b5.grid(row = 2, column = 1, padx=5, pady=5)
    b6 = tk.Button(m, text='6', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(6))
    b6.grid(row = 2, column = 2, padx=5, pady=5)
    b11 = tk.Button(m, text='X', padx = 13.2, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry('x'))
    b11.grid(row = 2, column = 3, padx=5, pady=5)
    b1 = tk.Button(m, text='1', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(1))
    b1.grid(row = 3, column = 0, padx=5, pady=5)
    b2 = tk.Button(m, text='2', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(2))
    b2.grid(row = 3, column = 1, padx=5, pady=5)
    b3 = tk.Button(m, text='3', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(3))
    b3.grid(row = 3, column = 2, padx=5, pady=5)
    b12 = tk.Button(m, text='-', padx = 17.4, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry('-'))
    b12.grid(row = 3, column = 3, padx=5, pady=5)
    b0 = tk.Button(m, text='0', padx = 15, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry(0))
    b0.grid(row = 4, column = 0, padx=5, pady=5)
    b13 = tk.Button(m, text='.', padx = 18.5, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry('.'))
    b13.grid(row = 4, column = 1, padx=5, pady=5)
    b14 = tk.Button(m, text='=', padx = 14.5, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command= calculate)
    b14.grid(row = 4, column = 2, padx=5, pady=5)
    b15 = tk.Button(m, text='+', padx = 13.5, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=lambda: update_entry('+'))
    b15.grid(row = 4, column = 3, padx=5, pady=5)
    clear = tk.Button(m, text='Clear', padx = 106, pady = 15, font=('ariel', '20', 'bold'), background='#FF9C00', command=clear_entry)
    clear.grid(row=5, column=0, columnspan=4)


buttons() 

m.mainloop()
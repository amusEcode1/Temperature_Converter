import tkinter as tk
from tkinter import ttk
'''Conversion of Celsius to Fahrenheit using Command Line Interface'''
def convert():
    user = int(input('Enter the Celcius Value '))
    return user * (9/5) + 32
print('Convert Celsius to Fahrenheit')
print(f'Convert: {convert()}')

'''Conversion of Celsius to Fahrenheit using Graphical User Interface'''
def conversion():
    celsius = entry_int.get()
    fahrenheit = (celsius * (9/5) + 32)
    output_string.set(fahrenheit)
app = tk.Tk()
app.title('amusEcode')
app.geometry('500x500')  
#Title Field
title_label = ttk.Label(app, text = 'Convert Celsius to Fahrenheit', font = 'calibri 25 bold')
title_label.pack()
#Input Field
input_frame = ttk.Frame(app)
text = ttk.Label(input_frame, text = 'Enter the Celsius Value', font = 'calibri 10 bold')
entry_int = tk.IntVar()
entry = ttk.Entry(input_frame, textvariable = entry_int)
button = ttk.Button(input_frame, text = 'Convert', command = conversion)
text.pack()
entry.pack(side = 'left')
button.pack(padx = 10)
input_frame.pack(pady = 20)
#Output
output_string = tk.StringVar()
output_label = ttk.Label(app, text = 'Output', font = 'calibri 20 bold', textvariable = output_string)
output_label.pack()
app.mainloop()
import tkinter as tk
from tkinter import ttk
'''window = tk.Tk()
window.title('amusEcode Project')
window.geometry('800x500')
label = tk.Label(master = window, text = 'This is a text')
label.pack()
message = tk.Text(master = window)
message.pack(0)
entry = ttk.Entry(master = window)
entry.pack()
button = ttk.Button(master = window, text = 'Click', command = lambda: print('Hello'))
button.pack()

window.mainloop()'''

'''def button_func():
    entry_int = entry.get()
    label.config(text = entry_int)
    entry['state'] = 'disabled'
def buttons_func():
    label.config(text = 'Large Text')
    entry['state'] = 'enabled'
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('500x500')
label = ttk.Label(master = window, text = 'Some Text')
label.pack()
entry = ttk.Entry(master = window)
entry.pack()
button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()
button2 = ttk.Button(master = window, text = 'The button', command = buttons_func)
button2.pack()

window.mainloop()'''

'''window = tk.Tk()
window.title('amusEcode')
window.geometry('800x500')

def button_func():
    string_var.set('Button Pressed')

string_var = tk.StringVar(value = 'Click me')
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

button = ttk.Button(master = window, text = 'Button', command = button_func)
button.pack()

window.mainloop()'''

'''window = tk.Tk()
window.title('amusEcode')
window.geometry('800x500')
def button_func():
    print('A basic button')
    print(radio_button.get())
    print(check_button.get())
button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()
def radio_func():
    a = check_bool.get()
    check_bool.set(False)
    output_string.set(a)

def check_func():
    print(radio_string.get())

#checkbutton
check_bool = tk.BooleanVar()
check_button = ttk.Checkbutton(window, text = 'Male', variable = check_bool, command = check_func)
check_button.pack()
radio_string = tk.StringVar()
radio_button1 = ttk.Radiobutton(window, text = 'radiobox 1', value = 'A', variable = radio_string, command = radio_func)
radio_button2 = ttk.Radiobutton(window, text = 'radiobox 2', value = 'B', variable = radio_string, command = radio_func)
radio_button1.pack()
radio_button2.pack() 

output_string = tk.StringVar()
output = ttk.Label(window, text = 'Output Value', textvariable = output_string)
output.pack()

window.mainloop()'''
'''def button_func(param):
    def inner_func():
        print('A button was pressed')
        print(entry_string.get())
    return inner_func
window = tk.Tk()
window.geometry('700x400')
window.title('amusEcode')

entry_string = tk.StringVar(value = 'test')
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = 'button', command = button_func(entry_string))
button.pack()


window.mainloop()'''

def motion_func(event):
    print(f'x: {event.x} y: {event.y}')


window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')

text = tk.Text(window)
text.pack()
#entry_string = tk.StringVar(value = 'jjjk')
entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text = 'A button')
button.pack()

#Event
'''entry.bind('<Alt-KeyPress-a>', lambda event: print(event.keycode))
text.bind('<Motion>', motion_func)
window.bind('<KeyPress>', lambda event: print(event.char))
entry.bind('<FocusIn>', lambda event: print('selected'))
entry.bind('<FocusOut>', lambda event: print('unselected'))'''
text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))
#text.bind('<Motion>', lambda event: print('Mousewheel'))
window.mainloop()
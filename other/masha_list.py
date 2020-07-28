# it was stolen

from tkinter import *
from tkinter import messagebox
import random

HEIGHT = 600
WIDTH = 600

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        Listbox.insert(END, task)

def add_task():
    task = text_input.get()
    if task != '':
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning('Warning', 'Enter the task in the input box, plase.')
    text_input.delete(0, END)

def del_one():
    task = listbox.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def del_all():
    confirmed = messagebox.askyesno('Plase Confirm', 'Do you really want to delete all?')
    if confirmed:
        global tasks
        tasks = []
        update_listbox()

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()

def choose_random():
    if len(task)> 0:
        task = random.choice(tasks)
        label_display['text'] = task
    else:
        messagebox.showwarning('Warning', 'No tasks')


def show_number_of_tasks():
    number_of_tasks = len(tasks)
    message = 'Number of tasks: %s' % number_of_tasks
    label_display['text'] = message

root = Tk()
root.title('My Super To-Do List')
root.geometry('%dx%d' % (WIDTH, HEIGHT))
root.resizable(False, False)

img = PhotoImage(file='img/todo.png')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

root.option_add('*Font', '{Comic Sans MS} 10')
root.option_add('*Background', 'white')

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_title = Label(frame, text='My Super To-Do List', fg='dark blue', font='{Comic Sans MS} 16')
label_title.place(relx=0.3)

label_display = Label(frame, text='')
label_display.place(relx=0.3, rely=0.1)

text_input = Entry(frame, width=15)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6)
'''
# Buttons
button_and_tack = Button (frame, text='Add task', command=add_tack)
button_and_tack.place(rely=0.15, relwidth=0.25)'''

button_del = Button(frame, text='Delete', command=del_one)
button_del.place(rely=0.25, relwidth=0.25)

button_del_all = Button(frame, text='Delete All', command=del_all)
button_del_all.place(rely=0.35, relwidth=0.25)

button_sort_asc = Button(frame, text='Sort (A-Z)', command=sort_asc)
button_sort_asc.place(rely=0.45, relwidth=0.25)

button_sort_desc = Button(frame, text='Sort (Z-A)', command=sort_desc)
button_sort_desc.place(rely=0.55, relwidth=0.25)

button_radom = Button(frame, text='Choose Random', command=choose_random)
button_radom.place(rely=0.65, relwidth=0.25)

button_number_of_tasks = Button(frame, text='Number of Tasks', command=show_number_of_tasks)
button_number_of_tasks.place(rely=0.75, relwidth=0.25)

button_exit = Button(frame, text='Exit', command=exit)
button_exit.place(rely=0.85, relwidth=0.25)

listbox = Listbox(frame)
listbox.place(relx=0.3, rely=0.24, relwidth=0.6, relheight=0.6)

root.mainloop()

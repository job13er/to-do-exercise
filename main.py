# Importing all the necessary modules
from tkinter import *

# Adding and Deleting items functions
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open('tasks.txt', 'a') as tasks_list_file:
        tasks_list_file.write(f'{new_task}\n')


def delete_item(listbox: Listbox):

    # print(f'Before: {listbox.get(ACTIVE)}')
    removing = listbox.get(ACTIVE)
    listbox.delete(ACTIVE)
    # print(f'After: {listbox.get(ACTIVE)}')

    with open('tasks.txt', 'r+') as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.seek(0)
        tasks_list_file.truncate()

        for line in lines:
            print(f'1)Active:[{removing}]')
            print(f'2)Line:[{line}]')
            print(f'3)s_line:[{line.strip()}]')
            print('\n')
            if removing.strip() != line.strip():
            # if removing != line.strip():
                # lines.remove(line)
                tasks_list_file.write(line)
        print('------')

        # tasks_list_file.close()
def load_tasks(listbox):
    # Adding items to the Listbox
    with open('tasks.txt', 'r+') as tasks_list:
        for task in tasks_list:
            listbox.insert(END, task)
        tasks_list.close()



def run():
    # Initializing the GUI window
    root = Tk()
    root.title('TechVidvan To-Do List')
    root.geometry('300x400')
    root.resizable(0, 0)
    root.config(bg="PaleVioletRed")

    # Heading Label
    Label(root, text='Tech Vidvan To-Do List', bg='PaleVioletRed', font=("Comic Sans MS", 15), wraplength=300).place(
        x=35, y=0)

    # Listbox with all the tasks with a Scrollbar
    tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)

    scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
    scroller.place(x=260, y=50, height=232)

    tasks.config(yscrollcommand=scroller.set)

    tasks.place(x=35, y=50)

    # # Adding items to the Listbox
    # with open('tasks.txt', 'r+') as tasks_list:
    #     for task in tasks_list:
    #         tasks.insert(END, task)
    #     tasks_list.close()
    load_tasks(tasks)

    # Creating the Entry widget where the user can enter a new item
    new_item_entry = Entry(root, width=37)
    new_item_entry.place(x=35, y=310)

    # Creating the Buttons
    add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                     command=lambda: add_item(new_item_entry, tasks))
    add_btn.place(x=45, y=350)

    delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                     command=lambda: delete_item(tasks))
    delete_btn.place(x=150, y=350)

    # Finalizing the window
    root.update()
    root.mainloop()

if __name__ == '__main__':
    run()

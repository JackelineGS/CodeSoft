import psycopg2
from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END

root = Tk()
root.title("Lista de tareas")

host = "localhost"
user = "postgres"
password = "postnew"
database = "tareas"
port = 5432


def save_new_student(title, description, status):

    connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    port = port
    )

    cur = connection.cursor()
    query = '''INSERT INTO lista(title, description, status) VALUES (%s, %s, %s)'''
    cur.execute(query, (title, description, status))
    print('Data Saved')
    connection.commit()
    connection.close()
    display_students()

def display_students(): 
        connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database,
        port = port
        )

        cur = connection.cursor()
        query = '''SELECT * FROM lista'''
        cur.execute(query)

        row = cur.fetchall()
        
        listbox = Listbox(frame, width=90, height=10)
        listbox.grid(row=10, columnspan=5, sticky=W+E)
        
        for x in row: 
             listbox.insert(END, x)

        connection.commit()
        connection.close()

        # Refresh with new Task 
        


#Canvas
canvas = Canvas(root, height=380, width=400)
canvas.pack()
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


label = Label(frame, text='Add new task')
label.grid(row=0, column=1)

label = Label(frame, text='Title')
label.grid(row=1, column=0)
entry_title = Entry(frame)
entry_title.grid(row=1, column=1)

label = Label(frame, text='Description')
label.grid(row=2, column=0)
entry_description = Entry(frame)
entry_description.grid(row=2, column=1)

label = Label(frame, text='Status')
label.grid(row=3, column=0)
entry_status = Entry(frame)
entry_status.grid(row=3, column=1)

button = Button(frame, text='Add', command=lambda:save_new_student(
    entry_title.get(),
    entry_description.get(),
    entry_status.get()
))
button.grid(row=5, column=1, sticky=W+E)

display_students()
root.mainloop()




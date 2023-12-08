import psycopg2
from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E

root = Tk()
root.title("Lista de tareas")

def save_new_student(title, description, status):
    print(title)
    print(description)
    print(status)

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

root.mainloop()


host = "localhost"
user = "postgres"
password = "postnew"
database = "tareas"
port = 5432

cur = None
# Crea un objeto de conexión a la base de datos
try:
    connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    port = port
    )

    cur = connection.cursor()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
                """)

    new_user = ("maria torres", "maria1@gmail.com", "mar321")
    insert_query = "INSERT INTO users(name, email, password) VALUES (%s, %s, %s) RETURNING id, name, email"
    cur.execute(insert_query, new_user)
    user = cur.fetchone()
    connection.commit()
    print(user)
    
except Exception as error:
    print(f'Error: {error}')
finally:
    if cur is not None:
        cur.close()
    if connection is not None:
        connection.close()

# Ejecuta una consulta SQL




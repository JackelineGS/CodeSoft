import psycopg2

host = "localhost"
user = "postgres"
password = ""
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




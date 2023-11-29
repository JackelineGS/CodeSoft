import psycopg2

host = "localhost"
user = "postgres"
password = "postnew"
database = "tareas"
port = 5432

# Crea un objeto de conexión a la base de datos
try:
    connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = database,
    port = port
)
    print("correct conection")
except Exception as error:
    print(error)


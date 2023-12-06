CREATE DATABASE tareas

CREATE TABLE lista(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE,
    description VARCHAR(255),
    estado ENUM('completada', 'pendiente')  
)
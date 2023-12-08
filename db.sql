CREATE DATABASE tareas

CREATE TABLE lista(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE,
    description VARCHAR(255),
    status VARCHAR(20)  
)

INSERT INTO lista(title, description, status) VALUES ('tarea 1', 'Revisar videos', 'incompleto');
INSERT INTO lista(title, description, status) VALUES ('tarea 2', 'Revisar manuales', 'incompleto');




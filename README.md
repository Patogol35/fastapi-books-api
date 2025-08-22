📚 FastAPI Books CRUD

Este proyecto es una API REST construida con FastAPI y MySQL que permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre una colección de libros.

---

🚀 Tecnologías utilizadas

FastAPI

MySQL

SQLAlchemy

Uvicorn

⚙️ Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

Python 3.9+

MySQL Server

pip (gestor de paquetes de Python)

---

🗄️ Configuración de la base de datos

Entra a MySQL con tu usuario:

mysql -u root -p


Crea la base de datos:

CREATE DATABASE fastapi_books;

En este proyecto usamos:

Usuario: root

Contraseña: patricio12

Base de datos: fastapi_books

---

📦 Instalación del proyecto

Clona el repositorio:

git clone https://github.com/Patogol35/fastapi-books-api.git

cd fastapi-books-crud

Crea un entorno virtual e instålalo:

python -m venv venv

En Linux/Mac: source venv/bin/activate 

En Windows: venv\Scripts\activate 


Instala las dependencias:

pip install -r requirements.txt


⚡ Ejecución del servidor

uvicorn main:app --reload


El servidor estará disponible en:
👉 http://127.0.0.1:8000

La documentación interactiva estará en:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

---

📌 Endpoints disponibles

🔹 Crear un libro

POST /books/

Body (JSON):

{
  "title": "Las Catilinarias",
  "author": "Juan Montalvo",
  "year": 1880
}

🔹 Obtener todos los libros

GET /books/

🔹 Obtener un libro por ID

GET /books/{book_id}

Ejemplo:

/books/1

🔹 Actualizar un libro

PUT /books/{book_id}

Body (JSON):

{
  "title": "El Cosmopolita",
  "author": "Juan Montalvo",
  "year": 1886
}

🔹 Eliminar un libro

DELETE /books/{book_id}

Ejemplo:

/books/1

---

✨ Autor

👨‍💻 Jorge Patricio Santamaría Cherrez

Máster en Ingeniería de Software y Sistemas Informáticos

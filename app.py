from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# FUNCIÓN PARA CONECTAR CON LA BASE DE DATOS
def consultar_db():
    conexion = sqlite3.connect('blog.db')
    # Esto sirve para poder llamar a las columnas por su nombre (ej: post['titulo'])
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    # Seleccionamos todo de la tabla posts
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    conexion.close()
    return posts

# RUTA PRINCIPAL (LA WEB)
@app.route('/')
def inicio():
    # Llamamos a la función de arriba para obtener los datos
    mis_posts = consultar_db()
    # Enviamos esos datos al archivo HTML
    return render_template('index.html', noticias=mis_posts)

# ARRANCAR EL SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
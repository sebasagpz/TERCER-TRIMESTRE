from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def conectar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="form",
            user="postgres",
            password="123456"
        )
        print("✅ Conexión exitosa")
        return conexion
    except Exception as e:
        print("❌ Error en la conexión:", e)
        return None


@app.route("/", methods=["GET", "POST"])
def formulario():
    if request.method == "POST": # enviar el dato al formulario
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        direccion = request.form["direccion"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        mensaje = request.form["mensaje"]

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO registros (nombre, apellido, direccion, telefono, correo, mensaje) 
            VALUES (%s, %s, %s, %s, %s, %s) # espacio donde van los valores
        """, (nombre, apellido, direccion, telefono, correo, mensaje))
        conn.commit()
        cursor.close() # decirle que hacer, osea cerrar
        conn.close()

        return "Los datos fueron guardados correctamente."

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)

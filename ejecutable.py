from flask import Flask, render_template, request
from airbnb import obtener_datos_airbnb
from gtravel import obtener_datos_google_travel

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    datos_airbnb = []
    datos_google_travel = []
    
    if request.method == "POST":
        consulta = request.form["consulta"]
        precio_maximo = float(request.form["precio_maximo"])  # Obtener precio máximo desde el formulario
        
        # Obtener datos de Airbnb
        datos_airbnb = obtener_datos_airbnb(consulta, precio_maximo)
        
        # Obtener datos de Google Travel
        datos_google_travel = obtener_datos_google_travel(consulta, precio_maximo)

        return render_template("resultado.html", datos_airbnb=datos_airbnb, datos_google_travel=datos_google_travel)
        
    return render_template("index.html", datos_airbnb=datos_airbnb, datos_google_travel=datos_google_travel)

if __name__ == "__main__":
    app.run(debug=True)


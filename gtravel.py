from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

def obtener_datos_google_travel(consulta, precio_maximo):
    # Initialize ChromeDriver service
    service = Service('/usr/bin/chromedriver')
    service.start()

    # Configure Chrome options (uncomment for headless mode)
    options = Options()
    # options.add_argument('--headless')

    # Create Chrome driver instance
    driver = webdriver.Chrome(service=service, options=options)

    # Build Google Travel URL with user query
    url = f"https://www.google.com/travel/hotels?q={consulta}"

    # Open the URL in the browser
    driver.get(url)
    
    # Para aceptar las cookies si es necesario
    driver.find_element(By.XPATH, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 XWZjwc"]').click()

    time.sleep(15)

    # Extract data from results
    resultados = driver.find_elements(By.XPATH, '//h2[@class="BgYkof ogfYpf ykx2he"]')
    precios = driver.find_elements(By.XPATH, '//span[@class="kixHKb flySGb"]')
    
    datos = []
    hoteles = []
    precios_hoteles = []

    # Bucle para resultados
    for resultado in resultados:
        nombre_hotel = resultado.text
        hoteles.append(nombre_hotel)

    # Bucle para precios
    for precio in precios:
        precio_hotel = precio.text
        if precio_hotel.strip():
            if float(precio_hotel[:3]) <= precio_maximo:  # Filtrar por precio máximo
                precios_hoteles.append(precio.text)

    datos = list(zip(hoteles, precios_hoteles))

    # Close the browser
    driver.quit()

    return datos


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        consulta = request.form["consulta"]
        precio_maximo = float(request.form["precio_maximo"])  # Obtener precio máximo desde el formulario
        datos = obtener_datos_google_travel(consulta, precio_maximo)
        return render_template("resultado.html", datos=datos)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


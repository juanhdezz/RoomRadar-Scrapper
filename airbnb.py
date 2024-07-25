from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

def obtener_datos_airbnb(consulta, precio_maximo):
    # Inicializa el servicio ChromeDriver
    service = Service('/usr/bin/chromedriver')
    service.start()

    # Inicializa las opciones de Chrome
    options = Options()
    # Aquí puedes configurar las opciones según sea necesario
    # options.add_argument('--headless')

    # Crea una instancia del controlador Chrome remoto
    driver = webdriver.Chrome(service=service, options=options)

    # Abre una página web en el navegador
    cadena_previa = 'https://www.airbnb.es/s/'
    cadena_siguiente = '/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-06-01&monthly_length=3&monthly_end_date=2024-09-01&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change'
    enlace = cadena_previa + consulta + cadena_siguiente
    driver.get(enlace)

    # Espera 5 segundos
    time.sleep(5)

    # Extraer los datos de los resultados
    resultados = driver.find_elements(By.XPATH, '//span[@data-testid="listing-card-name"]')
    precios = driver.find_elements(By.XPATH, '//span[@class="_11jcbg2"]')
    datos = []
    hoteles = []
    precios_hoteles = []

    # Bucle para resultados
    for resultado in resultados:
        nombre_hotel = resultado.text
        hoteles.append(nombre_hotel)
        print(nombre_hotel)

    # Bucle para precios
    for precio in precios:
        precio_hotel = precio.text # Extraer solo el precio numérico
        if '€' in precio_hotel:
            precio_hotel = precio_hotel[:3]
            #precio_hotel = precio_hotel.replace('€', '').replace(',', '')  # Eliminar caracteres no numéricos
            if float(precio_hotel) <= precio_maximo:  # Filtrar por precio máximo
                precios_hoteles.append(precio.text)
                

    datos = list(zip(hoteles, precios_hoteles))

    # Cerrar el navegador
    driver.quit()

    return datos


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        consulta = request.form["consulta"]
        precio_maximo = float(request.form["precio_maximo"])  # Obtener precio máximo desde el formulario
        datos = obtener_datos_airbnb(consulta, precio_maximo)
        return render_template("resultado.html", datos=datos)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


#cy5jw6o atm_5j_223wjw atm_70_87waog atm_j3_1u6x1zy atm_jb_4shrsx atm_mk_h2mmj6 atm_vy_7abht0 dir dir-ltr


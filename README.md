# RoomRadar

## Introducción

Presentamos una aplicación web innovadora diseñada para facilitar la búsqueda y comparación de hoteles de diversas fuentes en un solo lugar. Aprovechando tecnologías modernas, esta plataforma ofrece a los usuarios la capacidad de encontrar las mejores opciones de alojamiento según sus necesidades y presupuesto.

## Objetivo

El objetivo principal de esta aplicación es proporcionar una herramienta eficaz y fácil de usar para comparar precios y características de hoteles de dos fuentes principales: Airbnb, Google Travel. La integración de estos datos permite a los usuarios tomar decisiones informadas sin la necesidad de consultar múltiples sitios web.

## Características Clave

- **Búsqueda Integrada:**
  - Los usuarios pueden buscar hoteles introduciendo una ubicación y un precio máximo.
  - La aplicación consulta simultáneamente a Airbnb y Google Travel para obtener resultados actualizados.
  
- **Comparación de Precios:**
  - Muestra los precios de las dos fuentes para facilitar la comparación.
  - Filtrado de resultados para mostrar solo aquellos que se ajusten al presupuesto del usuario.
  
- **Interfaz Intuitiva:**
  - Una interfaz limpia y fácil de navegar.
  - Resultados presentados de manera clara y ordenada, mostrando el nombre del hotel, el precio y la fuente.
  
- **Resultados Filtrados:**
  - Los datos se filtran automáticamente para excluir aquellos que excedan el precio máximo especificado por el usuario.

## Tecnologías Utilizadas

- **Backend con Flask:**
  - Framework ligero y flexible que facilita el desarrollo rápido y eficiente de la aplicación web.
  - Utiliza Python para la lógica de negocio y la integración de datos.
  
- **Web Scraping con Selenium:**
  - Obtención de datos en tiempo real desde Airbnb y Google Travel.
  - Navegación automatizada para extraer la información necesaria de las páginas web.
  
- **Despliegue en Heroku:**
  - Plataforma de nube que permite un despliegue rápido y eficiente.
  - Garantiza que la aplicación esté disponible y escalable según la demanda.

## Beneficios para el Cliente

- **Ahorro de Tiempo:**
  - Centraliza la información de múltiples fuentes, evitando la necesidad de visitar varios sitios web.
  - Proceso de búsqueda rápido y eficiente.
  
- **Toma de Decisiones Informada:**
  - Presenta una visión comparativa de los precios y opciones de alojamiento.
  - Ayuda a los usuarios a elegir la mejor oferta disponible.
  
- **Accesibilidad y Conveniencia:**
  - Disponible desde cualquier dispositivo con acceso a internet.
  - Interfaz amigable que facilita la interacción y el uso.

## Ejemplo de Uso

Un usuario que planea un viaje a París puede simplemente ingresar "París" y su presupuesto máximo por noche en la aplicación. En pocos segundos, la plataforma mostrará una lista de hoteles disponibles en Airbnb y Google Travel, permitiendo al usuario comparar precios y elegir la mejor opción sin salir de la página.

## Instalación y Uso

1. **Clona el repositorio:**
   ```sh
   git clone https://github.com/tu_usuario/roomradar.git
    ```
2. **Navega al directorio del proyecto:**
   ```sh
   cd roomradar
   ```
3. **Instala las dependencias:**
    ```sh
   pip install -r requirements.txt
   ```
4. **Ejecuta la aplicacion:**
    ```sh
    python3 app.py
    ```
5. **Despliegue**

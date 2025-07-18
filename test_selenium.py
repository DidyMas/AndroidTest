from driver_controller import get_chrome_driver

# Crear una instancia del driver usando el controlador
driver = get_chrome_driver(headless=True)

# Navegar a una página web
driver.get("http://3.136.167.94:3002/signin")

# Obtener el título de la página y mostrarlo en la terminal
print(f"Título de la página: {driver.title}")

# Cerrar el navegador
driver.quit()

# behave
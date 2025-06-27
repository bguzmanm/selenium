from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import tempfile
import time


options = Options()
options.add_argument("--headless=new")  # o "--headless" según la versión
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)
# Esperar resultados
time.sleep(2)

# Validar que exista algún resultado
#resultados = driver.find_elements(By.CSS_SELECTOR,".result")
resultados = driver.find_elements(By.CSS_SELECTOR,'[data-testid="result"]')
assert len(resultados) > 0, "No se encontraron resultados."
print("✅ Prueba funcional completada con éxito")

driver.quit()


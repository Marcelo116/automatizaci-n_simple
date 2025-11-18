from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def obtener_precio_accion(nombre_accion):
    try:
        options = Options()
        options.add_argument("–headless/=new")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.google.com/search?q=precio+de+{nombre_accion}")
        wait = WebDriverWait(driver, 1)
        precio = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@jsname="vWLAgc"]'))).text
        driver.quit()
        return f"El precio de {nombre_accion} es {precio} pesos mexicanos."
    except Exception as e:
        print("No se pudo obtener el precio de la acción en este momento. Error:", e)
        if driver:
            driver.quit()
        return None, None
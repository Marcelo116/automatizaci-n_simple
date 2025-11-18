from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def obtener_clima(ciudad):
    try:
        options = Options()
        options.add_argument("–headless/=new")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(f"https://www.google.com/search?q=clima+en+{ciudad}")
        wait = WebDriverWait(driver, 1)
        temperatura = wait.until(EC.presence_of_element_located((By.ID, "wob_tm"))).text
        condicion = wait.until(
            EC.presence_of_element_located((By.XPATH, '//span[@id="wob_dc"] | //div[contains(@class,"vk_gy")]//span'))).text
        driver.quit()
        return f"El {ciudad} es {condicion} con una temperatura de {temperatura}°C."
    except Exception as e:
        print("No se pudo obtener el clima en este momento. Error:", e)
        if driver:
            driver.quit()
        return None, None



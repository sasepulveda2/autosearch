from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import json
import time
from config import page as url

with open(
    "eventos.json", "r", encoding="utf-8"
) as f:  
    eventos = json.load(f) # acá se cargan los eventos guardados desde el JSON

driver = webdriver.Chrome()  # se inicia chrome
driver.get(url)  # esto usa la URL de config.py

acciones = ActionChains(driver)

for e in eventos:
    if e["tipo"] == "click":
        # mueve el mouse a la posición y hacer click
        acciones.move_by_offset(e["x"], e["y"]).click().perform()
        # No TOCAR idealmente
        acciones.reset_actions()
        time.sleep(0.5)
driver.quit()

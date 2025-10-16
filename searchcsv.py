from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import signal
import sys
import time
from config import page as url
eventos = []

def signal_handler(sig, frame):
    print("\nGuardando eventos capturados...")
    with open("eventos.json", "w", encoding="utf-8") as f:
        json.dump(eventos, f, indent=2)
    driver.quit()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
driver = webdriver.Chrome()
driver.get(url)

#script para capturar eventos
driver.execute_script("""
window.eventos = [];
document.addEventListener('click', function(e) {
    window.eventos.push({
        tipo: 'click',
        x: e.clientX,
        y: e.clientY,
        target: e.target.tagName
    });
});
document.addEventListener('keydown', function(e) {
    window.eventos.push({
        tipo: 'keydown',
        key: e.key,
        target: e.target.tagName
    });
});
""")

print("Registrando eventos. Presiona Ctrl+C para finalizar...")

try:
    while True:
        # pa obtener eventos desde el navegador
        nuevos = driver.execute_script("return window.eventos;")
        if nuevos:
            eventos.extend(nuevos)
            driver.execute_script("window.eventos = [];")
        time.sleep(0.5)
except KeyboardInterrupt:
    signal_handler(None, None)

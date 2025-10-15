import requests
from bs4 import BeautifulSoup

url = "https://infotecnica.coordinador.cl/instalaciones/transformadores-corrientes"
try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())  
except requests.exceptions.RequestException as e:
    print(f"Error al acceder a la URL: {e}")
    exit()
# Extracción de Datos de Transformadores de Corriente?¿?¿?

De momento se usa **Python** para realizar *web scraping* de una tabla de datos de la web de Infotécnica del Coordinador Eléctrico Nacional de Chile

## Pasos a seguir para correr el programa


### 1. Requisitos

**Python 3** instalado.

### 2. Configuración del Entorno Virtual

Se recomienda trabajar dentro de un entorno virtual (`env`) para aislar las dependencias del proyecto.

1.  **Crea** el entorno con:
    ```bash
    python -m venv env
    ```

2.  **Activa** el entorno con:
    * **Windows:**
        ```bash
        .\env\Scripts\activate
        ```
        o con:
        ```bash
        env\Scripts\activate
        ```
        si es que no funca el primero 

### 3. Instalación de Dependencias

Una vez activado el entorno, instala todas las librerías necesarias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
---

### 4. CORRELO  

Una vez instalada las dependencias corre el comando en la terminal:
```bash
python searchcsv.py
```
Esto va a abrir una ventana en chrome, las acciones que realices se guardaran en un json, al volver
a la terminal apreta ctrl + c, haces control c y todo lo que hiciste en el navegador con el mouse se guarda
en el .json

### 5. CORRE tu BOT  básico

con esto lo que automatizaste se va realizar automaticamente 1 vez... de momento
```bash
python bot.py
```
pd: como no caché porque se me olvido lo que había qe hacer, dejo esto por acá dfjdsfkjdsfjsd

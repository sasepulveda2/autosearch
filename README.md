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

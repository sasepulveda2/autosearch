# Automated Search

Currently, **Python** is used to scrape data tables from the Infotécnica portal of Chile's National Electrical Coordinator (*Coordinador Eléctrico Nacional*).

## Getting Started

### 1. Prerequisites

* **Python 3.x** installed on your system.

### 2. Virtual Environment Setup

It is strongly recommended to use a virtual environment (`env`) to isolate project dependencies.

1. **Create** the virtual environment:
```bash
python -m venv env

```


2. **Activate** the environment:
* **Windows (PowerShell):**
```bash
.\env\Scripts\activate

```


* **Windows (Command Prompt):**
```cmd
env\Scripts\activate

```


* **macOS / Linux:**
```bash
source env/bin/activate

```





### 3. Install Dependencies

Once the environment is active, install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt

```

---

### 4. Record Actions

Run the recording script from your terminal:

```bash
python searchcsv.py

```

This will launch a Chrome browser window. Perform the required navigation and clicks manually. Once finished, return to the terminal and press `Ctrl + C` to stop the script and save your recorded browser actions into a `.json` file.

### 5. Run the Automation Bot

To replay the recorded workflow:

```bash
python bot.py

```

This will automatically execute the saved actions sequence.

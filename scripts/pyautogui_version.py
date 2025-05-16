# Steps --------------------------------------------------------------
# 1 - Entrar no site da empresa
# 2 - Fazer login (e-mail e senha)
# 3 - Importar base de dados
# 4 - Cadastrar produtos (todos os produtos)

# Libraries ----------------------------------------------------------
from dotenv import load_dotenv
import pandas as pd
import pyautogui
import time
import os

load_dotenv()

# Script -------------------------------------------------------------
# Variaveis
site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
mouse_position_x = int(os.getenv("MOUSE_POSITION_X_EMAIL", 0))
mouse_position_y = int(os.getenv("MOUSE_POSITION_Y_EMAIL", 0))
mouse_position_x_codigo = int(os.getenv("MOUSE_POSITION_X_CODIGO", 0))
mouse_position_y_codigo = int(os.getenv("MOUSE_POSITION_Y_CODIGO", 0))

pyautogui.PAUSE = 1

# Abrir navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# Digitar o site
pyautogui.write(site)
pyautogui.press("enter")
time.sleep(3)

# Fazer login
pyautogui.click(mouse_position_x, mouse_position_y)

pyautogui.write(login)
pyautogui.press("tab")
pyautogui.write(password)
pyautogui.press("enter")

time.sleep(3)

# Baixar base de dados -----------------------------------------------
file_path = r"C:\Users\bruno\Documents\Documents\Hashtag Treinamentos\Python\Aula 01 - Power UP Automation\database"
file = r'db.csv'
full_path = os.path.join(file_path, file)

db = pd.read_csv(full_path)
print(db)

pyautogui.PAUSE = 0.1

# Cadastrar Produtos -------------------------------------------------
for linha in db.index:
    pyautogui.click(mouse_position_x_codigo, mouse_position_y_codigo)

    codigo = db.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = db.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = db.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(db.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(db.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(db.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(db.loc[linha, "obs"])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press("enter")
    pyautogui.scroll(10000)

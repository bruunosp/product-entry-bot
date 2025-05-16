# Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import pandas as pd
import traceback
import time
import os

load_dotenv()

# Variáveis
site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
login = os.getenv("login")
password = os.getenv("password")

# %%
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = r'..\database\db.csv'
full_path = os.path.abspath(os.path.join(base_path, file_path))

# Configurações do navegador
options = Options()
options.add_argument('--start-maximized')  # Abre em tela cheia

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)  # Esperar até 10s pelos elementos

# Acessar o site
driver.get(site)
print("Site carregado...")

# Fazer login
wait.until(EC.presence_of_element_located(
    (By.NAME, 'email'))).send_keys(login)
wait.until(EC.presence_of_element_located(
    (By.NAME, 'password'))).send_keys(password)
driver.find_element(By.TAG_NAME, 'button').click()
print("Login feito com sucesso!")

# Carregar base de dados
db = pd.read_csv(full_path)
print(f"Base de dados carregada: {len(db)} produtos para cadastrar.")

# Cadastrar produtos
start_time_total = time.time()
errors = []

for linha in db.index:
    try:
        start_time = time.time()

        # Clicar no botão de adicionar produto
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Enviar')]"))).click()

        time.sleep(1)  # Pequena pausa para garantir carregamento

        # Preencher os campos
        driver.find_element(By.NAME, 'codigo').send_keys(
            str(db.loc[linha, "codigo"]))
        driver.find_element(By.NAME, 'marca').send_keys(db.loc[linha, "marca"])
        driver.find_element(By.NAME, 'tipo').send_keys(db.loc[linha, "tipo"])
        driver.find_element(By.NAME, 'categoria').send_keys(
            str(db.loc[linha, "categoria"]))
        driver.find_element(By.NAME, 'preco_unitario').send_keys(
            str(db.loc[linha, "preco_unitario"]))
        driver.find_element(By.NAME, 'custo').send_keys(
            str(db.loc[linha, "custo"]))

        obs = str(db.loc[linha, "obs"])
        if obs != 'nan':
            driver.find_element(By.NAME, 'obs').send_keys(obs)

        # Salvar o produto
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Enviar')]").click()

        end_time = time.time()
        duration = end_time - start_time
        print(
            f"✅ Produto {linha + 1} cadastrado com sucesso! (Tempo: {duration:.2f} segundos)")

        time.sleep(1)  # Pequena pausa antes do próximo

    except Exception as e:
        error_message = traceback.format_exc()
        errors.append((linha, error_message))
        print(
            f"❌ Erro ao cadastrar produto {linha + 1}. Pulando para o próximo...")
        time.sleep(2)  # Pausar mais se der erro

end_time_total = time.time()
total_duration = end_time_total - start_time_total

# Finalizar
print("\n🚀 Cadastro finalizado!")
print(f"Tempo total: {total_duration/60:.2f} minutos.")

if errors:
    print(f"\n⚠️ {len(errors)} erro(s) encontrados durante o cadastro:")
    for linha, error in errors:
        # Mostra a última linha do erro
        print(f"- Produto {linha + 1}: erro -> {error.splitlines()[-1]}")
else:
    print("\n🎯 Todos os produtos cadastrados sem erros!")

# driver.quit()  # NÃO fecha o navegador, como você pediu

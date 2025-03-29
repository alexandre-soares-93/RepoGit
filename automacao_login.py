from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options
import time

# Configuração do driver do Chrome
options = Options()
options.add_argument("--headless")  # Executa o navegador em modo headless (opcional)
driver = webdriver.Chrome(options=options)

try:
    # Acessa o site
    driver.get("http://testfire.net/login.jsp")

    # Localiza os campos de login e senha
    username_field = driver.find_element(By.ID, "uid")
    password_field = driver.find_element(By.ID, "passw")

    # Insere as credenciais
    username_field.send_keys("admin")  # Substitua pelo usuário desejado
    password_field.send_keys("admin")  # Substitua pela senha desejada

    # Envia o formulário
    password_field.send_keys(Keys.RETURN)

    # Aguarda alguns segundos para verificar o resultado
    time.sleep(3)

    # Verifica se o login foi bem-sucedido
    if "Hello Admin User" in driver.page_source:
        print("Login realizado com sucesso!")
    else:
        print("Falha no login.")

finally:
    # Fecha o navegador
    driver.quit()
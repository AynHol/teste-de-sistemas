from selenium import webdriver
import time
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
time.sleep(5)
navegador.maximize_window()
navegador.get("https://www.facebook.com/")
time.sleep(5)
navegador.find_element(By.NAME, "email").send_keys("Nome@gmail.com")
navegador.find_element(By.NAME, "pass").send_keys("123456")
time.sleep(5)
botao_verde = navegador.find_element(By.NAME, "login")
botao_verde.click()
time.sleep(10)
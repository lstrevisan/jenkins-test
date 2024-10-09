import pytest
import time
from selenium import webdriver

chrome_path = 'chrome-win64/chrome.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)

url = 'http://192.168.0.16:8080'

#teste da pagina inicial
driver.get(url)
time.sleep(10)
assert 'Dash' in driver.title
assert 'pagina inicial' in driver.page_source
print('Pagina inicial validada com sucesso')

#teste da pagina do formulario
driver.get(url + '/formulario')
time.sleep(10)
assert 'Dashboard - Formulario' in driver.title
assert 'Formulario' in driver.page_source
print('Pagina de Formulario validada com sucesso')

#teste da pagina de graficos
driver.get(url + '/graficos')
time.sleep(10)
assert 'Dashboard - Graficos' in driver.title
assert 'Graficos' in driver.page_source
print('Pagina de Graficos validada com sucesso')

driver.quit()
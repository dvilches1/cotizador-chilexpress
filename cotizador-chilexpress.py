from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd



def get_chilexpress_prices(kgs):
	#Opciones navegacion
	options = webdriver.ChromeOptions()
	options.add_argument('--start-maximized')
	options.add_argument('--disable-extensions')
	driver_path = "C:/Users/Diego/Downloads/chromedriver.exe"


	origenes = ['Santiago Centro', 'Vina del Mar']
	destinos = ['Antofagasta','Concepcion']
	lista_origen = []
	lista_destinos = []
	lista_kgs = []
	lista_precio = []

	for ciudad in origenes:
		for ciudad2 in destinos:
			for i in range(1,kgs+1):
				with webdriver.Chrome(driver_path, chrome_options = options) as driver:
					#Iniciar en la pantalla 2
					driver.set_window_position(2000,0)
					driver.maximize_window()
					time.sleep(1)

					#Inicializamos el navegador
					driver.get('https://www.chilexpress.cl/cotizador-envios-de-encomiendas-tarifas')
					time.sleep(3)

					origen = Select(driver.find_element_by_xpath('//*[@id="ddlOrigenCotizacion"]'))
					origen.select_by_visible_text(ciudad.upper())

					destino = Select(driver.find_element_by_xpath('//*[@id="ddlDestinoCotizacion"]'))
					destino.select_by_visible_text(ciudad2.upper())

					encomienda = Select(driver.find_element_by_xpath('//*[@id="ddlProductoCotizacion"]'))
					encomienda.select_by_value('3')

					valor = driver.find_element_by_xpath('//*[@id="txtValorProductoDolares"]')
					valor.send_keys(1000)

					kg = driver.find_element_by_id('txtPeso')
					kg.send_keys(i)

					largo = driver.find_element_by_id('txtLargo')
					largo.send_keys(1)

					alto = driver.find_element_by_id('txtAlto')
					alto.send_keys(1)

					ancho = driver.find_element_by_id('txtAncho')
					ancho.send_keys(1)

					cotizar = driver.find_element_by_id('btnSig')
					cotizar.click()

					time.sleep(2)

					cotizacion = driver.find_element_by_id('totalCotizar')
					valor_cot = cotizacion.text
					lista_origen.append(ciudad)
					lista_destinos.append(ciudad2)
					lista_kgs.append(i)
					lista_precio.append(valor_cot.replace('.-',''))
	return  export_csv(lista_origen, lista_destinos, lista_kgs, lista_precio)
		


def export_csv(lista_origen,lista_destinos,lista_kgs,lista_precio):
	df = pd.DataFrame(list(zip(lista_origen,lista_destinos,lista_kgs,lista_precio)), columns = ['Origen','Destino', 'Kgs', 'Precio'])
	df.to_csv('chilexpress.csv', index = False)

get_chilexpress_prices(20)
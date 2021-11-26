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


	origenes = ['Santiago Centro']
	
	# destinos = ['Achao', 'Algarrobo', 'Alto biobio', 'Alto hospicio', 'Alto jahuel', 'Ancud', 'Andacollo', 'Angol', 'Antofagasta', 'Antuco', 'Arauco', 'Arica', 'Artificio', 'Balmaceda', 'Barrancas', 'Batuco', 'Brisas de santo domingo', 'Buin', 'Bulnes', 'Cabrero', 'Cachagua', 'Calama', 'Calbuco', 'Caldera', 'Calera de tango', 'Calle larga', 'Canela', 'Canete', 'Carahue', 'Cartagena', 'Casablanca', 'Castro', 'Catemu', 'Cauquenes', 'Cerrillos', 'Cerro navia', 'Chanaral', 'Chanco', 'Chepica', 'Chicureo', 'Chiguayante', 'Chile chico', 'Chillan', 'Chillan viejo', 'Chimbarongo', 'Chol chol', 'Cholguan', 'Chonchi', 'Cochamo', 'Cochrane', 'Codegua', 'Coelemu', 'Coihueco', 'Coinco', 'Colbun', 'Colina', 'Collipulli', 'Coltauco', 'Combarbala', 'Concepcion', 'Conchali', 'Concon', 'Constitucion', 'Contulmo', 'Copiapo', 'Coquimbo', 'Coronel', 'Coyhaique', 'Cunco', 'Curacautin', 'Curacavi', 'Curaco de velez', 'Curanilahue', 'Curico', 'Dalcahue', 'Dichato', 'Diego de almagro', 'Domeyco', 'Donihue', 'El belloto', 'El bosque', 'El carmen', 'El melon', 'El monte', 'El paico', 'El quisco', 'El salvador', 'El tabito', 'El tabo', 'Empedrado', 'Enea express', 'Entre lagos', 'Estacion central', 'Estacion paipote', 'Florida', 'Freire', 'Freirina', 'Fresia', 'Frutillar', 'Futrono', 'Galvarino', 'Gorbea', 'Graneros', 'Hijuelas', 'Hornopiren', 'Hualaihue', 'Hualane', 'Hualpen', 'Hualqui', 'Huasco', 'Huechuraba', 'Huepil', 'Illapel', 'Independencia', 'Internacional', 'Iquique', 'Isla de maipo', 'Isla negra', 'La calera', 'La cisterna', 'La cruz', 'La florida', 'La granja', 'La junta', 'La ligua', 'La palma', 'La paz', 'La pintana', 'La reina', 'La serena', 'La union', 'Lago ranco', 'Laja', 'Lampa', 'Lanco', 'Las cabras', 'Las canchas', 'Las condes', 'Las cruces', 'Las tacas', 'Lautaro', 'Lebu', 'Licanray', 'Licanten', 'Limache', 'Linares', 'Lirquen', 'Litueche', 'Llanquihue', 'Llay llay', 'Llo lleo', 'Lo barnechea', 'Lo espejo', 'Lo miranda', 'Lo prado', 'Lolol', 'Loncoche', 'Longavi', 'Longovilo', 'Lonquen', 'Lonquimay', 'Lontue', 'Los alamos', 'Los andes', 'Los angeles', 'Los lagos', 'Los muermos', 'Los vilos', 'Lota', 'Lumaco', 'Machali', 'Macul', 'Mafil', 'Maipu', 'Maitencillo', 'Malloa', 'Malloco', 'Marchigue', 'Maria elena', 'Mariquina', 'Maule', 'Maullin', 'Mejillones', 'Melipilla', 'Mininco', 'Molina', 'Monte patria', 'Mulchen', 'Nacimiento', 'Nancagua', 'Natales', 'Navidad', 'Negrete', 'Ninhue', 'Niquen', 'Nogales', 'Nos', 'Nueva aldea', 'Nueva imperial', 'Nunoa', 'Olivar', 'Olmue', 'Osorno', 'Ovalle', 'Padre hurtado', 'Padre las casas', 'Paiguano', 'Paillaco', 'Paine', 'Paipote', 'Palmilla', 'Panguipulli', 'Papudo', 'Paredones', 'Pargua', 'Parral', 'Pedro aguirre cerda', 'Pelequen', 'Pelluhue', 'Pemuco', 'Penablanca', 'Penaflor', 'Penalolen', 'Pencahue', 'Penco', 'Peralillo', 'Peumo', 'Pichidegua', 'Pichilemu', 'Pinto', 'Pirque', 'Pitrufquen', 'Placilla quinta region', 'Placilla sexta region', 'Pocochay', 'Porvenir', 'Pozo almonte', 'Providencia', 'Puchuncavi', 'Pucon', 'Pudahuel', 'Pueblo seco', 'Puente alto', 'Puerto aysen', 'Puerto chacabuco', 'Puerto cisnes', 'Puerto montt', 'Puerto octay', 'Puerto varas', 'Punitaqui', 'Punta arenas', 'Puren', 'Purranque', 'Putaendo', 'Puyehue', 'Quellon', 'Quemchi', 'Quepe', 'Quilicura', 'Quilleco', 'Quillon', 'Quillota', 'Quilpue', 'Quinta de tilcoco', 'Quinta normal', 'Quintero', 'Quirihue', 'Quiriquina', 'Rancagua', 'Recoleta', 'Renaca', 'Renaico', 'Renca', 'Rengo', 'Requinoa', 'Retiro', 'Rio bueno', 'Rio ibanez', 'Rio negro', 'Romeral', 'Rosario', 'Saavedra', 'Salamanca', 'San antonio', 'San bernardo', 'San carlos', 'San clemente', 'San esteban', 'San felipe', 'San fernando', 'San francisco de limache', 'San francisco de mostazal', 'San ignacio', 'San javier', 'San joaquin', 'San jose de la mariquina', 'San miguel', 'San nicolas', 'San pablo', 'San pedro', 'San pedro de atacama', 'San pedro de la paz', 'San pedro quinta region', 'San rafael', 'San ramon', 'San rosendo', 'San sebastian', 'San vicente de tagua tagua', 'Santa barbara', 'Santa cruz', 'Santa maria', 'Santo domingo', 'Sierra gorda', 'Talagante', 'Talca', 'Talcahuano', 'Taltal', 'Temuco', 'Teno', 'Teodoro schmidt', 'Tierra amarilla', 'Til til', 'Tocopilla', 'Tome', 'Traiguen', 'Tucapel', 'Valdivia', 'Vallenar', 'Valparaiso', 'Victoria', 'Vicuna', 'Vilcun', 'Villa alegre', 'Villa alemana', 'Villarrica', 'Vina del mar', 'Vitacura', 'Yumbel', 'Yungay', 'Zapallar']
	#destinos = ['Arica', 'Iquique', 'Alto Hospicio', 'Antofagasta', 'Calama', 'Copiapo', 'Caldera', 'Coquimbo', 'Ovalle', 'Vina del Mar', 'Valparaiso', 'San Felipe', 'Los Andes', 'Rancagua', 'San Fernando', 'Santa Cruz', 'Curico', 'Talca', 'Linares', 'Chillan', 'Los Angeles', 'Concepcion', 'Lota', 'Molina', 'Victoria', 'Angol', 'Temuco', 'Villarrica', 'Valdivia', 'Osorno', 'Puerto Varas', 'Puerto Montt', 'Coyhaique', 'Puerto Aysen', 'Punta Arenas', 'Santiago Centro', 'Maipu', 'La Florida', 'Las Condes', 'Vitacura', 'Lo Barnechea', 'Providencia', 'Nunoa', 'Macul', 'Puente Alto', 'Quilicura', 'Huechuraba', 'San Miguel', 'San Joaquin', 'San Bernardo', 'Colina', 'Chicureo', 'Penaflor', 'Calera de tango', 'Buin', 'Vallenar', 'Los Vilos', 'Castro']
	
	#destinos = ['Arica', 'Iquique', 'Alto Hospicio', 'Antofagasta', 'Calama']
	#destinos = ['Copiapo', 'Caldera', 'Coquimbo', 'Ovalle']
	#destinos = ['Vina del Mar', 'Valparaiso', 'San Felipe', 'Los Andes', 'Rancagua', 'San Fernando', 'Santa Cruz']
	#destinos = ['Curico', 'Talca', 'Linares', 'Chillan', 'Los Angeles', 'Concepcion', 'Lota', 'Molina', 'Victoria', 'Angol']
	#destinos = ['Temuco', 'Villarrica', 'Valdivia', 'Osorno', 'Puerto Varas', 'Puerto Montt', 'Coyhaique', 'Puerto Aysen', 'Punta Arenas']
	destinos = ['Santiago Centro', 'Maipu', 'La Florida', 'Las Condes', 'Vitacura', 'Lo Barnechea', 'Providencia', 'Nunoa', 'Macul', 'Puente Alto','Quilicura', 'Huechuraba', 'San Miguel', 'San Joaquin', 'San Bernardo', 'Colina', 'Chicureo', 'Penaflor', 'Calera de tango', 'Buin', 'Vallenar', 'Los Vilos', 'Castro']


	lista_origen = []
	lista_destinos = []
	lista_kgs = []
	lista_cour = []
	lista_expreso = []

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

					time.sleep(4)
					
					try:
						click_cour = driver.find_element_by_id('lebel-valores-12')
						click_cour.click()
						cotizacion_cour = driver.find_element_by_id('totalCotizar')
						valor_cour = cotizacion_cour.text

					except:
						valor_cour = '0.-'

					try:
						click_expreso = driver.find_element_by_id('lebel-valores-13')
						click_expreso.click()
						cotizacion_expreso = driver.find_element_by_id('totalCotizar')
						valor_expreso = cotizacion_expreso.text
						
					except:
						valor_expreso= '0.-'

					lista_origen.append(ciudad)
					lista_destinos.append(ciudad2)
					lista_kgs.append(i)
					lista_cour.append(valor_cour.replace('.-',''))
					lista_expreso.append(valor_expreso.replace('.-',''))
	return  export_csv(lista_origen, lista_destinos, lista_kgs, lista_cour, lista_expreso)
		


def export_csv(lista_origen,lista_destinos,lista_kgs,lista_cour,lista_expreso):
	df = pd.DataFrame(list(zip(lista_origen,lista_destinos,lista_kgs,lista_cour,lista_expreso)), columns = ['Origen','Destino', 'Kgs', 'Precio Courier', 'Precio Expreso'])
	df.to_csv('chilexpress.csv', index = False)

get_chilexpress_prices(25)
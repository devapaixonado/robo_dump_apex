from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Painel:

    def __init__(self): pass
    
    def clica_botao_exportar(self, browser, xpath):
        btn_exportar = WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        btn_exportar.click()
 

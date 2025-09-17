from time import time, sleep
import logging
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter("ignore", InsecureRequestWarning)

from src.config import *
from src.utils import scraping_utils, helpers
from src.pages import Painel

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

class RunScraping():

    def __init__(self) -> None:
        """
            Inicializa a classe RunScraping, obtendo uma instância do navegador.

            Args:
                self: Instância da classe.
        """
        self.browser = Browser().get_browser()
        
    def executa_scraping(self) -> None:
        self.browser.get("https://investsuspaineis.saude.gov.br/extensions/CGIN_ONE/CGIN_ONE.html")  
        painel = Painel()
        painel.clica_botao_exportar(self.browser)
        helpers.renomeia_arquivo()
        
    def fecha_browser(self) -> None:
        """
            Fecha o navegador.

            Args:
                self: Instância da classe.
        """
        sleep(5)
        self.browser.close()

if __name__ == '__main__':
    start_time = time()

    run_sc = RunScraping()
    run_sc.executa_scraping()
    run_sc.fecha_browser()
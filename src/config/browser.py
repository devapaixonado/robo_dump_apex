

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service
import os


class Browser:
    def __init__(self) -> None:
        PATH_DOWNLOAD = 'J:\Repositorio_QLIK\APEX\ROBO_DUMP_PF'
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": PATH_DOWNLOAD,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.default_content_setting_values.automatic_downloads": 1
        }
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        os.environ["WDM_SSL_VERIFY"] = "0"

        # Força o webdriver-manager a baixar a versão correta
        service = Service(
            ChromeDriverManager(driver_version="139.0.7258.139").install()
        )
        self.browser = webdriver.Chrome(service=service, options=chrome_options)

    def get_browser(self) -> webdriver.Chrome:
        return self.browser

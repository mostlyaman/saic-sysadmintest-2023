from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def get_chrome():
    chrome_options = ChromeOptions()
    chrome_options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def get_edge():
    edge_options = EdgeOptions()
    edge_options.headless = True
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    return driver

def get_firefox():
    firefox_options = FirefoxOptions()
    firefox_options.headless = True
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return driver
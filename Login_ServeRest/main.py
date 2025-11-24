import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Login_ServeRest import data
from page import ServeRestPage

class TestServeRest:

    def test_set_login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.ServeRest_URL)
        self.serveRest = ServeRestPage(self.driver)
        email = data.EMAIL
        password = data.PASSWORD
        self.serveRest.set_login(email, password)
        assert self.serveRest.get_email_field() == email
        assert self.serveRest.get_password_field() == password
        assert self.serveRest.get_inicial_page() == 'Serverest Store'
        time.sleep(5)
        self.driver.quit()

    def test_set_login_invalido(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.ServeRest_URL)
        self.serveRest = ServeRestPage(self.driver)
        email = data.EMAIL
        invalid_password = data.INVALID_PASSWORD
        self.serveRest.set_login(email, invalid_password)
        assert self.serveRest.get_email_field() == email
        assert self.serveRest.get_password_field() == invalid_password
        assert self.serveRest.get_error_message() == 'Email e/ou senha inválidos'
        time.sleep(5)
        self.driver.quit()

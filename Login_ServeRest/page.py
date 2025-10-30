from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ServeRestPage:

    # Localizadores
    email_field = (By.ID, 'email')
    password_field = (By.ID, 'password')
    enter_button = (By.XPATH, '//button[contains(text(), "Entrar")]')

    def __init__(self, driver):
        self.driver = driver

    def _wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def set_enter(self):
        self.driver.find_element(*self.enter_button).click()

    def set_login(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.set_enter()

    def get_inicial_page(self):
        element = self._wait_for_visible((By.XPATH, '//h1[contains(text(), "Serverest Store")]'))
        return element.text


    def get_email_field(self):
        return self.driver.find_element(*self.email_field).get_attribute('value')

    def get_password_field(self):
        return self.driver.find_element(*self.password_field).get_attribute('value')
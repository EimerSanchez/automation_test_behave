from selenium.webdriver.common.by import By


class HomeWebElements:
    where_label = (By.XPATH, "//h2[contains(text(),'Busca en cientos de webs de vuelos a la vez.')]")
    signin_button = (By.XPATH, "//span[contains(text(),'Iniciar sesión')]")
    search_button = (By.CSS_SELECTOR, "//span[contains(text(),'Buscar')]")
    name = (By.TAG_NAME, "type")
    name_tag_input = (By.TAG_NAME, "input")
    name_dropdown_column_input = (By.TAG_NAME, "input")
    search_tag_input = (By.TAG_NAME, "input")
    cancel_button = (By.TAG_NAME, "button")
    create_column_disabled_button = (By.TAG_NAME, "button")



    @staticmethod
    def getElementOption(option_name):
        option_locator = (By.XPATH, f"//div[text()='{option_name}']")
        return option_locator

import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_HELLO_LOGIN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_POST_TITLE = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[1]/div/label/input')
    LOCATOR_POST_DESCRIPTION = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea')
    LOCATOR_POST_CONTENT = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea')
    LOCATOR_EXPECTED_TITLE = (By.XPATH, """/html/body/div[1]/main/div/div[1]/h1""")
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, '#create-btn')
    LOCATOR_SAVE_POST_BTN = (By.CSS_SELECTOR, '.mdc-button__label')
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_YOUR_EMAIL = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_MESSAGE = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_SEND_MESSAGE_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_login_text(self):
        element_success_login = self.find_element(TestSearchLocators.LOCATOR_HELLO_LOGIN)
        return element_success_login.text

    def new_post_btn(self):
        logging.info("New post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def new_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def new_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)

    def new_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_POST_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_POST_CONTENT)
        login_field.clear()
        login_field.send_keys(word)

    def post_save_button(self):
        logging.info("Save new post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def expected_title(self):
        expected_title = self.find_element(TestSearchLocators.LOCATOR_EXPECTED_TITLE)
        return expected_title.text

    def new_contact_btn(self):
        logging.info("Contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def your_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_YOUR_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME)
        name_field.clear()
        name_field.send_keys(word)

    def your_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_YOUR_EMAIL[1]}")
        email_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL)
        email_field.clear()
        email_field.send_keys(word)

    def message(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_MESSAGE[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_MESSAGE)
        content_field.clear()
        content_field.send_keys(word)

    def contact_us_btn(self):
        logging.info("Contact us button")
        self.find_element(TestSearchLocators.LOCATOR_SEND_MESSAGE_BTN).click()

    def alert(self):
        alert = self.driver.switch_to.alert
        return alert.text

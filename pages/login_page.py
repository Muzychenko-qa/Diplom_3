import allure

from pages.base_page import BasePage
from locators.login_page_locators import *
from tests_data import BASE_CREDENTIAL


class LoginPage (BasePage):

    @allure.step("Нажать 'Восстановить пароль'")
    def click_forgot_password(self):
        self.wait_and_find_element(BUTTON_LINK_FORGOT_PASSWORD).click()
        self.wait_for_loading_to_disappear()

    def wait_for_loading_overlay_invisibility(self):
        self.wait_for_loading_to_disappear()

    @allure.step("Ввод email в поле ввода")
    def input_email(self):
        self.wait_and_find_element(FILED_EMAIL).send_keys(BASE_CREDENTIAL)

    @allure.step("Ввод пароля в поле ввода")
    def input_password(self):
        self.wait_and_find_element(FILED_PASSWORD).send_keys(BASE_CREDENTIAL)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_button_forgot_password(self):
        self.wait_and_find_element(BUTTON_FORGOT_PASSWORD).click()
        self.wait_for_loading_to_disappear()

    @allure.step("Ожидание кнопки 'Восстановить'")
    def check_button_forgot_password(self):
        forgot_password_button = self.wait_and_find_element(BUTTON_FORGOT_PASSWORD)
        return forgot_password_button

    @allure.step("Клик по иконке 'Глаза'")
    def click_show_password(self):
        self.wait_and_find_element(SHOW_PASSWORD).click()

    @allure.step("Получить тип поля ввода пароля")
    def get_password_input_type(self):
        return self.wait_and_find_element(FILED_PASSWORD).get_attribute("type")

    @allure.step("Нажать на кнопку 'Войти'")
    def click_button_login(self):
        self.wait_and_find_element(BUTTON_LOGIN).click()

    @allure.step("Ожидание кнопки 'Оформить заказ'")
    def check_button_save(self):
        save_button = self.wait_and_find_element(BUTTON_SAVE)
        return save_button

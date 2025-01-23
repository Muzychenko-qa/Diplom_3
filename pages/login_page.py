import allure

from locators.base_page_locators import *
from locators.login_page_locators import *
from locators.profile_page_locators import BUTTON_LOGIN, BUTTON_PLACE_ORDER
from pages.base_page import BasePage
from tests_data import BASE_EMAIL, BASE_PASSWORD


class LoginPage (BasePage):

    @allure.step("Нажать 'Восстановить пароль'")
    def click_forgot_password(self):
        self.wait_and_find_element(BUTTON_LINK_FORGOT_PASSWORD).click()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def wait_for_loading_overlay_invisibility(self):
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    @allure.step("Ввод email в поле ввода")
    def input_email(self, email):
        self.wait_and_find_element(FILED_EMAIL).send_keys(email)

    @allure.step("Ввод пароля в поле ввода")
    def input_password(self, password):
        self.wait_and_find_element(FILED_PASSWORD).send_keys(password)


    @allure.step("Нажать кнопку 'Восстановить'")
    def click_button_forgot_password(self):
        self.wait_and_find_element(BUTTON_FORGOT_PASSWORD).click()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    @allure.step("Ожидание кнопки 'Восстановить'")
    def check_button_forgot_password(self):
        forgot_password_button = self.wait_and_find_element(BUTTON_FORGOT_PASSWORD)
        return forgot_password_button

    @allure.step("Клик по иконке 'Глаза'")
    def click_show_password(self):
        self.wait_and_find_element(SHOW_PASSWORD).click()

    @allure.step("Нажать на кнопку 'Войти'")
    def click_button_login(self):
        self.wait_and_find_element(BUTTON_LOGIN).click()

    @allure.step("Ожидание кнопки 'Оформить заказ'")
    def check_place_order(self):
        place_order_button = self.wait_and_find_element(BUTTON_PLACE_ORDER)
        return place_order_button

    @allure.step("Ожидание кнопки 'Оформить заказ'")
    def check_button_save(self):
        save_button = self.wait_and_find_element(BUTTON_SAVE)
        return save_button

    def input_credentials(self):
        self.input_email(BASE_EMAIL)
        self.input_password(BASE_PASSWORD)

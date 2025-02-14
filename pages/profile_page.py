import allure

from locators.profile_page_locators import *
from pages.base_page import BasePage


class ProfilePage (BasePage):

    @allure.step("Нажать кнопку Личный кабинет")
    def click_button_header_profile(self):
        self.wait_and_find_element(BUTTON_LINK_PROFILE).click()
        self.wait_for_loading_to_disappear()

    @allure.step("Нажать кнопку История заказов")
    def click_order_history(self):
        self.wait_for_loading_to_disappear()
        self.wait_and_find_element(BUTTON_ORDER_HISTORY).click()

    @allure.step("Нажать кнопку Выйти")
    def click_logout_profile(self):
        self.wait_for_loading_to_disappear()
        self.wait_and_find_element(BUTTON_LOGOUT_PROFILE).click()

    @allure.step("Ожидание окна Заказ создан - Ваш заказ начали готовить")
    def check_form_login(self):
        return self.wait_and_find_element(FORM_LOGIN)

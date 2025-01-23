import allure

from locators.base_page_locators import *
from locators.order_feed_locators import *
from locators.profile_page_locators import *
from pages.base_page import BasePage


class DesignerPage (BasePage):

    @allure.step("Нажать на ингрдиент")
    def click_ingredient(self):
        self.wait_and_find_element(COUNTER_INGREDIENT).click()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    @allure.step("Закрыть информацию об ингредиенте")
    def click_close_info_ingredient(self):
        self.wait_and_find_element(BUTTON_CLOSE_INFO_INGREDIENT).click()

    @allure.step("Перенос ингридиента в Заказ")
    def move_ingredient(self):
        ingredient_element = self.wait_and_find_element(ELEMENT_INGREDIENT)
        order_area = self.wait_and_find_element(SPACE_ORDER)
        self.drag_and_drop(ingredient_element, order_area)
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    @allure.step("Нажать кнопку Оформить заказ")
    def click_place_order(self):
        self.wait_and_find_element(BUTTON_PLACE_ORDER).click()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    @allure.step("Нажать кнопку Закрыть окно Заказ создан")
    def click_close_place_order(self):
        self.wait_and_find_element(BUTTON_CLOSE_WINDOW_START_ORDER).click()

    @allure.step("Создание заказа")
    def create_order(self):
        self.open_base_page()
        self.move_ingredient()
        self.click_place_order()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)
        new_number_order = self.get_text(NUMBER_INFO_ORDER)
        self.click_close_place_order()
        return new_number_order

    @allure.step("Ожидание Детали ингредиента")
    def check_info_ingredient(self):
        return self.wait_and_find_element(INFO_INGREDIENT)

    def check_details_ingredient(self):
        return self.wait_invisibility_element(INFO_INGREDIENT)

    def get_ingredient_counter_text(self):
        return self.get_text(COUNTER_INGREDIENT)


    @allure.step("Ожидание окна Заказ создан - Ваш заказ начали готовить")
    def check_window_start_order(self):
        return self.wait_and_find_element(WINDOW_START_ORDER)
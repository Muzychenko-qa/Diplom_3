import allure

from locators.order_feed_locators import *
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Проверить исчезновение заголовка 'Все текущие заказы готовы!'")
    def wait_for_orders_ready_invisibility(self):
        self.wait_invisibility_element(ALL_ORDERS_READY)

    @allure.step("Получить текст текущих заказов")
    def get_orders_in_work_text(self):
        return self.get_text(ORDERS_IN_WORK)

    @allure.step("Нажать ссылку Восстановить пароль")
    def click_order_in_history(self):
        self.wait_and_find_element(NUMBERS_HISTORY_ORDER).click()

    @allure.step("Получить значение счётчика 'Выполнено за всё время'")
    def get_all_time_orders_count(self):
        return int(self.get_text(ALL_TIME_ORDERS))

    @allure.step("Получить значение счётчика 'Выполнено за сегодня'")
    def get_day_time_orders_count(self):
        return int(self.get_text(DAY_ORDERS))

    @allure.step("Нажать кнопку Личный кабинет")
    def click_order_history(self):
        self.wait_and_find_element(BUTTON_ORDER_HISTORY_FOR_ORDER_FEED).click()

    @allure.step("Получить номер последнего заказа из История заказов")
    def get_last_order_history(self):
        return self.find_all_elements(NUMBERS_HISTORY_ORDER)[-1].text

    @allure.step("Проверить существование последнего номера заказа в Ленте заказов")
    def get_check_number_order(self, last_order):
        locator = (LAST_ORDER_NUMBER[0], LAST_ORDER_NUMBER[1].format(last_order=last_order))
        return self.wait_and_find_element(locator)

    @allure.step("Ожидание Окно информации о заказе")
    def check_window_info_order(self):
        return self.wait_and_find_element(INFO_ORDER)


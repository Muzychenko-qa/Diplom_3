import allure

from pages.designer_page import DesignerPage
from urls import *

@allure.suite("Проверка основного функционала (Конструктор)")
class TestDesignerFunctional:

    @allure.title('Тест переход по клику на «Конструктор»')
    def test_click_button_header_designer_is_opened_designer_page(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_order_page()
        designer_page.click_constructor_button()
        assert designer_page.get_current_page_url() == BASE_URL + "/"

    @allure.title('Тест переход по клику на «Лента заказов»')
    def test_click_button_header_order_feed_is_opened_order_feed(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.click_order_feed_button()
        assert designer_page.get_current_page_url() == ORDER_FEED_PAGE_URL

    @allure.title('Тест если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient_is_opened_info_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.click_ingredient()
        assert designer_page.check_info_ingredient()

    @allure.title('Тест всплывающее окно закрывается кликом по крестику')
    def test_click_close_info_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.click_ingredient()
        designer_page.check_info_ingredient()
        designer_page.click_close_info_ingredient()
        assert designer_page.wait_invisibility_details_ingredient()

    @allure.title('Тест при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_is_change_counter_ingredient(self, driver):
        designer_page = DesignerPage(driver)
        designer_page.open_base_page()
        designer_page.move_ingredient()
        assert designer_page.get_ingredient_counter_text() == "2"

    @allure.title('Тест залогиненный пользователь может оформить заказ')
    def test_login_user_can_place_order(self, authorization):
        designer_page = DesignerPage(authorization)
        designer_page.open_base_page()
        designer_page.move_ingredient()
        designer_page.click_place_order()
        assert designer_page.check_window_start_order()

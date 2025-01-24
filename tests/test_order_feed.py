import allure

from pages.designer_page import DesignerPage
from pages.order_feed_page import OrderFeedPage

@allure.suite("Проверка основного функционала (Конструктор)")
class TestOrderFeed:

    @allure.title('Тест после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_have_in_work(self, authorization):
        designer_page = DesignerPage(authorization)
        order_feed_page = OrderFeedPage(authorization)
        new_number_order = designer_page.create_order()
        designer_page.click_order_feed_button()

        order_feed_page.wait_for_orders_ready_invisibility()
        assert new_number_order in order_feed_page.get_orders_in_work_text()

    @allure.title('Тест если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_is_opened_order_info(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.open_order_page()
        order_feed_page.click_order_in_history()
        assert order_feed_page.check_window_info_order()

    @allure.title('Тест заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_history_have_too_feed(self, authorization):
        order_feed_page = OrderFeedPage(authorization)
        order_feed_page.navigate_to_profile()
        order_feed_page.click_order_history()
        order_from_history = order_feed_page.get_last_order_history()
        order_feed_page.open_order_page()
        assert order_feed_page.get_check_number_order(order_from_history)

    @allure.title('Тест при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_change_all_time_order(self, authorization):
        designer_page = DesignerPage(authorization)
        order_feed_page = OrderFeedPage(authorization)
        order_feed_page.open_order_page()
        old_all_time_order = order_feed_page.get_all_time_orders_count()
        designer_page.create_order()
        order_feed_page.open_order_page()
        new_all_time_order = order_feed_page.get_all_time_orders_count()
        assert new_all_time_order > old_all_time_order

    @allure.title('Тест при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_change_day_time_order(self, authorization):
        designer_page = DesignerPage(authorization)
        order_feed_page = OrderFeedPage(authorization)
        order_feed_page.open_order_page()
        old_day_time_order = order_feed_page.get_day_time_orders_count()
        designer_page.create_order()
        order_feed_page.open_order_page()
        new_day_time_order = order_feed_page.get_day_time_orders_count()
        assert new_day_time_order > old_day_time_order

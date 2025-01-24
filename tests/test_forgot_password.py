import allure
from pages.login_page import LoginPage
from urls import *

@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title('Тест переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_button_open_forgot_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.wait_for_loading_overlay_invisibility()
        login_page.click_forgot_password()
        assert login_page.check_button_forgot_password()

    @allure.title('Тест ввод почты и клик по кнопке «Восстановить»')
    def test_send_email_open_reset_password(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_password_recovery()
        login_page.input_email()
        login_page.click_button_forgot_password()
        assert login_page.check_button_save() and login_page.get_current_page_url() == RESET_PASSWORD_PAGE_URL

    @allure.title('Тест клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_button_show_password(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate_to_password_recovery()
        login_page.input_email()
        login_page.click_button_forgot_password()
        login_page.check_button_save()
        login_page.input_password()
        login_page.click_show_password()
        assert login_page.get_password_input_type() == "text"
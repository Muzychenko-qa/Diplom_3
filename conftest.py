import pytest
from selenium import webdriver
from pages.login_page import LoginPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.input_email()
    login_page.input_password()
    login_page.click_button_login()
    login_page.check_place_order()
    return driver


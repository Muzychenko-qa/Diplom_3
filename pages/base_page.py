from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import *
from urls import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 200).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def wait_invisibility_element(self, locator):
        return WebDriverWait(self.driver, 40).until(expected_conditions.invisibility_of_element_located(locator))

    def click_constructor_button(self):
        self.wait_and_find_element(BUTTON_HEADER_DESIGNER).click()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def click_order_feed_button(self):
        self.wait_and_find_element(BUTTON_HEADER_ORDER_FEED).click()
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def navigate_to_profile(self):
        self.driver.get(PROFILE_PAGE_URL)
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def navigate_to_password_recovery(self):
        self.driver.get(FORGOT_PASSWORD_PAGE_URL)
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def find_all_elements(self, locator):
        self.wait_and_find_element(locator)
        return self.driver.find_elements(*locator)

    def get_text(self, locator):
        text = self.wait_and_find_element(locator).text
        return text

    def get_type_input(self, locator):
        text = self.wait_and_find_element(locator).get_attribute("type")
        return text

    def get_current_page_url(self):
        return self.driver.current_url

    def drag_and_drop(self, element, target):
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
            """,
            element,
            target
        )

    def open_base_page(self):
        self.driver.get(BASE_URL)
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def open_login_page(self):
        self.driver.get(LOGIN_PAGE_URL)
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)

    def open_order_page(self):
        self.driver.get(ORDER_FEED_PAGE_URL)
        self.wait_invisibility_element(LOADING_MODAL_OVERLAY)
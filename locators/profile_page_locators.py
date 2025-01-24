from selenium.webdriver.common.by import By

# Кнопка Личный кабинет
BUTTON_LINK_PROFILE = (By.XPATH, '//a[@href="/account"]')
# Форма войти
FORM_LOGIN = (By.XPATH, '//*[contains(@class, "Auth_login__")]')
# Кнопка История заказов
BUTTON_ORDER_HISTORY = (By.XPATH, '//a[@href="/account/order-history"]')
# Кнопка нажатая История заказов
SELECTED_BUTTON_ORDER_HISTORY = (By.XPATH, '//a[@href="/account/order-history" and contains(@class,"Account_link_active")]')
# Кнопка нажатая Выйти
BUTTON_LOGOUT_PROFILE = (By.XPATH, '//button[text()="Выход"]')
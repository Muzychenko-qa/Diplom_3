from selenium.webdriver.common.by import By

# Кнопка Конструктор
BUTTON_HEADER_DESIGNER = (By.XPATH, '//*[contains(text(),"Конструктор")]')
# Кнопка Войти в аккаунт
BUTTON_LOGIN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')
# Кнопка Лента заказов
BUTTON_HEADER_ORDER_FEED = (By.XPATH, '//a[@href="/feed"]')
# Список ленты заказов
LIST_ORDER_FEED = (By.XPATH, '//*[contains(@class,"OrderFeed_list__")]')
# Ожидание выполнения запроса
LOADING_MODAL_OVERLAY = (By.XPATH, '//div[contains(@class,"Modal_modal__loading__")]')
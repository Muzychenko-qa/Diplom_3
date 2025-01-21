from selenium.webdriver.common.by import By

# Кнопка Конструктор
BUTTON_HEADER_DESIGNER = (By.XPATH, '//*[contains(text(),"Конструктор")]')
# Кнопка Войти в аккаунт
BUTTON_LOGIN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')
# Кнопка Лента заказов
BUTTON_HEADER_ORDER_FEED = (By.XPATH, '//a[@href="/feed"]')
# # Заголовок 'Соберите бургер'
# HEADER_TEXT_COLLECT_BURGER = (By.XPATH, ' //h1[text()="Соберите бургер"]')
# Список ленты заказов
LIST_ORDER_FEED = (By.XPATH, '//*[contains(@class,"OrderFeed_list__")]')
# Детали ингредиента
INFO_INGREDIENT = (By.XPATH, '//h2[text()="Детали ингредиента"]')
# Ингредиент - Счётчик ингредиента
ELEMENT_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]')
# Ингредиент - Счётчик ингредиента
COUNTER_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]//*[contains(@class,"counter_default__")]')
# Кнопка Закрыть - Детали ингредиента
BUTTON_CLOSE_INFO_INGREDIENT  = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]/..//..//button[contains(@class,"Modal_modal__close")]')
# Простарнство сбора заказа
SPACE_ORDER = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')
# Заказ создан - Ваш заказ начали готовить
WINDOW_START_ORDER = (By.XPATH, '//*[text()="Ваш заказ начали готовить"]')
# Кнопка Заказ создан - Ваш заказ начали готовить
BUTTON_CLOSE_WINDOW_START_ORDER = (By.XPATH, '//*[contains(text(),"Ваш заказ начали готовить")]/..//..//..//button[contains(@class,"Modal_modal__close")]')
# Ожидание выполнения запроса
LOADING_MODAL_OVERLAY = (By.XPATH, '//div[contains(@class,"Modal_modal__loading__")]')
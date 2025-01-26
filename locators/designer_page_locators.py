
from selenium.webdriver.common.by import By

# Ингредиент - Счётчик ингредиента
COUNTER_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]//*[contains(@class,"counter_default__")]')
# Кнопка Закрыть - Детали ингредиента
BUTTON_CLOSE_INFO_INGREDIENT  = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]/..//..//button[contains(@class,"Modal_modal__close")]')
# Ингредиент - Счётчик ингредиента
ELEMENT_INGREDIENT = (By.XPATH, '//*[contains(@class,"BurgerIngredient_ingredient__")]')
# Пространство сбора заказа
SPACE_ORDER = (By.XPATH, '//ul[contains(@class,"BurgerConstructor_basket")]')
# Кнопка Заказ создан - Ваш заказ начали готовить
BUTTON_CLOSE_WINDOW_START_ORDER = (By.XPATH, '//*[contains(text(),"Ваш заказ начали готовить")]/..//..//..//button[contains(@class,"Modal_modal__close")]')
# Детали ингредиента
INFO_INGREDIENT = (By.XPATH, '//h2[text()="Детали ингредиента"]')
# Заказ создан - Ваш заказ начали готовить
WINDOW_START_ORDER = (By.XPATH, '//*[text()="Ваш заказ начали готовить"]')
# Номер созданного заказа в окне информации о заказе
NUMBER_INFO_ORDER = (By.XPATH, '//*[contains(@class,"Modal_modal__title__")]')
# Кнопка Оформить заказ
BUTTON_PLACE_ORDER = (By.XPATH, '//button[contains(text(),"Оформить заказ")]')
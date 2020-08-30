from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")               # форма авторизации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")         # форма регистрации
    REGISTER_EMAIL = (By.ID, "id_registration-email")           # поле ввода email
    REGISTER_PASSWORD1 = (By.ID, "id_registration-password1")   # поле ввода пароля
    REGISTER_PASSWORD2 = (By.ID, "id_registration-password2")   # поле для повторного ввода пароля
    REGISTER_SUBMIT = (By.NAME, "registration_submit")          # кнопка Зарегистрироваться


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")                            # добавить в корзину
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")                               # название книги
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")                    # цена книги
    BOOK_NAME_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")       # название добавленной книги
    BOOK_PRICE_BASKET = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")      # цена добавленно книги
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")               # SUCCESS_MESSAGE


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")                   # ссылка на логин
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")       # не существующая ссылка на логин
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")   # ссылка на Перейти в корзину
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")                     # иконка пользователя


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")       # список продуктов
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")   # сообщение что корзина пустая

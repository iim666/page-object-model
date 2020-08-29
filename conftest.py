import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: ru, en. Default is en")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    # Время чтбы визуально проверить, что фраза на кнопке добавления в корзину на необходимом языке
    print("\nquit browser..")
    browser.quit()

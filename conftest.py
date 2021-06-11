import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help="Choose your browser. But sorry, only Chrome is available)")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es/en/fr/ru")

available_languages = ("es", "en", "fr", "ru", )

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if language not in available_languages:
        raise Exception("This kind of laguage is not supported")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    if browser_name == 'Chrome':
        print("/n everything good, run Chrome")
        browser = webdriver.Chrome(options=options)
    else:
        raise Exception("Sorry, but this browser is not supported at the moment")
    
    yield browser
    
    print("/n test complete, close browser")
    browser.quit()
from selenium import webdriver


class BasePage:
    
    def __init__(self, browser: webdriver.Chrome, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
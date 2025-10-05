import json
from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page: Page, data_file="test data/login_page_testData.json"):
        self.page = page
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")

        with open(data_file, 'r') as file:
            self.test_data = json.load(file)

    def navigateToLoginPage(self, url=None):
        url = url or self.test_data.get("url")
        self.page.goto(url)

    def enterValidCredentials(self, username=None, password=None):
        user = username or self.test_data.get("username")
        pwd = password or self.test_data.get("password") 
        self.username_input.fill(user)
        self.password_input.fill(pwd)

    def clickLoginButton(self):
        self.login_button.click()
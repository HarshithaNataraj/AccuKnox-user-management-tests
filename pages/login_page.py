from playwright.sync_api import Page, expect

class LoginPage:
    URL = "https://sinchu-trials719.orangehrmlive.com/auth/seamlessLogin"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("input[name='txtUsername']")
        self.password = page.locator("input[name='txtPassword']")
        self.login_btn = page.locator("button[type='submit']")

    def navigate(self):
        self.page.goto(self.URL)
        self.page.wait_for_selector("input[name='txtUsername']", timeout=5000)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
        
        expect(self.page.get_by_text("HR Administration")).to_be_visible(timeout=30000)
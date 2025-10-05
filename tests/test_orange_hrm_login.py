import sys, os, datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import re
from playwright.sync_api import sync_playwright, expect
from pom.login_page import LoginPage

Screendshot_Dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(Screendshot_Dir, exist_ok=True)

def test_orange_hrm_login():
    
        #browser = p.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=3000)
        headless_mode = os.getenv("HEADLESS", "True").lower() == "true"

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=headless_mode,
                args=["--start-maximized"],
                slow_mo=3000
            )
        
            context = browser.new_context(viewport = {"width": 1920, "height": 1080})
            page = context.new_page()

            login_page = LoginPage(page)
            login_page.navigateToLoginPage()
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            page.screenshot(path=os.path.join(Screendshot_Dir, f"01_login_page_{timestamp}.png"))

            expect(page).to_have_url(re.compile(".*orangehrmlive.com.*"))
            expect(page).to_have_title(re.compile(".*OrangeHRM.*"))
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            page.screenshot(path=os.path.join(Screendshot_Dir, f"02_login_page_validated_{timestamp}.png"))

            login_page.enterValidCredentials()
            page.screenshot(path=os.path.join(Screendshot_Dir, f"03_login_page_credentials_entered_{timestamp}.png"))

            login_page.clickLoginButton()
            page.screenshot(path=os.path.join(Screendshot_Dir, f"04_after_click_login_{timestamp}.png"))


            expect(page.locator("h6:has-text('Dashboard')")).to_be_visible(timeout=3000)
            page.screenshot(path=os.path.join(Screendshot_Dir, f"05_dashboard_page_{timestamp}.png"))

            context.close()
            browser.close()
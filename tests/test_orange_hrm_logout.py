import sys, os, datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import re
from playwright.sync_api import sync_playwright, expect
from pom.login_page import LoginPage
from pom.dashboard_page import DashboardPage

Feature = "Logout"
Screenshot_Dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(Screenshot_Dir, exist_ok=True)

def test_orange_hrm_logout():
    #browser = sync_playwright().start().chromium.launch(headless=False, args=["--start-maximized"],slow_mo=3000)
    headless_mode = os.getenv("HEADLESS", "True").lower() == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless_mode,
            args=["--start-maximized"],
            slow_mo=3000
        )
        context = browser.new_context(viewport = {"width": 1920, "height": 1080})
        page = context.new_page()

        # Navigate to the OrangeHRM login page
        login_page = LoginPage(page)        
        login_page.navigateToLoginPage()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"01_login_page_during_logout_{timestamp}.png"))

        # Perform login
        login_page.enterValidCredentials()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"02_credentials_entered_during_logout_{timestamp}.png"))

        login_page.clickLoginButton()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"03_after_click_login_during_logout_{timestamp}.png"))

        # Verify successful login by checking for the presence of the dashboard
        expect(page.locator("h6:has-text('Dashboard')")).to_be_visible(timeout=3000)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"04_dashboard_page_during_logout_{timestamp}.png"))

        # Perform logout       
        dashboard_page = DashboardPage(page)
        dashboard_page.clickUserProfile()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"05_user_profile_clicked_{timestamp}.png"))

        dashboard_page.clickLogout()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"06_after_clicking_logout_{timestamp}.png"))
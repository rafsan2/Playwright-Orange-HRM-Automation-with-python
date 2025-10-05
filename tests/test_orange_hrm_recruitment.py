import sys, os, datetime
import playwright
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import re
from playwright.sync_api import sync_playwright, expect
from pom.login_page import LoginPage
from pom.dashboard_page import DashboardPage
from pom.recruitment_page import RecruitmentPage  

Feature = "Recruitment Page Test"
Screenshot_Dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
os.makedirs(Screenshot_Dir, exist_ok=True)

def test_orange_hrm_login():
    
        #browser = p.chromium.launch(headless=False, args=["--start-maximized"],slow_mo=1000)
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
        page.screenshot(path=os.path.join(Screenshot_Dir, f"01_login_page_during_recruitement_{timestamp}.png"))

        login_page.enterValidCredentials()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"02_credentials_entered_during_rucruitment_{timestamp}.png"))

        login_page.clickLoginButton()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path = os.path.join(Screenshot_Dir, f"03_after_click_login_during_recruitment_{timestamp}.png"))

        dashboard_page = DashboardPage(page)
        dashboard_page.clickRecruitment()
        expect(page).to_have_url(re.compile(".*https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates*"))
        expect(page).to_have_title(re.compile(".*OrangeHRM.*"))
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"04_recruitment_page_after_clicking_recruitement_{timestamp}.png"))

        recruitment_page = RecruitmentPage(page)
        recruitment_page.clickAdd()
        expect(page).to_have_url(re.compile(".*https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate*"))
        expect(page).to_have_title(re.compile(".*OrangeHRM.*"))
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"05_after_clicking_add{timestamp}.png"))

        recruitment_page.enterCandidateDetails()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"06_after_entering_candidate_details_{timestamp}.png"))

        recruitment_page.clickVacancyDropdown()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"07_after_clicking_vacancy_dropdown_{timestamp}.png"))

        recruitment_page.selectVacancyOption()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"08_after_selecting_vacancy_option_{timestamp}.png"))

        recruitment_page.uploadResumeFile()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"09_after_uploading_resume_{timestamp}.png"))

        recruitment_page.clickContestToKeepData()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"10_after_clicking_continue_{timestamp}.png"))

        recruitment_page.clickSave()
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        page.screenshot(path=os.path.join(Screenshot_Dir, f"11_after_clicking_save_{timestamp}.png"))

        print("✅ Test completed. Browser will remain open.")
        input("Press Enter to close browser...")  # waits for manual input

        browser.close()




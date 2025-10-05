from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page):
        self.page = page
        self.recruitment = page.locator("//li[.='Recruitment']")
        self.userProfile = page.locator("//span[@class='oxd-userdropdown-tab']")
        self.logout = page.locator("//a[.='Logout']")
        
    def clickRecruitment(self):
        self.recruitment.click()

    def clickUserProfile(self):
        self.userProfile.click()

    def clickLogout(self):
        self.logout.click()
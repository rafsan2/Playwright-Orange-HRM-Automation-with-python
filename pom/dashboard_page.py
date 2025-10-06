from playwright.sync_api import Page

class DashboardPage:

    def __init__(self, page):
        self.page = page
        self.dashboardHeader = page.locator("//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        self.recruitment = page.locator("//li[.='Recruitment']")
        self.userProfile = page.locator("//span[@class='oxd-userdropdown-tab']")
        self.logout = page.locator("//a[.='Logout']")
    
    def verifyDashboardPageDisplayed(self):
        return self.dashboardHeader.is_visible()
        
    def clickRecruitment(self):
        self.recruitment.click()

    def clickUserProfile(self):
        self.userProfile.click()

    def clickLogout(self):
        self.logout.click()
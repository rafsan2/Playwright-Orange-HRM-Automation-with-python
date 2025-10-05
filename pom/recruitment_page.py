import json
import os
from playwright.sync_api import Page

class RecruitmentPage:

    def __init__(self, page: Page, data_file="test data/recruitment_page_testData.json"):
        self.page = page
        self.add = page.locator("//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
        self.firstName = page.locator("//input[@name='firstName']")
        self.middleName = page.locator("//input[@name='middleName']")
        self.lastName = page.locator("//input[@name='lastName']")
        self.email = page.locator("//form[@class='oxd-form']/div[3]/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[1]//input[@class='oxd-input oxd-input--active']")
        self.contactNumber = page.locator("//form[@class='oxd-form']//div[2]//div[2]/input[@class='oxd-input oxd-input--active']")
        self.vacancy = page.locator("//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")
        self.selectVacancy = page.locator("//div[@role='listbox']//span[.='Senior QA Lead']")
        self.uploadResume = page.locator("//input[@type='file']")
        self.keywords = page.locator("//div[5]//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-save-candidate-page-full-width']//input[@class='oxd-input oxd-input--active']")   
        self.dateOfApplication = page.locator("//div[@class='oxd-date-input']/input[@class='oxd-input oxd-input--active']")
        self.notes = page.locator("//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical']")
        self.contestToKeepData = page.locator("//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']")
        self.save = page.locator("//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

        with open(data_file, 'r') as file:
            self.test_data = json.load(file)

    def clickAdd(self):
        self.add.click()

    def enterCandidateDetails(self, firstName=None, middleName=None, lastName=None, email=None, contactNumber=None, keywords=None, dateOfApplication=None, notes=None):
        firstName = firstName or self.test_data.get("firstName")
        middleName = middleName or self.test_data.get("middleName")
        lastName = lastName or self.test_data.get("lastName")
        email = email or self.test_data.get("email")
        contactNumber = contactNumber or self.test_data.get("contactNumber")
        keywords = keywords or self.test_data.get("keywords")
        dateOfApplication = dateOfApplication or self.test_data.get("dateOfApplication")
        notes = notes or self.test_data.get("notes")

        self.firstName.fill(firstName)
        self.middleName.fill(middleName)
        self.lastName.fill(lastName)
        self.email.fill(email)
        self.contactNumber.fill(contactNumber)
        self.keywords.fill(keywords)
        self.dateOfApplication.fill(dateOfApplication)
        self.notes.fill(notes)
    
    def clickVacancyDropdown(self):
        self.vacancy.click()
    
    def selectVacancyOption(self):
        self.selectVacancy.click()

    def uploadResumeFile(self):
        file_path = os.path.abspath('test data/Markopolo — Test Report.pdf')
        self.uploadResume.set_input_files(file_path)
    
    def clickContestToKeepData(self):
        self.contestToKeepData.click()

    def clickSave(self):
        self.save.click()

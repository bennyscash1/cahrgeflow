from playwright.sync_api import Page

from WebTest.PageObject.base_pages import BasePages


class LoginPage(BasePages):

    def __init__(self, page):
        self.page = page
        #Login page
        self.m_user_name_input_field = "//input[@id='email']"
        self.m_password_input_field = "//input[@id='password']"
        self.m_submit_button = "//button[normalize-space()='Sign in']"
        self.m_invalid_email_or_pass = "//div[@role='alert']"
        #Dashoboard
        self.m_logout_button = "//button[normalize-space()='Logout']"
        self.m_items_button = "//a[normalize-space()='Items']"
        self.m_item_array_title = "//div[@class='items-list']//div[@class='item-row']"
        self.m_open_items_count = (
            "//div[contains(@class,'dashboard-card')][.//h2[normalize-space()='Open Items']]"
            "//div[contains(@class,'card-count')]"
        )
    def enter_email(self, email):
        self.fill_text(self.m_user_name_input_field, email)
        return self

    def enter_password(self, password):
        self.fill_text(self.m_password_input_field, password)
        return self

    def click_on_submit_button(self):
        self.click(self.m_submit_button)
        self

    def is_home_page_displayed(self, expected_email: str) -> bool:
        assert self.wait_for_element_visibility(self.m_logout_button)
        self.m_home_page_logo_by = "//p[@class='welcome-message']"
        el = self.page.locator(self.m_home_page_logo_by).first
        el.wait_for(state="visible")

        text = el.inner_text().strip()
        return expected_email in text

    def is_error_login_invalid_user_password(self):
        return self.wait_for_element_visibility(self.m_invalid_email_or_pass)
    
    def is_user_or_password_empty(self) -> bool:
        assert self.wait_for_element_visibility(self.m_submit_button)

        email_input = self.page.locator("#email")
        password_input = self.page.locator("#password")

        email_message = email_input.evaluate("el => el.validationMessage")
        password_message = password_input.evaluate("el => el.validationMessage")

        return (
            email_message == "Please fill out this field." or
            password_message == "Please fill out this field."
    )
       #Log out pages
    def click_logout(self):
        return self.click(self.m_logout_button)
    
    def navigate_items_page(self):
        return self.click(self.m_items_button)

    def return_array_of_items(self):
        #Validate page display
        assert self.wait_for_element_visibility(self.m_item_array_title)
        items = self.page.locator(self.m_item_array_title)
        return items.count()

    #Count total open and close itemns
    def get_dashboard_item_count(self, title: str) -> int:
        assert self.wait_for_element_visibility(self.m_open_items_count)
        locator = (
            f"//div[contains(@class,'dashboard-cards')]"
            f"//div[contains(@class,'dashboard-card')][.//h2[normalize-space()='{title}']]"
            f"//div[contains(@class,'card-count')]"
        )

        el = self.page.locator(locator).first
        el.wait_for(state="visible")
        return int(el.inner_text().strip())
                
    
    




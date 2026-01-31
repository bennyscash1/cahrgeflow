from CommonInfra import GetData
from WebTest.Flows.base_flows import BaseFlows
from WebTest.PageObject.login_page import LoginPage


class LoginFlow(BaseFlows):

    def __init__(self, page):
        super().__init__(page)
        self.login_page = LoginPage(page)

    def open_page(self, navigate_to_logon_screen=True, url=None):
        if not navigate_to_logon_screen:
            return self
        final_url = url or GetData.loaded_data[GetData.VarData.WebUrl]
        self.page.goto(final_url)
        return self
    
    #Login flow
    def login_web_flow(self, email, password):
        self.login_page \
            .enter_email(email) \
            .enter_password(password) \
            .click_on_submit_button()
        return self
    
    def is_eamil_display_on_dashboard(self, expected_email):
        return self.login_page.is_home_page_displayed(expected_email)
    
    def is_login_failed(self, incorrect_input=True):
        if (incorrect_input):
             return self.login_page.is_error_login_invalid_user_password()
        else:
            return self.login_page.is_user_or_password_empty()
        
    #Home Page Flow
    def loggedin_user_do_logout(self):
        self.login_page \
            .click_logout()
        return self
    
    def validate_items_numbers(self):
        self.login_page.navigate_items_page()
        item_num =self.login_page.return_array_of_items()
        return item_num

    def get_total_open_and_review_items(self):
        total_open_items = self.login_page.get_dashboard_item_count("Open Items")
        total_review_items = self.login_page.get_dashboard_item_count("Reviewed Items")
        return total_open_items + total_review_items

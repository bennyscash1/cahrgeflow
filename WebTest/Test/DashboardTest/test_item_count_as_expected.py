import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import pytest
import CommonInfra.GetData as GetData
from CommonInfra.GetData import VarData
from WebTest.WebInfra.web_driver_factory import WebDriverFactory
from WebTest.Flows.login_flow import LoginFlow


@pytest.mark.webtest
class TestItemCounter:
    def setup_method(self):
        self.driver = WebDriverFactory()
        self.page = self.driver.get_page()
        self.web_user_name = GetData.loaded_data[VarData.WebUserName]
        self.web_password = GetData.loaded_data[VarData.WebPassword]

    def teardown_method(self):
        self.driver.close_browser()

    def test_item_count_as_expected(self):
        login_flow = LoginFlow(self.page)
        login_flow.open_page()
        login_flow.login_web_flow(self.web_user_name, self.web_password)
        assert login_flow.is_eamil_display_on_dashboard(self.web_user_name)
        
        dashboard_item_count = login_flow.get_total_open_and_review_items()

        item_total_num = login_flow.validate_items_numbers()
        assert item_total_num == dashboard_item_count, f"Item total need to be {dashboard_item_count} \
            but it is {item_total_num}"



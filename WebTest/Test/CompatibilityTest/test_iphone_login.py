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
class TestIphoneLogin:
    def setup_method(self):
        self.driver = WebDriverFactory(
            browser_type="webkit",
            device="iPhone 15 Pro"
            )
        self.page = self.driver.get_page()

        self.url = GetData.loaded_data[VarData.WebUrl]
        self.web_user_name = GetData.loaded_data[VarData.WebUserName]
        self.web_password = GetData.loaded_data[VarData.WebPassword]

    def teardown_method(self):
        self.driver.close_browser()

    def test_login_iphone(self):
        login_flow = LoginFlow(self.page)
        login_flow.open_page(True, url=self.url)
        login_flow.login_web_flow(self.web_user_name, self.web_password)
        assert login_flow.is_eamil_display_on_dashboard(self.web_user_name)

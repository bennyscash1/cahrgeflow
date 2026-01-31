import os
import sys
import pytest
from CommonInfra import GetData
from CommonInfra.GetData import VarData
from CommonInfra.CommonHleperInfra import generate_email
from WebTest.WebInfra.web_driver_factory import WebDriverFactory
from WebTest.Flows.login_flow import LoginFlow

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, "..", "..", ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


@pytest.mark.webtest
class TestInvalidLoginWeb:

    def setup_method(self):
        self.driver = WebDriverFactory()
        self.page = self.driver.get_page()

    def teardown_method(self):
        self.driver.close_browser()
    @pytest.mark.parametrize(
        "email, password, case_name",
        [
            ("", GetData.loaded_data[VarData.WebPassword], "empty email"),
            (GetData.loaded_data[VarData.WebUserName], "", "empty password"),
        ]
    )
    def test_invalid_login_empty_field_tdd(self, email, password, case_name):
        login_flow = LoginFlow(self.page)

        login_flow.open_page()
        login_flow.login_web_flow(email, password)

        assert login_flow.is_login_failed(incorrect_input=False), "User login should failed, but it succeeded"

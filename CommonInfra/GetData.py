import json
import os
from enum import Enum
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class VarData(Enum):
    URL1 = "URL1"
    URL2 = "URL2"
    ApiEmail = "ApiEmail"
    ApiPassword = "ApiPassword"
    BaseApiUrl = "BaseApiUrl"
    WebUrl = "WebUrl"
    WebUserName = "WebUserName"
    WebPassword = "WebPassword"
    ContactName = "ContactName"
    ContactNumber = "ContactNumber"
    AppPackage = "appPackage"
    AppActivity = "appActivity"
    Environment = "Environment"

env = 'dev'
script_directory = os.path.dirname(os.path.abspath(__file__))
file_name = f'jsonData.{env}.json'
# Try several candidate locations (current dir, __pycache__, parent dir)
candidates = [
    os.path.join(script_directory, file_name),
    os.path.join(script_directory, '__pycache__', file_name),
    os.path.join(os.path.dirname(script_directory), file_name),
]
file_path = next((p for p in candidates if os.path.exists(p)), None)
if file_path is None:
    raise FileNotFoundError(
        f"Could not find '{file_name}'. Tried paths: {candidates}")
with open(file_path, 'r') as file:
    data = json.load(file)


loaded_data = {}
loaded_data[VarData.ApiEmail] = data["API"]["Email"]
loaded_data[VarData.ApiPassword] = data["API"]["Password"]
loaded_data[VarData.BaseApiUrl] = data["API"]["BaseApiUrl"]
loaded_data[VarData.WebUrl] = data["WebUi"]["WebUrl"]
loaded_data[VarData.WebUserName] = data["WebUi"]["WebUserName"]
loaded_data[VarData.WebPassword] = data["WebUi"]["WebPassword"]
loaded_data[VarData.ContactName] = data["Mobile"]["ContactName"]
loaded_data[VarData.ContactNumber] = data["Mobile"]["ContactNumber"]
loaded_data[VarData.AppPackage] = data["Mobile"]["appPackage"]
loaded_data[VarData.AppActivity] = data["Mobile"]["appActivity"]
loaded_data[VarData.Environment] = data["Common"]["Enviorment"]

# api init

def get_headers(include_token=False, bearer_token=None):
    headers = {
        'Content-Type': 'application/json'
    }
    if include_token and bearer_token:
        headers['Authorization'] = f'Bearer {bearer_token}'
    return headers
# Now you can use the URL value in your Python code

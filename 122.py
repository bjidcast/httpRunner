import pytest

from test_login_api import Test_Login
from common.yaml_util import clear_yaml


@pytest.fixture(scope='function')
def get_token():
    token = get_token
    return token



#在所有的接口请求之前执行   session级别，自动执行



@pytest.fixture(scope='session',autouse=True)

def red_excel():
    print('前置')
    clear_yaml()
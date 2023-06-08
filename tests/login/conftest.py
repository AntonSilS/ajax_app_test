import pytest
from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)


@pytest.fixture(scope='function')
def user_login_with_back_fixture(user_login_fixture):
    yield user_login_fixture
    user_login_fixture.back()


@pytest.fixture(scope='function')
def user_login_with_out_fixture(user_login_fixture):
    yield user_login_fixture
    user_login_fixture.sign_out()
    



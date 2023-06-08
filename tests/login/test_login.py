import pytest


correct_email = "qa.ajax.app.automation@gmail.com"
correct_password = "qa_automation_password"
incorrect_email = "xxx"
incorrect_password = "wwww"

def test_user_login(user_login_with_out_fixture):
    log_page = user_login_with_out_fixture

    log_page.sign_in(correct_email, correct_password)
    log_page.check_user_name()

    assert correct_email == log_page.find_element_by_id("com.ajaxsystems:id/mail").text
        

@pytest.mark.parametrize("email, password", [
    (correct_email, incorrect_password),
    (incorrect_email, correct_password),
    (incorrect_email, incorrect_password)
])
def test_user_login_wrong(user_login_with_back_fixture, email, password):
    log_page = user_login_with_back_fixture

    log_page.sign_in(email, password)

    assert log_page.find_element_by_text("Wrong login or password").is_displayed()
from .page import Page
from selenium.common.exceptions import TimeoutException

class LoginPage(Page):

    login_button_text = "Log In"
    app_settings_button_text = "App Settings"
    sign_out_button_text = "Sign Out"
    back_button_text = "Back"

    email_field_id = "com.ajaxsystems:id/login"
    pass_field_id = "com.ajaxsystems:id/password"
    log_button_id = "com.ajaxsystems:id/next"
    warn_alert_cancel_id = "com.ajaxsystems:id/cancel_button"
    menu_left_rec_id = "com.ajaxsystems:id/menuDrawer"
    
    def back(self):
        back_button = self.find_element_by_text(self.back_button_text)
        self.click_element(back_button)

    def check_user_name(self):
        try:
            warn_alert_cancel = self.find_element_by_id(self.warn_alert_cancel_id)
            self.click_element(warn_alert_cancel)

        except TimeoutException:
            pass

        finally:
            menu_left = self.find_element_by_resource_id(self.menu_left_rec_id)
            menu_left.click()

            app_settings_button = self.find_element_by_text(self.app_settings_button_text)
            app_settings_button.click()

    def sign_in(self, email, password):
        login_button = self.find_element_by_text(self.login_button_text)
        self.click_element(login_button)

        email_field = self.find_element_by_id(self.email_field_id)
        pass_field = self.find_element_by_id(self.pass_field_id)
        self.fill_field(email_field, email)
        self.fill_field(pass_field, password)

        log_button = self.find_element_by_id(self.log_button_id)
        self.click_element(log_button)

    def sign_out(self):
        sign_out_button = self.find_element_by_text(self.sign_out_button_text)
        sign_out_button.click()
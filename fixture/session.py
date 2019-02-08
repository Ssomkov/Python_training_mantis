class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, user_password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//input[@id='username']").clear()
        wd.find_element_by_xpath("//input[@id='username']").send_keys(user_name)
        wd.find_element_by_xpath("//input[@value='Войти']").click()
        wd.find_element_by_xpath("//input[@id='password']").clear()
        wd.find_element_by_xpath("//input[@id='password']").send_keys(user_password)
        wd.find_element_by_xpath("//input[@value='Войти']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//i[@class='ace-icon fa fa-angle-down']").click()
        wd.find_element_by_xpath("//a[contains(text(), 'Выход')]").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[contains(text(), 'Выход')]")) > 0

    def is_logged_in_as(self, user_name):
        wd = self.app.wd
        return self.get_logged_user() == user_name

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//span[@class='user-info']").text

    def ensure_login(self, user_name, user_password):
        if self.is_logged_in():
            if self.is_logged_in_as(user_name):
                return
            else:
                self.logout()
        self.login(user_name, user_password)

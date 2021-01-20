from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url, login="admin", password="secret"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.login = login
        self.password = password

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
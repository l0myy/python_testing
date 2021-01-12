from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.contact import  ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.navigation = NavigationHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
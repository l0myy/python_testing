from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact(self):
        wd = self.app.wd
        if wd.find_elements_by_name("group"):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact()
        self.filling_contact_forms(contact)
        # choosing group
        if contact.group_name is not None:
            wd.find_element_by_name("new_group").click()
            Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group_name)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.navigation.open_home_page()

    def edit(self, contact):
        wd = self.app.wd
        # click on the edit button
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.filling_contact_forms(contact)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.navigation.open_home_page()

    def delete(self):
        wd = self.app.wd
        # selecting contact to delete
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.navigation.open_home_page()

    def filling_contact_forms(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_filed_box_value("bday", contact.bday)
        self.change_filed_box_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_filed_box_value("aday", contact.aday)
        self.change_filed_box_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_filed_box_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

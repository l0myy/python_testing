from selenium.webdriver.support.ui import Select
from model.contacts import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def open_add_new_contact(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Select all")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact()
        self.filling_contact_forms(contact)
        # choosing group
        if contact.group_name is not None and (contact.group_name in wd.find_elements_by_name("new_group")):
            wd.find_element_by_name("new_group").click()
            Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group_name)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        # click on the edit button
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.filling_contact_forms(contact)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        # click on the edit button
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.filling_contact_forms(contact)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        # selecting contact by index to delete
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.navigation.open_home_page()
        self.contact_cache = None

    def filling_contact_forms(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
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
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                text_in_td = element.find_elements_by_xpath(".//td")
                id = text_in_td[0].find_element_by_name("selected[]").get_attribute("value")
                last_name = text_in_td[1].text
                first_name = text_in_td[2].text
                address = text_in_td[3].text
                emails = text_in_td[4].text
                all_phones = text_in_td[5].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails=emails,
                                                  address=address))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_xpath(".//td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_xpath(".//td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=homephone, work=workphone,
                       mobile=mobilephone, phone2=secondaryphone, email=email, email2=email2, email3=email3,
                       address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        fio = re.search("(.*)\n", text).group(1).split()
        firstname = fio[0]
        lastname = fio[2]
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        address = text.split("\n")[4]
        emails = []
        for element in wd.find_element_by_id("content").find_elements_by_css_selector("a"):
            if re.search("(.*)@(.*).*", element.text) is not None:
                emails.append(element.text)
        return Contact(home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone,
                       email=emails[0], email2=emails[1], email3=emails[2], firstname=firstname, lastname=lastname,
                       address=address)



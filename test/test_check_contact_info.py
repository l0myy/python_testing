from model.contacts import Contact
import random


def test_check_contact_info_on_home_page(app, db):
    index = random.randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones == Contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == Contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_check_contact_info_on_view_page(app):
    index = random.randrange(app.contact.count())
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2
    assert contact_from_view_page.address == contact_from_edit_page.address
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3
    assert contact_from_view_page.address == contact_from_edit_page.address


def test_check_contact_info_with_db(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = db.get_contact_list()
    for index in range(len(contact_from_home_page)):
        assert (contact_from_home_page[index].firstname, contact_from_home_page[index].lastname,
                contact_from_home_page[index].address, contact_from_home_page[index].all_emails,
                contact_from_home_page[index].all_phones) == \
               (contact_from_db[index].firstname.strip(), contact_from_db[index].lastname.strip(), contact_from_db[index].address.strip(),
                Contact.merge_emails_like_on_home_page(contact_from_db[index]),
                Contact.merge_phones_like_on_home_page(contact_from_db[index]))

from model.contacts import Contact
import random


def test_edit_contact_firstname(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="my firstname")
    app.contact.edit_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_full(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname", nickname="l0my")
    app.contact.edit_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)



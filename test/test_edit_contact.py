from model.contacts import Contact


def test_edit_contact_full(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit(Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname",
                             nickname="l0my"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit(Contact(firstname="my firstname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

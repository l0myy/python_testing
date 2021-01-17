from model.contacts import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Anatolii", middlename="Vladimirovich", lastname="Trofimov",
                               nickname="l0my", title="titles", company="bercut", address="saint-petersburg",
                               home="sweet home", mobile="85945739", work="32302", fax="445566",
                               email="wprwrew@mail.ru",
                               email2="epwrojwe@gmail.com", email3="qwpejqwewq@ya.ru", homepage="my home page",
                               bday="15", bmonth="January", byear="1884", aday="18", amonth="October",
                               ayear="1994", group_name="assdfdsf", address2="greg", phone2="rwgw", notes="qwe")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

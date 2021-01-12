from model.contacts import Contact


def test_edit_contact_full(app):
    app.contact.edit(Contact(firstname="new firstname", middlename="new middlename", lastname="new lastname", nickname="l0my",
                             title="titles", company="bercut", address="saint-petersburg", home="sweet home",
                             mobile="85945739", work="32302", fax="445566", email="wprwrew@mail.ru",
                             email2="epwrojwe@gmail.com", email3="qwpejqwewq@ya.ru", homepage="my home page",
                             bday="15", bmonth="January", byear="1884", aday="18", amonth="October", ayear="1994",
                             group_name="assdfdsf", address2="greg", phone2="rwgw", notes="qwe"))


def test_edit_contact_firstname(app):
    app.contact.edit(Contact(firstname="new firstname"))

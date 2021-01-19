from model.contacts import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits*15 + string.punctuation + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.digits + string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen/2))]) + "@" + \
           "".join([random.choice(symbols) for i in range(random.randrange(maxlen/2))]) + ".com"


def random_month():
    symbols = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]
    return random.choice(symbols)


test_data = [Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                     company=company, address=address, home=home, mobile=mobile, work=work, fax=fax, email=email,
                     email2=email2, email3=email3, homepage=homepage, bday=bday, bmonth=bmonth, byear=byear, aday=aday,
                     amonth=amonth, ayear=ayear, group_name=group_name, address2=address2, phone2=phone2, notes=notes)
        for firstname in [random_string("firstname", 10)]
        for middlename in [random_string("middlename", 10)]
        for lastname in [random_string("lastname", 10)]
        for nickname in [random_string("nickname", 10)]
        for title in [random_string("title", 10)]
        for company in [random_string("company", 10)]
        for address in [random_string("address", 10)]
        for home in [random_phone(10)]
        for mobile in [random_phone(10)]
        for work in [random_phone(10)]
        for fax in [random_phone(10)]
        for email in [random_email(10)]
        for email2 in [random_email(10)]
        for email3 in [random_email(10)]
        for homepage in [random_string("homepage", 10)]
        for bday in [str(random.randrange(31))]
        for bmonth in [random_month()]
        for byear in [str(random.randrange(2020))]
        for aday in [str(random.randrange(31))]
        for amonth in [random_month()]
        for ayear in [str(random.randrange(2020))]
        for group_name in [random_string("name", 10)]
        for address2 in [random_string("address2", 10)]
        for phone2 in [random_phone(10)]
        for notes in [random_string("notes", 10)]
        ]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

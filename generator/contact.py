from model.contacts import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters*10 + string.digits + string.punctuation
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


test_data = [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                     lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                     title=random_string("title", 10),company=random_string("company", 10),
                     address=random_string("address", 10), home=random_phone(10),mobile=random_phone(10),
                     work=random_phone(10), fax=random_phone(10), email=random_email(10),email2=random_email(10),
                     email3=random_email(10), homepage=random_string("homepage", 10),bday=str(random.randrange(1, 31)),
                     bmonth=random_month(), byear=str(random.randrange(2020)), aday=str(random.randrange(1, 31)),
                     amonth=random_month(), ayear=str(random.randrange(2020)), group_name=random_string("name", 10),
                     address2=random_string("address2", 10), phone2=random_phone(10), notes=random_string("notes", 10))
             for i in range(5)]+\
            [Contact(firstname="my_name", middlename="my_middle_name", lastname="my last name", nickname="nickname",
                       title="", company="", address="", home="457457", mobile="3567537", work="2457247", fax="245724742",
                       email=random_email(12), email2=random_email(12), email3=random_email(12), homepage="", bday="22",
                       bmonth=random_month(), byear="1363", aday="3", amonth=random_month(), ayear="2000", group_name="",
                       address2="", phone2="31414", notes="")
                      ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
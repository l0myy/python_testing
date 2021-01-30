import pymysql
from model.group import Group
from model.contacts import Contact

class DbFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list ")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, address, home, mobile, work, email, email2, email3,"
                "phone2 from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                contact_list.append(
                    Contact(firstname=firstname, lastname=lastname, address=address,
                            home=home, mobile=mobile, work=work, email=email, email2=email2,
                            email3=email3, phone2=phone2, id=str(id)))
        finally:
            cursor.close()
        return contact_list


from model.contacts import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete()

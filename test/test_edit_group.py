from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="new name", header="new header", footer="new footer"))
    app.session.logout()



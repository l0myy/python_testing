from model.group import Group


def test_edit_group_name(app):
    app.group.edit(Group(name="new name"))


def test_edit_group_header(app):
    app.group.edit(Group(header="new header"))


def test_edit_group_footer(app):
    app.group.edit(Group(footer="new footer"))
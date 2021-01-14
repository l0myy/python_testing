from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="new name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(header="new header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(footer="new footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

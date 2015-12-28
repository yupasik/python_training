# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="New name", id=group.id)
    app.group.edit_group_by_id(new_group, group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)





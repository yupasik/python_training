# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first_group(Group(name="New name"))


def test_edit_first_group_header(app):
    app.group.edit_first_group(Group(header="New header"))


def test_edit_first_group_footer(app):
    app.group.edit_first_group(Group(footer="New footer"))



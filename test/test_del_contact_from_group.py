from model.group import Group
from model.contact import Contact
import random


def test_del_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    contact = random.choice(app.contact.get_contact_list())
    group = random.choice(app.group.get_group_list())
    app.contact.add_contact_to_group(contact, group)
    app.contact.delete_contact_from_group(contact, group)
    assert group.id not in db.get_group_ids_of_contact(contact)
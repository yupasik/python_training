from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test"))
    contact = random.choice(app.contact.get_contact_list())
    group, old_contacts = app.group.find_group_to_add_contact(contact)
    app.contact.add_contact_to_group(contact, group)
    new_contacts = app.group.group_contacts(group)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    assert group.id in db.get_group_ids_of_contact(contact)

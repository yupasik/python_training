# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = Contact(first_name="1111", middle_name="1111", last_name="1111", nickname="1111",
                          avatar="E:\\avatar.jpg", title="1111", company="11", address="111111111",
                          home_phone="1111", mobile_phone="+11111", work_phone="1111", fax="11111",
                          email_1="11111@111.111", email_2="11111@111.111", email_3="11111@111.111",
                          homepage="11", b_day="11", b_month="January", a_day="11", a_month="July", b_year="1911",
                          a_year="2011", address_2="11", phone_2="11", notes="111", id=contact.id)
    app.contact.edit_contact_by_id(new_contact, contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

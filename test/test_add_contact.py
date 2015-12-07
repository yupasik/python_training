# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Yuri", middle_name="none", last_name="Perin", nickname="yupasik",
                      avatar="E:\\avatar.jpg", title="None", company="GS", address="Spb, Turistskay 28k1, 138",
                      home_phone="none", mobile_phone="+79219709149", work_phone="none", fax="none",
                      email_1="yupasik@gmail.com", email_2="none", email_3="none", homepage="none", b_day="18",
                      b_month="8", a_day="14", a_month="3", b_year="1987", a_year="2015", address_2="none",
                      phone_2="none", notes="none")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

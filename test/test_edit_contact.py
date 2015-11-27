# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(first_name="1111", middle_name="1111", last_name="1111", nickname="1111",
                                           avatar="E:\\avatar.jpg", title="1111", company="11", address="111111111",
                                           home_phone="1111", mobile_phone="+11111", work_phone="1111", fax="11111",
                                           email_1="11111@111.111", email_2="11111@111.111", email_3="11111@111.111",
                                           homepage="11", b_day="11", b_month="2", a_day="11", a_month="11", b_year="1911",
                                           a_year="2011", address_2="11", phone_2="11", notes="111"))


def test_edit_first_contact_name(app):
    app.contact.edit_first_contact(Contact(first_name="NEW!", b_day="01", b_month="01", b_year="1999"))


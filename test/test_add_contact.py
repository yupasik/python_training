# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

testdata = [Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
                    last_name=random_string("last_name", 10), nickname=random_string("nickname", 10),
                    avatar=random_string("E:\\", 10), title=random_string("title", 10),
                    company=random_string("company", 10), address=random_string("address", 10),
                    home_phone=random_string("home_phone", 10), mobile_phone=random_string("mobile_phone", 10),
                    work_phone=random_string("work_phone", 10), fax=random_string("fax", 10),
                    email_1=random_string("email_1", 10), email_2=random_string("email_2", 10),
                    email_3=random_string("email_3", 10), homepage=random_string("homepage", 10),
                    b_day=str(random.randrange(1, 32)), b_month=random.choice(months), a_day=str(random.randrange(1, 32)),
                    a_month=random.choice(months), b_year=random_string("b_year", 10), a_year=random_string("a_year", 10),
                    address_2=random_string("address_2", 10), phone_2=random_string("phone_2", 10),
                    notes=random_string("notes", 10))
            for i in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

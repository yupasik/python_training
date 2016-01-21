import re
import random
from model.contact import Contact


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email_1, contact.email_2, contact.email_3])))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone_2]))))


def test_contact_info_on_home_page(app, db):
    contacts_from_ui = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list_from_home_page()
    assert sorted(contacts_from_ui, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)


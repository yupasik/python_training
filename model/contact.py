# -*- coding: utf-8 -*-
from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, avatar=None, title=None,
                 company=None, address=None, home_phone=None, mobile_phone=None, work_phone=None, fax=None,
                 email_1=None, email_2=None, email_3=None, homepage=None, b_day=None, b_month=None, a_day=None,
                 a_month=None, b_year=None, a_year=None, address_2=None, phone_2=None, notes=None, id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.avatar = avatar
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.a_day = a_day
        self.a_month = a_month
        self.b_year = b_year
        self.a_year = a_year
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name and \
                self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

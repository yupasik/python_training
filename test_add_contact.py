# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="Yuri", middle_name="none", last_name="Perin", nickname="yupasik",
                   title="None", company="GS", address="Spb, Turistskay 28k1, 138", home_phone="none",
                   mobile_phone="+79219709149", work_phone="none", fax="none", email_1="yupasik@gmail.com",
                   email_2="none", email_3="none", homepage="none", b_day="18", b_month="8", a_day="14", a_month="3",
                   b_year="1987", a_year="2015", address_2="none", phone_2="none", notes="none"))
    app.logout()


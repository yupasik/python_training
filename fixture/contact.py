from model.contact import Contact
import re


class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_avatar(self, avatar):
        wd = self.app.wd
        if avatar is not None:
            wd.find_element_by_name("photo").send_keys(avatar)

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        self.change_field_value("firstname", Contact.first_name)
        self.change_field_value("middlename", Contact.middle_name)
        self.change_field_value("lastname", Contact.last_name)
        self.change_field_value("nickname", Contact.nickname)
        self.change_field_value("title", Contact.title)
        self.change_avatar(Contact.avatar)
        self.change_field_value("company", Contact.company)
        self.change_field_value("address", Contact.address)
        self.change_field_value("home", Contact.home_phone)
        self.change_field_value("mobile", Contact.mobile_phone)
        self.change_field_value("work", Contact.work_phone)
        self.change_field_value("fax", Contact.fax)
        self.change_field_value("email", Contact.email_1)
        self.change_field_value("email2", Contact.email_2)
        self.change_field_value("email3", Contact.email_3)
        self.change_field_value("homepage", Contact.homepage)
        self.change_field_value("address2", Contact.address_2)
        self.change_field_value("phone2", Contact.phone_2)
        self.change_field_value("notes", Contact.notes)
        if Contact.b_day is not None:
            wd.find_element_by_name("bday").send_keys(Contact.b_day)
        if Contact.b_month is not None:
            wd.find_element_by_name("bmonth").send_keys(Contact.b_month)
        if Contact.b_year is not None:
            wd.find_element_by_name("byear").send_keys(Contact.b_year)
        if Contact.a_day is not None:
            wd.find_element_by_name("aday").send_keys(Contact.a_day)
        if Contact.a_month is not None:
            wd.find_element_by_name("amonth").send_keys(Contact.a_month)
        if Contact.a_year is not None:
            wd.find_element_by_name("ayear").send_keys(Contact.a_year)

    def new_contact_form(self, Contact):
        wd = self.app.wd
        self.fill_contact_form(Contact)
        self.contact_cache = None

    def edit_contact_form(self, Contact):
        wd = self.app.wd
        self.fill_contact_form(Contact)
        self.contact_cache = None

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.new_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def add_contact_to_group(self, Contact, Group):
        wd = self.app.wd
        self.app.open_home_page(wd)
        self.select_contact_by_id(Contact.id)
        wd.find_element_by_name("to_group").send_keys(Group.name)
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, Contact, Group):
        wd = self.app.wd
        self.app.open_home_page(wd)
        wd.find_element_by_name("group").send_keys(Group.name)
        wd.find_element_by_css_selector("body").click()
        self.select_contact_by_id(Contact.id)
        wd.find_element_by_name("remove").click()
        self.return_to_home_page()
        wd.find_element_by_name("group").send_keys("[all]")
        wd.find_element_by_css_selector("body").click()

    def edit_first_contact(self, Contact):
        self.edit_contact_by_index(Contact, 0)

    def edit_contact_by_index(self, Contact, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.edit_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, Contact, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.edit_contact_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page(wd)
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                address = cells[3].text
                first_name = cells[2].text
                last_name = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, id=id, address=address,
                                                  all_phones_from_homepage=all_phones,
                                                  all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page(wd)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page(wd)
        wd.find_element_by_xpath("//input[@value='%s']/../../td[8]/a" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page(wd)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page(wd)
        wd.find_element_by_xpath("//input[@value='%s']/../../td[7]/a" % id).click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, id=id, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, phone_2=phone_2, address=address,
                       email_1=email_1, email_2=email_2, email_3=email_3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        try:
            home_phone = re.search("H: (.*)", text).group(1)
        except AttributeError:
            home_phone = ""
        try:
            mobile_phone = re.search("M: (.*)", text).group(1)
        except AttributeError:
            mobile_phone = ""
        try:
            work_phone = re.search("W: (.*)", text).group(1)
        except AttributeError:
            work_phone = ""
        try:
            phone_2 = re.search("P: (.*)", text).group(1)
        except AttributeError:
            phone_2 = ""
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone_2=phone_2)

    def clean(self, contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip(), last_name=contact.last_name.strip(),
                       address=contact.address.strip(), mobile_phone=contact.mobile_phone,
                       work_phone=contact.work_phone, phone_2=contact.phone_2,
                       email_1=contact.email_1, email_2=contact.email_2,
                       email_3=contact.email_3)

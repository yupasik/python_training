

class ContactHelper:

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

    def fill_group_form(self, Contact):
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

    def new_group_form(self, Contact):
        wd = self.app.wd
        self.fill_group_form(Contact)
        self.change_birthday_value(Contact.b_day, Contact.b_month, Contact.b_year)
        self.change_anniversary_value(Contact.a_day, Contact.a_month, Contact.a_year)

    def edit_group_form(self, Contact):
        wd = self.app.wd
        if Contact.b_month is not None:
            Contact.b_month = str(int(Contact.b_month) + 1)
        if Contact.a_month is not None:
            Contact.a_month = str(int(Contact.a_month) + 1)
        self.fill_group_form(Contact)
        self.change_birthday_value(Contact.b_day, Contact.b_month, Contact.b_year)
        self.change_anniversary_value(Contact.a_day, Contact.a_month, Contact.a_year)

    def change_birthday_value(self, day, month, year):
        wd = self.app.wd
        if day is not None:
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % (int(day) + 2)).click()
        if month is not None:
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % (int(month) + 1)).click()
        if year is not None:
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(year)

    def change_anniversary_value(self, day, month, year):
        wd = self.app.wd
        if day is not None:
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % (int(day) + 2)).click()
        if month is not None:
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % (int(month) + 1)).click()
        if year is not None:
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(year)

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.new_group_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_first_contact(self, Contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.edit_group_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

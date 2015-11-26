

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_group_form(self, Contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Contact.nickname)
        wd.find_element_by_name("photo").send_keys(Contact.avatar)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(Contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(Contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(Contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % (int(Contact.b_day) + 2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % (int(Contact.b_day) + 2)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % (int(Contact.b_month) + 1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % (int(Contact.b_month) + 1)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Contact.b_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % (int(Contact.a_day) + 2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % (int(Contact.a_day) + 2)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % (int(Contact.a_month) + 1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % (int(Contact.a_month) + 1)).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Contact.a_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Contact.phone_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Contact.notes)

    def create(self, Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_group_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit_first_contact(self, Contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_group_form(Contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
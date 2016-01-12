from model.group import Group
from model.contact import Contact
from random import randrange
import random


class GroupHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        #  submit deletion
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        #  submit deletion
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(new_group_data, 0)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def find_group_to_add_contact(self, Contact):
        wd = self.app.wd
        self.return_to_home_page()
        groups = self.get_group_list()
        self.return_to_home_page()
        while 1:
            group = random.choice(groups)
            wd.find_element_by_name("group").send_keys(group.name)
            wd.find_element_by_css_selector("body").click()
            contacts = self.get_contact_list_in_group()
            if Contact not in contacts:
                wd.find_element_by_name("group").send_keys("[all]")
                wd.find_element_by_css_selector("body").click()
                return group, contacts

    def group_contacts(self, Group):
        wd = self.app.wd
        self.return_to_home_page()
        wd.find_element_by_name("group").send_keys(Group.name)
        wd.find_element_by_css_selector("body").click()
        contacts = self.get_contact_list_in_group()
        wd.find_element_by_name("group").send_keys("[all]")
        wd.find_element_by_css_selector("body").click()
        return contacts

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

    def get_contact_list_in_group(self):
        wd = self.app.wd
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

    def edit_group_by_index(self, new_group_data, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        #  open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        #  submit editing
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, new_group_data, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        #  open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        #  submit editing
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

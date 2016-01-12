import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True  # Turn off cashing db

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, mobile, work, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, address=address,
                                            mobile_phone=mobile, work_phone=work, phone_2=phone2,
                                            email_1=email, email_2=email2, email_3=email3))
        finally:
            cursor.close()
        return contact_list

    def get_contact_list_from_home_page(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id), first_name=firstname.strip(), last_name=lastname.strip(), address=address.strip(),
                                            all_phones_from_homepage="%s\n%s\n%s\n%s" % (home.strip(), mobile.strip(), work.strip(), phone2.strip()),
                                            all_emails_from_homepage="%s\n%s\n%s" % (email.strip(), email2.strip(), email3.strip())))
        finally:
            cursor.close()
        return contact_list

    def get_group_ids_of_contact(self, Contact):
        group_id_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                if Contact.id == str(id):
                    group_id_list.append(str(group_id))
        finally:
            cursor.close()
        return group_id_list

    def get_not_empty_groups_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (group_id) = row
                group_list.append(str(group_id))
        finally:
            cursor.close()
        return list(set(group_list))

    def destroy(self):
        self.connection.close()



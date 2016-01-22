Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname> , <nickname> , <title> , <company> , <address> , <home> , <mobile> , <work> , <fax> , <email> , <email2> , <email3> , <homepage> , <address2> , <phone2> , <notes> , <bday> , <bmonth> , <byear> , <aday> , <amonth>  and <ayear>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added new contact

  Examples:
  | firstname   | middlename   | lastname   | nickname   | title   | company   |  address   | home   | mobile    |  work     | fax     | email         | email2         | email3        | homepage    |address2 |  phone2    | notes   |bday| bmonth   |  byear |aday| amonth   | ayear |
  | firstname1  | middlename1  | lastname1  | nickname1  | title1  | company1  |  address1  | home1  | 11111111  |  1111111  | 111111  | 11111111@111  | 1111111@11111  | 111111@11111  | 11111.1111  | 111111  |  11111111  | 111111  | 1  | January  |  1991  | 1  | January  | 2001  |
  | firstname2  | middlename2  | lastname2  | nickname2  | title2  | company2  |  address2  | home2  | 22222222  |  2222222  | 222222  | 22222222@222  | 2222222@22222  | 222222@22222  | 22222.2222  | 222222  |  22222222  | 222222  | 2  | January  |  1992  | 2  | January  | 2002  |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <middlename>, <lastname> , <nickname> , <title> , <company> , <address> , <home> , <mobile> , <work> , <fax> , <email> , <email2> , <email3> , <homepage> , <address2> , <phone2> , <notes> , <bday> , <bmonth> , <byear> , <aday> , <amonth>  and <ayear>
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list with the modified contact

  Examples:
  | firstname   | middlename   | lastname   | nickname   | title   | company   |  address   | home   | mobile    |  work     | fax     | email         | email2         | email3        | homepage    | address2|  phone2    | notes   |bday| bmonth   |  byear |aday| amonth   | ayear |
  | firstname1  | middlename1  | lastname1  | nickname1  | title1  | company1  |  address1  | home1  | 11111111  |  1111111  | 111111  | 11111111@111  | 1111111@11111  | 111111@11111  | 11111.1111  | 111111  |  11111111  | 111111  | 1  | January  |  1991  | 1  | January  | 2001  |

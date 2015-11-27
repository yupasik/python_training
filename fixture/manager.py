from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class InitHelpers:

    def __init__(self, app):
        self.app = app
        self.app.session = SessionHelper(app)
        self.session = SessionHelper(app)
        self.app.contact = ContactHelper(app)
        self.contact = ContactHelper(app)
        self.app.group = GroupHelper(app)
        self.group = GroupHelper(app)



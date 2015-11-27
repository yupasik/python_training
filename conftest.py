import pytest
from fixture.application import Application
from fixture.manager import InitHelpers

fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.manager.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.manager.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

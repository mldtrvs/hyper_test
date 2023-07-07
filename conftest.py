import pytest

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    fixture.session.login_HGfilm(username="mentalfvnda@gmail.com", password="retSoHn18")
    return fixture

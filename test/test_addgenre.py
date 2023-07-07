import pytest
import time

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addgenre(app):
    app.session.login_HGfilm(username="mentalfvnda@gmail.com", password="retSoHn18")
    wait = app.genres.go_to_genres()
    app.genres.add_new(wait, "pyuic5456dsc")
    time.sleep(2)
    app.genres.search_for_new_added("pyuic5456dsc")
    app.genres.check_if_added_delete_check_if_deleted()

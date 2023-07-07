import pytest
import time

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_addfilmtype(app):
    app.session.login_HGfilm(username="mentalfvnda@gmail.com", password="retSoHn18")
    wait = app.filmType.go_to_film_types_menu()
    app.filmType.add_new(wait, "eji4t3a4r3")
    time.sleep(3)
    app.filmType.search_for_new_added("eji4t3a4r3")
    app.filmType.check_if_added_delete_check_if_deleted()

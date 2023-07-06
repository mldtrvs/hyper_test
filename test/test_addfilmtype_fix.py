import pytest
import time

from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_addfilmtype(app):

    app.session.login_HGfilm(username="mentalfvnda@gmail.com", password="retSoHn18")
    #time.sleep(2)
    wait = app.go_to_film_types_menu()
    app.add_new_film_type(wait, film_type="eji4t3a4r3")
    time.sleep(2)
    app.search_for_new_film_type()
    app.check_if_added_delete_check_if_deleted()




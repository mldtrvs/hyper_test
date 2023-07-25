import time


def test_addFilmType(app):
    app.menuCategories.go_to_directories()
    wait = app.filmType.go_to_film_types_menu()
    app.filmType.add_new(wait)
    time.sleep(4)
    app.filmType.search_for_new_added("eji4t3a4r3")
    app.filmType.check_if_added_delete_check_if_deleted(wait)


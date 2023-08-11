import time


def test_addFilmType(app):
    app.menuCategories.go_to_directories()
    wait = app.filmType.go_to_film_types_menu()

    app.filmType.add_new(wait, "eji4t3a4r3")
    time.sleep(2)
    app.filmType.search_for_new_added("eji4t3a4r3")
    app.filmType.check_if_added()

    app.filmType.edit(wait, "mmjag341rds")
    time.sleep(2)
    app.filmType.search_for_new_added("mmjag341rds")
    app.filmType.check_if_added()

    app.filmType.delete_record(wait)
    app.filmType.check_if_deleted()


import time


def test_addGenre(app):
    app.menuCategories.go_to_directories()
    wait = app.genres.go_to_genres()
    app.genres.add_new(wait, "pyuic5456dsc")
    time.sleep(2)
    app.genres.search_for_new_added("pyuic5456dsc")
    app.genres.check_if_added_delete_check_if_deleted(wait)

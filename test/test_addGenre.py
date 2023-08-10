import time


def test_addGenre(app):
    app.menuCategories.go_to_directories()
    wait = app.genres.go_to_genres()

    app.genres.add_new(wait, "pyuic5456dsc", "tyutbg12fed")
    time.sleep(2)
    app.genres.search_for_new_added("pyuic5456dsc")
    app.genres.check_if_added()
    app.genres.search_for_new_added("tyutbg12fed")
    app.genres.check_if_added()

    app.genres.edit(wait, "yrhgd34das", "qwexcsxc213")
    time.sleep(2)
    app.genres.search_for_new_added("yrhgd34das")
    app.genres.check_if_added()
    app.genres.search_for_new_added("qwexcsxc213")
    app.genres.check_if_added()

    app.genres.delete_record(wait)
    app.genres.check_if_deleted()

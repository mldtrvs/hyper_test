import time


def test_addPersonalitiesType(app):
    app.menuCategories.go_to_directories()
    wait = app.personalitiesType.go_to_person_type()
    app.personalitiesType.add_new(wait, "uywte3243ijo", "gfhg657sad")
    time.sleep(2)
    app.personalitiesType.search_for_new_added("uywte3243ijo")
    app.personalitiesType.check_if_added()
    app.personalitiesType.search_for_new_added("gfhg657sad")
    app.personalitiesType.delete_record(wait)
    app.personalitiesType.check_if_deleted()
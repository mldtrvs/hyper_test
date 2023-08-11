import time


def test_addPersonalitiesType(app):
    app.menuCategories.go_to_directories()
    wait = app.personalitiesType.go_to_person_type()

    app.personalitiesType.add_new(wait, "uywte3243ijo", "gfhg657sad")
    time.sleep(2)
    app.personalitiesType.search_for_new_added_ru("uywte3243ijo")
    app.personalitiesType.check_if_added()
    app.personalitiesType.search_for_new_added_en("gfhg657sad")
    app.personalitiesType.check_if_added()

    app.personalitiesType.edit(wait, "dasf324fsf", "kiufuj12d")
    time.sleep(2)
    app.personalitiesType.search_for_new_added_ru("dasf324fsf")
    app.personalitiesType.check_if_added()
    app.personalitiesType.search_for_new_added_en("kiufuj12d")
    app.personalitiesType.check_if_added()

    app.personalitiesType.delete_record(wait)
    app.personalitiesType.check_if_deleted()
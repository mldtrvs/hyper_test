import time


def test_addTerritory(app):
    app.menuCategories.go_to_directories()
    wait = app.territories.go_to_territories()
    app.territories.add_new_rest(wait, "refthd23fr", "18", "131")
    time.sleep(3)
    app.territories.search_for_new_added("refthd23fr")


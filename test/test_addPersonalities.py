import time


def test_addPersonalities(app):
    app.menuCategories.go_to_directories()
    wait = app.personalities.go_to_personalities()
    app.personalities.add_new(wait, "aasd870asxsa0")
    time.sleep(2)
    app.personalities.search_for_new_added_ru("aasd870asxsa0")
    app.personalities.check_if_added()
    app.personalities.delete_record(wait)
    app.personalities.check_if_deleted()
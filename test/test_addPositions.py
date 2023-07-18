import time


def test_addPosition(app):
    app.menuCategories.go_to_directories()
    wait = app.positions.go_to_positions()
    app.positions.add_new(wait, "hijnoii257")
    time.sleep(2)
    app.positions.search_for_new_added("hijnoii257")
    app.positions.check_if_added_delete_check_if_deleted(wait)
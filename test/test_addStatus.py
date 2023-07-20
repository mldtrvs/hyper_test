import time


def test_addstatus(app):
    app.menuCategories.go_to_directories()
    wait = app.statuses.go_to_statuses()
    for div_index in range(1, 16):
        aria_owns_value = app.statuses.open_new_form("qwe4345sda", wait)
        app.statuses.choose_status_type(aria_owns_value, div_index)
        app.statuses.save_form(wait)
        app.statuses.search_for_new_added("qwe4345sda")
        app.statuses.check_if_added_delete_check_if_deleted(wait)
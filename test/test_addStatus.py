import time

def test_addstatus(app):
    app.menuCategories.go_to_directories()
    wait = app.statuses.go_to_statuses()
    for div_index in range(1, 2):
        aria_owns_value = app.statuses.open_new_form("qwe4345sda", wait)
        status_type_text_in = app.statuses.choose_status_type(aria_owns_value, div_index)
        time.sleep(2)
        app.statuses.save_form(wait)
        time.sleep(2)
        app.statuses.search_for_new_added("qwe4345sda")
        time.sleep(2)
        status_type_text_out = app.statuses.get_status_type_value()
        app.statuses.check_selected_status_type_match(status_type_text_in, status_type_text_out)
        app.statuses.check_if_added()
        app.statuses.delete_record(wait)
        app.statuses.check_if_deleted()
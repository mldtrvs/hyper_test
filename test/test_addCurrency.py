import time


def test_addCurrency(app):
    app.menuCategories.go_to_directories()
    wait = app.currency.go_to_currency()
    app.currency.add_new(wait, "refthd23fr", "18", "XYZ", "131", "☮︎")
    time.sleep(3)
    app.currency.search_for_new_added("refthd23fr")
    tr_attributes = app.currency.get_tr_values()
    app.currency.check_tr_values_match("refthd23fr", "18", "XYZ", "131", "☮︎", tr_attributes)
    app.currency.check_if_added()
    app.currency.delete_record(wait)
    app.currency.check_if_deleted()
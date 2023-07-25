
def test_addtag(app):
    app.menuCategories.go_to_directories()
    wait = app.tags.go_to_tags()
    for div_index in range(1, 7):
        aria_owns_value = app.tags.open_new_form("zaa1231kjklm", wait)
        app.tags.choose_status_type(aria_owns_value, div_index)
        app.tags.save_form(wait)
        app.tags.search_for_new_added("zaa1231kjklm")
        app.tags.check_if_added_delete_check_if_deleted(wait)

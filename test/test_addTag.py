import time
def test_addtag(app):
    app.menuCategories.go_to_directories()
    wait = app.tags.go_to_tags()
    for div_index in range(1, 2):
        aria_owns_value = app.tags.open_new_form("zaa1231kjklm", wait)
        tag_type_text_in = app.tags.choose_tag_type(aria_owns_value, div_index)
        time.sleep(2)
        app.tags.save_form(wait)
        time.sleep(2)
        app.tags.search_for_new_added("zaa1231kjklm")
        time.sleep(2)
        tag_type_text_out = app.tags.get_tag_type_value()
        app.tags.check_selected_tag_type_match(tag_type_text_in, tag_type_text_out)
        app.tags.check_if_added()
        app.tags.delete_record(wait)
        app.tags.check_if_deleted()

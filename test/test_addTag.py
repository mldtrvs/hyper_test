import time


def test_addtag(app):
    app.menuCategories.go_to_directories()
    wait = app.tags.go_to_tags()
    for div_index in range(1, 3):
        aria_owns_value = app.tags.open_new_form("ethet34fev", wait)
        tag_type_text_in = app.tags.choose_tag_type(aria_owns_value, div_index)
        app.tags.save_form(wait)

        app.tags.search_for_new_added(wait, "ethet34fev")
        time.sleep(4)
        app.tags.check_if_added()
        tag_type_text_out = app.tags.get_tag_type_value()
        app.tags.check_selected_tag_type_match(tag_type_text_in, tag_type_text_out)

        app.tags.edit(wait, "mnmndh34fgd")
        app.tags.search_for_new_added(wait, "mnmndh34fgd")
        time.sleep(4)
        app.tags.check_if_added()

        app.tags.delete_record(wait)
        app.tags.check_if_deleted()

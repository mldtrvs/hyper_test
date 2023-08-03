import time

def test_licence_type(app):
    app.menuCategories.go_to_directories()
    wait = app.licenceType.go_to_licence_type()
    for div_index in range(1, 3):
        aria_owns_value = app.licenceType.open_new_form("poyujv2323dc", wait, 'weqwfdv')
        licence_type_text_in = app.licenceType.choose_licence_type(aria_owns_value, div_index)
        app.licenceType.save_form(wait)
        app.licenceType.search_for_new_added("poyujv2323dc")
        time.sleep(4)
        licence_type_text_out = app.licenceType.get_licence_type_value()
        app.licenceType.check_selected_licence_type_match(licence_type_text_in, licence_type_text_out)
        app.licenceType.check_if_added()
        app.licenceType.delete_record(wait)
        app.licenceType.check_if_deleted()
import time
def test_docDetails(app):
    app.menuCategories.go_to_directories()
    wait = app.docDetails.go_to_doc_details()
    for div_index in range(1, 4):
        aria_owns_value = app.docDetails.open_new_form("ethet34fev", wait)
        affiliation_text_in = app.docDetails.choose_affiliation(aria_owns_value, div_index)
        app.docDetails.save_form(wait)
        app.docDetails.search_for_new_added("ethet34fev")
        time.sleep(4)
        affiliation_text_out = app.docDetails.get_affiliation_value()
        app.docDetails.check_selected_affiliation_match(affiliation_text_in, affiliation_text_out)
        app.docDetails.check_if_added()

        app.docDetails.edit(wait, "dfgwr4353df")
        app.docDetails.search_for_new_added("dfgwr4353df")
        time.sleep(4)
        app.docDetails.check_if_added()

        app.docDetails.delete_record(wait)
        app.docDetails.check_if_deleted()
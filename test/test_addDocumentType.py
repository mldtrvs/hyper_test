import time


def test_addDocumentType(app):
    app.menuCategories.go_to_directories()
    wait = app.documentType.go_to_document_types()
    app.documentType.add_new(wait)
    time.sleep(2)
    app.documentType.search_for_new_added("yljw72lkdjek")
    app.documentType.check_if_added_delete_check_if_deleted(wait)
import time


def test_addDocumentType(app):
    app.menuCategories.go_to_directories()
    wait = app.documentType.go_to_document_types()
    app.documentType.add_new(wait, "yljw72lkdjek")
    time.sleep(2)
    app.documentType.search_for_new_added("yljw72lkdjek")
    app.documentType.check_if_added()

    app.documentType.edit(wait, "cdccaswszx12")
    time.sleep(2)
    app.documentType.search_for_new_added("cdccaswszx12")
    app.documentType.check_if_added()

    app.documentType.delete_record(wait)
    app.documentType.check_if_deleted()

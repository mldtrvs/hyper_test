import time


def test_addLegalForm(app):
    app.menuCategories.go_to_directories()
    wait = app.legalForms.go_to_legal_forms()
    app.legalForms.add_new(wait, "saDgr785gxc")
    time.sleep(2)
    app.legalForms.search_for_new_added("saDgr785gxc")
    app.legalForms.check_if_added_delete_check_if_deleted(wait)
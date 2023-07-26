import time


def test_addLegalForm(app):
    app.menuCategories.go_to_directories()
    app.legalForms.go_to_legal_forms()
    app.legalForms.add_new("saDgr785gxc")
    time.sleep(2)
    app.legalForms.search_for_new_added("saDgr785gxc")
    app.legalForms.check_if_added_delete_check_if_deleted()

def test_addLegalForm_with_SP_checkbox(app):
    app.menuCategories.go_to_directories()
    app.legalForms.go_to_legal_forms()
    app.legalForms.add_new_SP_attribute_checkbox("Dgr785gxc")
    time.sleep(2)
    app.legalForms.search_for_new_added("Dgr785gxc")
    app.legalForms.check_if_added_delete_check_if_deleted()
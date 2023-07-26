import time


def test_addAddressType(app):
    app.menuCategories.go_to_directories()
    wait = app.ageRestrictions.go_to_age_restrictions()
    app.ageRestrictions.add_new(wait, "wfrr+",)
    time.sleep(2)
    app.ageRestrictions.search_for_new_added("wfrr+")
    app.ageRestrictions.check_if_added()
    app.ageRestrictions.delete_record(wait)
    app.ageRestrictions.check_if_deleted()
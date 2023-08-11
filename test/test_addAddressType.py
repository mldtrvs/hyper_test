import time


def test_addAddressType(app):
    app.menuCategories.go_to_directories()
    wait = app.addressType.go_to_address_types()

    app.addressType.add_new(wait, "kamxc123masd")
    time.sleep(2)
    app.addressType.search_for_new_added("kamxc123masd")
    app.addressType.check_if_added()

    app.addressType.edit(wait, "sdfe213dsfd")
    time.sleep(2)
    app.addressType.search_for_new_added("sdfe213dsfd")
    app.addressType.check_if_added()

    app.addressType.delete_record(wait)
    app.addressType.check_if_deleted()
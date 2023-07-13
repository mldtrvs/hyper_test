import time


def test_addAddressType(app):
    wait = app.addressType.go_to_address_types()
    app.addressType.add_new(wait, "kamxc123masd")
    time.sleep(2)
    app.addressType.search_for_new_added("kamxc123masd")
    app.addressType.check_if_added_delete_check_if_deleted(wait)
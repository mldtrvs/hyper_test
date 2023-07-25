import time


def test_addPosition(app):
    app.menuCategories.go_to_directories()
    app.releaseType.go_to_release_type()
    app.releaseType.add_new("ccweeql79asds")
    time.sleep(2)
    app.releaseType.search_for_new_added("ccweeql79asds")
    app.releaseType.check_if_added_delete_check_if_deleted()
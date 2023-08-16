import time


def test_releaseType(app):
    app.menuCategories.go_to_directories()
    app.releaseType.go_to_release_type()

    wait = app.releaseType.add_new("ccweeql79asds")
    time.sleep(2)
    app.releaseType.search_for_new_added("ccweeql79asds")
    app.releaseType.check_if_added()

    app.releaseType.edit(wait, "bvxvs231cv")
    app.releaseType.search_for_new_added("bvxvs231cv")
    time.sleep(4)
    app.releaseType.check_if_added()

    app.releaseType.delete_record(wait)
    app.releaseType.check_if_deleted()
import time


def test_addVideoFormat(app):
    app.menuCategories.go_to_directories()
    wait = app.videoFormat.go_to_video_format()

    app.videoFormat.add_new(wait, "rtree332weq")
    time.sleep(2)
    app.videoFormat.search_for_new_added("rtree332weq")
    app.videoFormat.check_if_added()

    app.videoFormat.edit(wait, 'lllsadwqd21sd')
    time.sleep(2)
    app.videoFormat.search_for_new_added("lllsadwqd21sd")
    app.videoFormat.check_if_added()

    app.videoFormat.delete_record(wait)
    app.videoFormat.check_if_deleted()

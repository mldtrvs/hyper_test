import time


def test_addPersonalities(app):
    app.menuCategories.go_to_directories()
    wait = app.personalities.go_to_personalities()
    app.personalities.add_new(wait, "aasd870asxsa0", "vgbg55tfvssv")
    time.sleep(3)
    app.personalities.search_for_new_added_ru("aasd870asxsa0")
    app.personalities.check_if_added()
    app.personalities.search_for_new_added_en("vgbg55tfvssv")
    app.personalities.check_if_added()

    app.personalities.edit(wait, 'bbnrrf121vfv', 'asasdqre645fg')
    app.personalities.search_for_new_added_ru('bbnrrf121vfv')
    app.personalities.check_if_added()
    app.personalities.search_for_new_added_en('asasdqre645fg')
    app.personalities.check_if_added()

    app.personalities.delete_record(wait)
    app.personalities.check_if_deleted()

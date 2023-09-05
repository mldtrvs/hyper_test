import time

def test_addproject(app):
    app.menuCategories.go_to_general()
    wait = app.projects.go_to_projects()
    #app.projects.open_new_form(wait, )
    for div_index in range(1, 2):
        aria_owns_value = app.projects.open_new_form(wait, "prognrts213gd")
        production_type_text_in = app.projects.choose_production_type(aria_owns_value, div_index)
        app.projects.choose_genre_type()
        app.projects.save_form(wait)
        app.projects.search_for_new_added(wait, "prognrts213gd")
        time.sleep(4)
        app.projects.check_if_added()

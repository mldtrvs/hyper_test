import time


def test_project_genre(app):
    app.menuCategories.go_to_general()
    wait = app.projects.go_to_projects()

    aria_owns_value = app.projects.open_new_form(wait, "prognrts213gd")
    # app.projects.production_type_own_production(aria_owns_value, wait)
    production_type_text_in = app.projects.random_choice_production_type(aria_owns_value, wait)
    # div_index_gt = 0  # Define the index you want to exclude
    gt_aria_owns_value, checkboxes = app.projects.random_choice_genre_type(wait)
    app.projects.save_form(wait)
    app.projects.search_for_new_added(wait, "prognrts213gd")
    time.sleep(4)
    app.projects.check_if_added()

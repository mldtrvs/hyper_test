import time


def test_project_genre(app):
    app.menuCategories.go_to_general()
    wait = app.projects.go_to_projects()

    aria_owns_value = app.projects.open_new_form(wait, "pewqew123asd")
    # app.projects.production_type_own_production(aria_owns_value, wait)
    production_type_text_in = app.projects.random_choice_production_type(aria_owns_value)
    random_genre_types = app.projects.random_choice_genre_type(wait)
    app.projects.save_form(wait)

    app.projects.search_for_new_added(wait, "pewqew123asd")
    time.sleep(4)
    production_type_text_out = app.projects.get_production_type_td_value()
    app.projects.check_selected_production_type_match(production_type_text_in, production_type_text_out)
    project_tr_text_out = app.projects.get_genre_value(wait)
    app.projects.check_selected_genres_match(random_genre_types, project_tr_text_out)
    app.projects.check_if_added()

    app.projects.delete_record(wait)
    app.projects.check_if_deleted()

from random import randrange

from model.project import Project


def test_delete_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name="Project_to_del"))
    old_projects = app.project.get_project_list()
    index = randrange(len(old_projects))
    app.project.delete_project_by_index(index)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)

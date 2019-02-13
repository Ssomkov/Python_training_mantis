import random

from model.project import Project


def test_delete_project(app):
    if len(app.soap.get_project_list()) == 0:
        app.project.add_project(Project(name="Project_to_del"))
    old_projects = app.soap.get_project_list()
    app.session.login("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.soap.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

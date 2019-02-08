from model.task import Task


def test_add_task(app):
    task = Task(reproducibility="произвольно", severity="большое", priority="высокий", assignee="administrator",
                title="тема", description="описание", steps="шаги по воспроизведению",
                additional_info="дополнительная инфа")
    old_tasks = app.task.get_task_list()
    app.task.create(task)
    new_tasks = app.task.get_task_list()
    assert len(old_tasks) + 1 == len(new_tasks)
    # old_contacts.append(contact)
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    # if check_ui:
    # assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
    # key=Contact.id_or_max)

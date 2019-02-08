from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from model.task import Task


class TaskHelper:

    def __init__(self, app):
        self.app = app

    task_cache = None

    def open_tasks_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("view_all_bug_page.php") and wd.find_element_by_xpath(
                "//input[@name='searchstring']").is_displayed()):
            wd.find_element_by_xpath("//span[@class='menu-text' and contains(text(), 'Список задач')]").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//span[@class='menu-text' and contains(text(), 'Создать задачу')]").click()
        self.set_fields(contact)
        wd.find_element_by_xpath("//input[@value='Создать задачу']").click()
        self.contact_cache = None

    def set_fields(self, contact):
        wd = self.app.wd
        self.set_dropdown_field("reproducibility", contact.reproducibility)
        self.set_dropdown_field("severity", contact.severity)
        self.set_dropdown_field("priority", contact.priority)
        self.set_dropdown_field("handler_id", contact.assignee)
        self.set_text_field("summary", contact.title)
        self.set_text_field("description", contact.description)
        self.set_text_field("steps_to_reproduce", contact.steps)
        self.set_text_field("additional_info", contact.additional_info)

    def set_text_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def set_dropdown_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def get_task_list(self):
        if self.task_cache is None:
            wd = self.app.wd
            self.open_tasks_page()
            self.task_cache = []
            element: WebElement
            for element in wd.find_elements_by_xpath("//table[@id='buglist']//tbody/tr"):
                elements = element.find_elements_by_tag_name("td")
                severity = elements[7].text
                title = elements[10].text
                id = str(int(elements[3].text))
                self.task_cache.append(
                    Task(id=id, severity=severity, title=title))
        return list(self.task_cache)

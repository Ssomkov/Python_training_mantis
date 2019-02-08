from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php") and wd.find_element_by_xpath(
                "//button[contains(text(), 'Создать новый проект')]").is_displayed()):
            wd.find_element_by_xpath("//span[@class='menu-text' and contains(text(), 'Управление')]").click()
            wd.find_element_by_xpath("//a[text()='Управление проектами']").click()

    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[contains(text(), 'Создать новый проект')]").click()
        self.set_fields(project)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        wd.find_element_by_xpath("//a[contains(text(), 'Продолжить')]").click()
        self.project_cache = None

    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//tr/td[1]/a")[index].click()

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_index(index)
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        self.project_cache = None

    def set_fields(self, project):
        wd = self.app.wd
        self.set_text_field("name", project.name)
        self.set_dropdown_field("status", project.status)
        self.set_dropdown_field("view_state", project.view_state)
        self.set_text_field("description", project.description)

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

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            element: WebElement
            for element in wd.find_elements_by_xpath("//th/../../../tbody/tr"):
                elements = element.find_elements_by_tag_name("td")
                name = elements[0].text
                status = elements[1].text
                view_state = elements[3].text
                description = elements[4].text
                self.project_cache.append(
                    Project(name=name, description=description, status=status, view_state=view_state))
        return list(self.project_cache)

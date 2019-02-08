from sys import maxsize


class Task:

    def __init__(self, reproducibility=None, severity=None, priority=None, assignee=None, title=None,
                 description=None, steps=None, additional_info=None, id=None):
        self.reproducibility = reproducibility
        self.severity = severity
        self.priority = priority
        self.assignee = assignee
        self.title = title
        self.description = description
        self.steps = steps
        self.additional_info = additional_info
        self.id = id

    def __repr__(self):
        return "Id: %s; Title: %s; Description: %s" % (self.id, self.title, self.description)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.title == other.title and self.description == other.description

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

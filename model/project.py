from sys import maxsize


class Project:

    def __init__(self, name=None, status=None, view_state=None, description=None, id=None):
        self.name = name
        self.status = status
        self.view_state = view_state
        self.description = description
        self.id = id

    def __repr__(self):
        return "Name: %s; Description: %s" % (self.name, self.description)

    def __eq__(self, other):
        return (
                self.name == other.name and self.description == other.description)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

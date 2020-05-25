"""
    Person class hippokampoi
"""


class Person:
    def __init__(self, name="", role=""):
        self.__name = name
        self.__role = role

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, get_name):
        self.__name = get_name

    @property
    def get_role(self):
        return self.__role

    @get_role.setter
    def set_role(self, get_role):
        self.__role = get_role

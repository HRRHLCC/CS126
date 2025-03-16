class Doggos:
    def __init__(self, name, age, owner):
        self._name = name
        self._age = age
        self._owner = owner

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    def get_owner(self):
        return self._owner

    def set_owner(self, value):
        self._owner = value

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    owner = property(get_owner, set_owner)
class BaseSprite:
    def __init__(self):
        super().__init__()
        self._salary = None
        self._name = None
        self._age = None
        self._who = 'BaseSprite'

    # function to get value of _age
    def get_age(self) -> str:
        return self._age

    # function to set value of _age
    def set_age(self, a):
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    # function to get value of _name
    def get_name(self) -> str:
        return self._name

    # function to set value of _name
    def set_name(self, n):
        self._name = n

    # function to delete _name attribute
    def del_name(self):
        del self._name

    # function to get value of _who
    def get_who(self):
        return self._who

    # function to get value of _salary
    def get_salary(self) -> str:
        return self._salary

    # function to set value of _salary
    def set_salary(self, s):
        self._salary = s

    # function to delete _salary attribute
    def del_salary(self):
        del self._salary

    age = property(get_age, set_age, del_age)

    name = property(get_name, set_name, del_name)

    who = property(get_who)

    salary = property(get_salary, set_salary, del_salary)


class Character(BaseSprite):
    def __init__(self):
        super().__init__()
        self._who = 'Character'


class Actor(Character):
    def __init__(self):
        super().__init__()
        self._who = 'Actor'


class Protagonist(Actor):
    def __init__(self):
        super().__init__()
        self._who = 'Protagonist'


class Antagonist(Actor):
    def __init__(self):
        super().__init__()
        self._who = 'Antagonist'


class Deuteragonist(Protagonist):
    def __init__(self):
        super().__init__()
        self._who = 'Deuteragonist'


class TertiaryCharacter(Deuteragonist):
    def __init__(self):
        super().__init__()
        self._who = 'TertiaryCharacter'

import pygame


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self._salary = None
        self._name = None
        self._age = None
        self._who = 'BaseSprite'

    # function to get value of _age
    def get_age(self):
        return self._age

    # function to set value of _age
    def set_age(self, a):
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    # function to get value of _name
    def get_name(self):
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
    def get_salary(self):
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


if __name__ == '__main__':
    lst = []
    print('[1] - Add [2] - Load [3] - Delete [4] - Edit [5] - Save [6] - Exit')
    x = int(input())
    while x != 6:
        if x == 1:
            print(
                '[1] - BaseSprite [2] - Character [3] - Actor [4] - Protagonist [5] - Antagonist [6] - Deuteragonist [7] - TertiaryCharacter')
            per = int(input())

            if per == 1:
                person = BaseSprite()
                lst.append(person)

            elif per == 2:
                person = Character()
                lst.append(person)

            elif per == 3:
                person = Actor()
                lst.append(person)

            elif per == 4:
                person = Protagonist()
                lst.append(person)

            elif per == 5:
                person = Antagonist()
                lst.append(person)

            elif per == 6:
                person = Deuteragonist()
                lst.append(person)

            elif per == 7:
                person = TertiaryCharacter()
                lst.append(person)

        elif x == 2:
            with open('tmp.txt', 'r') as f:
                print(f.readlines())

        elif x == 3:
            print('Enter object number:')
            obj = int(input())
            if lst[obj]:
                del lst[obj]

        elif x == 4:
            print('Enter object number:')
            obj = int(input())
            if lst[obj]:
                print(vars(lst[obj]))
                print('[1] - Age [2] - Name [3] - Salary')
                num = int(input())

                if num == 1:
                    print('Enter new age:')
                    age = int(input())
                    lst[obj].age = age

                elif num == 2:
                    print('Enter new name:')
                    name = input()
                    lst[obj].name = name

                elif num == 3:
                    print('Enter new salary:')
                    salary = int(input())
                    lst[obj].salary = salary

            elif x == 5:
                with open('tmp.txt', 'w') as f:
                    for obj in lst:
                        f.writelines(obj.who, obj.name, obj.age, obj.salary)

        print('[1] - Add [2] - Load [3] - Delete [4] - Edit [5] - Save [6] - Exit')
        print(lst)
        x = int(input())

    exit(0)

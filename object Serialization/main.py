from hierarchy import *


def serialize(lst: list):
    with open('tmp.txt', 'w') as f:
        for obj in lst:
            character = vars(obj)
            cls = character.get('_who')
            f.writelines('{' + '\'' + str(cls) + '\'' + ': ' + str(character) + '}' + '\n')


def deserialize():
    lst = []

    with open('tmp.txt', 'r') as f:
        Lines = f.readlines()

    classes = []
    for line in Lines:
        classes.append(line.strip())

    objects = {'BaseSprite': BaseSprite(), 'Character': Character(), 'Actor': Actor(),
               'Protagonist': Protagonist(), 'Antagonist': Antagonist(), 'Deuteragonist': Deuteragonist(),
               'TertiaryCharacter': TertiaryCharacter()}

    for cls in classes:
        s = str(cls)
        for item in objects:
            if item in s:
                ss = s[1:]
                pos1 = ss.find('{')
                ss = ss[pos1:]
                ss = ss.replace('\'', '')
                ss = ss.replace('{', '')
                ss = ss.replace('}', '')
                convertedDict = dict((x.strip(), y.strip())
                                     for x, y in (element.split(':')
                                                  for element in ss.split(', ')))

                objects[item].salary = convertedDict['_salary']
                objects[item].name = convertedDict['_name']
                objects[item].age = convertedDict['_age']

            lst.append(objects[item])

    return lst


if __name__ == '__main__':
    lst = []
    objects = {1: BaseSprite(), 2: Character(), 3: Actor(),
               4: Protagonist(), 5: Antagonist(), 6: Deuteragonist(),
               7: TertiaryCharacter()}
    print('[1] - Add [2] - Load [3] - Delete [4] - Edit [5] - Save [6] - Exit')
    x = int(input())
    while x != 6:
        if x == 1:
            print(
                '[1] - BaseSprite [2] - Character [3] - Actor [4] - Protagonist [5] - Antagonist [6] - Deuteragonist [7] - TertiaryCharacter')
            per = int(input())
            for item in objects:
                if item == per:
                    lst.append(objects[item])

        elif x == 2:
            lst = deserialize()

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
                serialize(lst)

        print('[1] - Add [2] - Load [3] - Delete [4] - Edit [5] - Save [6] - Exit')
        print(lst)
        x = int(input())

    serialize(lst)

    exit(0)

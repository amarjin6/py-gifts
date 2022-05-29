import PySimpleGUI as sg

from itertools import chain, cycle

import string

import random


def railFenceEncrypt(plaintext: str, n: int) -> str:
    """
    chain - takes a series of iterables and returns one iterable 'ABC', 'DEF' --> 'A B C D E F'
    cycle - takes one argument as input and returns an infinite sequence ABC --> A B C A B C ...
    zip - takes iterable or containers and returns a single iterator object, having mapped values
    from all the containers: [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ], [ 4, 1, 3, 2 ] -->
    {('Shambhavi', 3), ('Nikhil', 1), ('Astha', 2), ('Manjeet', 4)}
    """
    rows = [""] * n
    zigzag = cycle(chain(range(n - 1), range(n - 1, 0, -1)))
    for i, c in zip(zigzag, plaintext):
        rows[i] += c

    return "".join(rows)


def railFenceDecrypt(text: str, key: int):
    """
    One iteration is 2 * key - 2 elements. Using that, it is possible to find out the len of substrings.
    With knowledge of the length of every single substring it is possible to fill it in.
    After that it is possible to get the initial string by taking symbols from substrings with encryption function.
    :param: text: Cipher text
    :param: key: Encryption key
    :return: Plain text in Russian language
    """
    tmp = [0 for _ in range(key)]
    try:
        for i in range(len(text)):
            tmp[abs(i % (2 * key - 2) - key + 1)] += 1
    except ZeroDivisionError:
        return text
    tmp = list(reversed(tmp))
    offs = 0
    lines = ['' for _ in range(key)]
    for i in range(key):
        lines[key - i - 1] = text[offs:offs + tmp[i]]
        offs += tmp[i]
    tmp.clear()
    ret = ''
    for i in range(len(text)):
        ret += lines[abs(i % (2 * key - 2) - key + 1)][0]
        lines[abs(i % (2 * key - 2) - key + 1)] = lines[abs(i % (2 * key - 2) - key + 1)][1:]
    return ret


def turn_90(mask):
    """
    :param: mask: plain iterator
    :return: mask offset
    """
    return list(zip(*mask[::-1]))


def turningEncrypt(text: str):
    """
    Different way of execution depending on the length of the text.
    Once the number of the symbol is divided by 4, the mask is turned 90 degrees to the right.
    :param: text: Plain text
    :return: Cipher text
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    mask = [
        [True, False, False, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, True, False, False]
    ]
    if len(text) <= 16:
        ret = [['' for _ in range(4)] for _ in range(4)]
        for i in range(len(text)):
            insert = False
            for j in range(4):
                for k in range(4):
                    if mask[j][k] and not ret[j][k]:
                        ret[j][k] = text[i]
                        insert = True
                        break
                if insert:
                    break
            if (i + 1) % 4 == 0:
                mask = turn_90(mask)
        for i in range(4):
            for j in range(4):
                if not ret[i][j]:
                    ret[i][j] = random.choice(string.ascii_uppercase)
    else:
        if len(text) % 16 == 0:
            ret = [[['' for _ in range(4)] for _ in range(4)] for _ in range(len(text) // 16)]
        else:
            ret = [[['' for _ in range(4)] for _ in range(4)] for _ in range(len(text) // 16 + 1)]
        for i in range(len(text)):
            cur = i // 16
            insert = False
            for j in range(4):
                for k in range(4):
                    if mask[j][k] and not ret[cur][j][k]:
                        ret[cur][j][k] = text[i]
                        insert = True
                        break
                if insert:
                    break
            if (i + 1) % 4 == 0:
                mask = turn_90(mask)

        for i in range(4):
            for j in range(4):
                if not ret[-1][i][j]:
                    ret[-1][i][j] = random.choice(string.ascii_uppercase)
    tmp = ''
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            for k in range(len(ret[i][j])):
                tmp += ret[i][j][k]
    ret = tmp
    return ret


def turningDecrypt(text: str):
    """
    Different way of execution depending on the length of the text.
    Given word is written in matrix(es). Then by masking every letter can be taken from the matrix(es).
    :param: text: Cipher text
    :return: Plain text (possibly with not important letters at the end)
    """
    mask = [
        [True, False, False, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, True, False, False]
    ]
    if len(text) <= 16:
        tmp = [['' for _ in range(4)] for _ in range(4)]
        for symb in range(len(text)):
            tmp[symb // 4][symb % 4] = text[symb]
        ret = ''
        for letter in range(len(text)):
            insert = False
            for i in range(len(tmp)):
                for j in range(len(tmp[i])):
                    if mask[i][j] and tmp[i][j]:
                        ret += tmp[i][j]
                        tmp[i][j] = ''
                        insert = True
                        break
                if insert:
                    break
            if (letter + 1) % 4 == 0:
                mask = turn_90(mask)
    else:
        tmp = [[['' for _ in range(4)] for _ in range(4)] for _ in range(len(text) // 16)]
        for symb in range(len(text)):
            cur = symb // 16
            tmp[cur][symb % 16 // 4][symb % 16 % 4] = text[symb]
        ret = ''
        for letter in range(len(text)):
            cur = letter // 16
            insert = False
            for i in range(len(tmp[cur])):
                for j in range(len(tmp[cur][i])):
                    if mask[i][j] and tmp[cur][i][j]:
                        ret += tmp[cur][i][j]
                        tmp[cur][i][j] = ''
                        insert = True
                        break
                if insert:
                    break
            if (letter + 1) % 4 == 0:
                mask = turn_90(mask)
    return ret


def vigenereEncrypt(text: str, key: str):
    """
    :param: text: plain text
    :param: key: your key
    :return: cipher text
    """
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    tmp = ''
    for i in range(len(text)):
        tmp += alphabet[(alphabet.index(key[i % len(key)]) + i // len(key)) % len(alphabet)]
    key = tmp[:len(text)]
    ret = ''
    for i in range(len(text)):
        ret += alphabet[(alphabet.index(text[i]) + alphabet.index(key[i])) % len(alphabet)]
    return ret


def vigenereDecrypt(text: str, key: str):
    """
    :param: text: cipher text
    :param: key: your key
    :return: plain text
    """
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    tmp = ''
    for i in range(len(text)):
        tmp += alphabet[(alphabet.index(key[i % len(key)]) + i // len(key)) % len(alphabet)]
    key = tmp[:len(text)]
    ret = ''
    for i in range(len(text)):
        ret += alphabet[(alphabet.index(text[i]) - alphabet.index(key[i])) % len(alphabet)]
    return ret


def keyGenerate(k):
    """
    Simple function that can immediately generated you a key
    :param k: key size
    :return: key
    """
    s = ''
    for i in range(k):
        s += random.choice(string.ascii_uppercase)

    return s


if __name__ == '__main__':
    layout = [
        [sg.Text('File 1:'), sg.InputText(), sg.FileBrowse(key="-IN1-"),
         sg.Checkbox('Railway fence', key="rail"), sg.Checkbox('Turning grille', key="turn")
         ],
        [sg.Text('File 2:'), sg.InputText(), sg.FileBrowse(key="-IN2-"),
         sg.Checkbox('Vigenere cipher', key="vige")],
        [sg.Output(size=(88, 20), key="output")],
        [sg.OK("OK"), sg.Submit("Encrypt"), sg.Submit("Decrypt"), sg.Exit("Bye"), sg.Text('                 Key:'),
         sg.InputText(key="-KEY-")]
    ]
    window = sg.Window('Simple ciphers', layout)
    while True:  # The Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit" or event == "Bye":
            break
        elif event == "OK":
            path1 = values["-IN1-"]
            file1 = open(path1, 'r')
            Lines = file1.readlines()
            for line in Lines:
                print(line.strip())

            file1.close()
        elif event == "Encrypt":
            alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            window.find_element("output").Update('')
            path2 = values["-IN2-"]
            file2 = open(path2, 'w')
            Linn = []
            Lin = []
            ss = ''
            L = []
            for line in Lines:
                Linn.append(line.strip())

            if values["rail"]:
                for line in Linn:
                    for i in line:
                        i1 = i
                        if alphabet.find(i.lower()) == -1:
                            i1 = ''
                        ss += i1
                    Lin.append(ss)
                    ss = ''

                word = ''
                for i in Lin:
                    word += i
                del Lin
                Lin = []
                Lin.append(word)
                for line in Lin:
                    if len(line) < 1:
                        print('[!] Nothing to encrypt!')
                    else:
                        sKey = str(values["-KEY-"])
                        if sKey:
                            iKey = ''.join(filter(str.isdigit, sKey))
                            if iKey:
                                key = int(iKey)
                                if 1 < key <= len(line):
                                    L.append(railFenceEncrypt(line.upper(), key) + " ")
                                else:
                                    print(f'[!] Bad key! [2..{len(line)}]')

                            else:
                                print('[!] Bad key!')
                        else:
                            print('[!] Bad key!')

            elif values["vige"]:
                for line in Linn:
                    for i in line:
                        i1 = i
                        if alphabet.find(i.lower()) == -1:
                            i1 = ''
                        ss += i1
                    Lin.append(ss)
                    ss = ''

                word = ''
                for i in Lin:
                    word += i
                del Lin
                Lin = []
                Lin.append(word)
                for line in Lin:
                    if len(line) < 1:
                        print('[!] Nothing to encrypt!')
                    else:
                        key = str(values["-KEY-"])
                        ss = ''
                        for i in key:
                            i1 = i
                            if alphabet.find(i.lower()) == -1:
                                i1 = ''
                            ss += i1
                        key = ss
                        if len(key):
                            L.append(vigenereEncrypt(line.lower(), key.lower()).upper() + " ")
                        else:
                            print('[!] Bad key!')

            elif values["turn"]:
                for line in Linn:
                    for i in line:
                        i1 = i
                        if string.ascii_lowercase.find(i.lower()) == -1:
                            i1 = ''
                        ss += i1
                    Lin.append(ss)
                    ss = ''

                word = ''
                for i in Lin:
                    word += i
                del Lin
                Lin = []
                Lin.append(word)
                for line in Lin:
                    if len(line) < 1:
                        print('[!] Nothing to encrypt!')
                    else:
                        L.append(turningEncrypt(line.upper()) + " ")

            file2.writelines(L)
            file2.close()
            file2 = open(path2, 'r')
            Lines = file2.readlines()
            for line in Lines:
                print(line.strip())

            file2.close()

        elif event == "Decrypt":
            alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            window.find_element("output").Update('')
            path2 = values["-IN2-"]
            file2 = open(path2, 'w')
            Linn = []
            Lin = []
            ss = ''
            L = []
            for line in Lines:
                Linn.append(line.strip())

            if values["rail"]:
                for line in Linn:
                    for i in line:
                        i1 = i
                        if alphabet.find(i.lower()) == -1:
                            i1 = ''
                        ss += i1
                    Lin.append(ss)
                    ss = ''

                for line in Lin:
                    if len(line) < 1:
                        print('[!] Nothing to encrypt!')
                    else:
                        key = int(values["-KEY-"])
                        if 1 < key <= len(line):
                            L.append(railFenceDecrypt(line.upper(), key) + " ")
                        else:
                            print(f'[!] Bad key! [2..{len(line)}]')



            elif values["vige"]:
                for line in Linn:
                    for i in line:
                        i1 = i
                        if alphabet.find(i.lower()) == -1:
                            i1 = ''
                        ss += i1
                    Lin.append(ss)
                    ss = ''

                for line in Lin:
                    # key = keyGenerate(len(line))
                    if len(line) < 1:
                        print('[!] Nothing to encrypt!')
                    else:
                        key = str(values["-KEY-"])
                        ss = ''
                        for i in key:
                            i1 = i
                            if alphabet.find(i.lower()) == -1:
                                i1 = ''
                            ss += i1
                        key = ss

                        if len(key):
                            L.append(vigenereDecrypt(line.lower(), key.lower()).upper() + " ")
                        else:
                            print('[!] Bad key!')

            elif values["turn"]:
                for line in Linn:
                    for i in line:
                        i1 = i
                        if string.ascii_lowercase.find(i.lower()) == -1:
                            i1 = ''
                        ss += i1
                    Lin.append(ss)
                    ss = ''

                for line in Lin:
                    if len(line) < 1:
                        print('[!] Nothing to encrypt!')
                    else:
                        L.append(turningDecrypt(line.upper()) + " ")

            file2.writelines(L)
            file2.close()
            file2 = open(path2, 'r')
            Lines = file2.readlines()
            for line in Lines:
                print(line.strip())

            file2.close()

    window.close()

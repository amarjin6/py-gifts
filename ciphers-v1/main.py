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
    return list(zip(*mask[::-1]))


def turningEncrypt(text: str):
    alphabet = string.ascii_letters
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
                    ret[i][j] = alphabet[int(random() * 1000) % (len(alphabet) - 1)]
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
                    ret[-1][i][j] = alphabet[int(random.random() * 1000) % (len(alphabet) - 1)]
    tmp = ''
    for i in range(len(ret)):
        for j in range(len(ret[i])):
            for k in range(len(ret[i][j])):
                tmp += ret[i][j][k]
    ret = tmp
    return ret


def turningDecrypt(text: str):
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


def vigenere(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def vigenereEncrypt(text: str, key: str):
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
        [sg.OK("OK"), sg.Submit("Encrypt"), sg.Submit("Decrypt"), sg.Exit("Bye")]
    ]
    window = sg.Window('Simple ciphers', layout)
    while True:  # The Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "OK":
            path1 = values["-IN1-"]
            file1 = open(path1, 'r')
            Lines = file1.readlines()
            for line in Lines:
                print(line.strip())

            file1.close()
        elif event == "Encrypt":
            window.find_element("output").Update('')
            path2 = values["-IN2-"]
            file2 = open(path2, 'w')
            L = []
            Lin = []
            Lines = [line.rstrip() for line in Lines]
            for line in Lines:
                lll = line.split()
                for ll in lll:
                    Lin.append(ll)

            if values["rail"]:
                for line in Lin:
                    L.append(railFenceEncrypt(line, 3) + " ")

            if values["vige"]:
                for line in Lin:
                    key = keyGenerate(len(line))
                    L.append(vigenere(line, key) + " ")

            file2.writelines(L)
            file2.close()
            file2 = open(path2, 'r')
            Lines = file2.readlines()
            for line in Lines:
                print(line.strip())

            file2.close()

    window.close()

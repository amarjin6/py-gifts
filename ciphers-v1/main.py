import PySimpleGUI as sg

from itertools import chain, cycle

import string

import random


# chain - takes a series of iterables and returns one iterable 'ABC', 'DEF' --> 'A B C D E F'
# cycle - takes one argument as input and returns an infinite sequence ABC --> A B C A B C ...
# zip - takes iterable or containers and returns a single iterator object, having mapped values from all the containers:
# [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ], [ 4, 1, 3, 2 ] --> {('Shambhavi', 3), ('Nikhil', 1), ('Astha', 2), ('Manjeet', 4)}
def railFence(plaintext: str, n: int) -> str:
    rows = [""] * n
    zigzag = cycle(chain(range(n - 1), range(n - 1, 0, -1)))
    for i, c in zip(zigzag, plaintext):
        rows[i] += c

    return "".join(rows)


def turningGrille():
    pass


def vigenere(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def keyGenerate(k):
    s = ''
    for i in range(k):
        s += random.choice(string.ascii_uppercase)

    return s


def progressiveKey():
    pass


if __name__ == '__main__':
    layout = [
        [sg.Text('File 1:'), sg.InputText(), sg.FileBrowse(key="-IN1-"),
         sg.Checkbox('Railway fence', key="rail"), sg.Checkbox('Turning grille', key="turn")
         ],
        [sg.Text('File 2:'), sg.InputText(), sg.FileBrowse(key="-IN2-"),
         sg.Checkbox('Vigenere cipher', key="vige"), sg.Checkbox('Progressive key', key="prog")
         ],
        [sg.Output(size=(88, 20), key="output")],
        [sg.OK("OK"), sg.Submit("Submit"), sg.Cancel("Cancel")]
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
        elif event == "Submit":
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

            if values["rail"] == True:
                for line in Lin:
                    L.append(railFence(line, 3) + " ")

            if values["vige"] == True:
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

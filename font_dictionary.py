#!/usr/bin/env python
# coding:utf-8
import config


def get_font_select(select):
    switcher = {
        0: get_font_one,
        1: get_font_two,
        2: get_font_three,
        3: get_font_four,
        4: get_font_five,
        5: get_font_six,
        6: get_font_seven,
        7: get_font_eight,
        8: get_font_nine,
        9: get_font_ten,
        10: get_font_eleventh
    }
    if config.DEBUG:
        print('Main :: get_font_select > ' + select)
    return switcher.get(select, get_default())()


def get_default():
    return 'Unknowns'


def get_font_one():
    return ["", "", "", "", "",
            "I", "J", "0", "x", "P", "X", "Y", "U", "M", "N",
            "Z", "7", "A", "B", "C", "D", "O", "9", "G", "E",
            "F", "R", "K", "H", "2", "L", "Q", "8", "3", "4",
            "S", "W", "V", "6", "1", "T", "5", "e", "f", "g",
            "h", "i", "j", "k", "n", "l", "m", "z", "y", "v",
            "p", "o", "d", "q", "t", "c", "w", "a", "r", "s",
            "u", "b"]


def get_font_two():
    return ['', '', '', '', '',
            '1', '0', 'Q', 'Y', '8', 'I', '9', 'Z', 'G', 'n',
            'l', 'S', 'O', 'c', 'N', 't', 'E', '5', 'T', 'k',
            'y', 'o', '2', 'j', 'z', 'B', 'm', 'h', 'M', 'L',
            'w', 'i', 'q', 'K', 'R', 'F', 'b', 'U', '7', 'D',
            'f', 'g', 'p', 'd', 'P', 'W', 'v', 'C', '3', 'H',
            'A', 'x', 'r', '6', 'u', 'V', 'X', 'a', 'J', '4',
            's', 'e']


def get_font_three():
    return ['', '', '', '', '',
            'o', 'Q', 'E', '1', 'M', 'P', '6', 'm', 'D', '8',
            'Y', 'S', 'N', 'k', '7', 'b', '5', 'i', '2', '3',
            'R', 'w', 'p', 't', 'I', 'e', 'f', 'z', 'l', 'X',
            '9', 'g', 's', 'r', '0', 'G', 'U', 'B', 'x', 'T',
            'a', 'j', 'V', 'd', 'h', 'A', 'c', 'F', 'K', '4',
            'n', 'H', 'L', 'C', 'Z', 'y', 'W', 'O', 'u', 'J',
            'v', 'q']


def get_font_four():
    return ['', '', '', '', '',
            'w', '7', 'B', 'P', 'a', 'y', 'T', 'n', 'Y', 'c',
            'F', '2', 'Q', 'R', 'z', 'e', 'Z', 'h', 'K', 'I',
            'W', '6', 'X', 'M', 'I', 'N', 'J', '5', '3', 'A',
            'b', 'L', '8', 'p', 'H', 'S', 'V', 'E', 'i', 'f',
            '4', 'd', 'U', 'r', 'C', 't', '1', 'O', 'G', 'D',
            '9', '0', 'v', 'g', 'k', 'u', 'o', 'x', 'q', 's',
            'm', 'j']


def get_font_five():
    return ['', '', '', '', '',
            'N', 'z', 'b', 'J', 'G', 'B', 'H', 'P', 'o', '6',
            't', 'M', 's', 'c', 'p', 'r', '9', '4', 'h', 'X',
            '7', 'a', 'U', 'T', 'n', '1', 'x', 'R', 'i', 'E',
            '2', 'w', 'C', '5', 'k', 'q', 'Q', '0', 'W', 'u',
            '3', 'l', 'j', 'e', 'Y', 'V', 'f', '8', 'S', 'F',
            'K', 'g', 'L', 'd', 'O', 'm', 'v', 'y', 'A', 'l',
            'Z', 'D']


def get_font_six():
    return ['', '', '', '', '',
            'B', 'z', '0', 'v', 'f', 'n', 'x', '7', 'U', 'L',
            't', 'd', 'V', 'w', 'k', 'P', 'e', 'E', '9', '3',
            'W', 'F', 'o', 'M', 'K', '5', 'a', 'N', 'H', 'O',
            '2', 'b', 'Q', 'r', 'Y', 'G', 'i', 'h', '8', 'S',
            '1', 'T', 'p', 'c', 's', 'I', 'm', '6', 'u', 'X',
            'A', 'y', 'l', 'C', '4', 'J', 'q', 'j', 'D', 'g',
            'R', 'Z']


def get_font_seven():
    return ['', '', '', '', '',
            'c', 'E', '9', 'q', '4', 'S', 'T', 'j', 'n', 'l',
            'g', 'N', 'h', 'B', 'D', '0', 'y', 's', 'G', '5',
            'C', 'w', 'M', 'e', 'u', 'p', 'x', 'K', 'H', 'L',
            'i', 'W', '3', '7', 'F', 't', 'o', 'Y', 'Z', 'R',
            'A', 'm', '8', '2', 'V', 'Q', 'b', 'O', 'v', '1',
            'f', 'P', 'z', 'X', 'a', 'd', 'l', 'J', 'k', 'r',
            '6', 'U']


def get_font_eight():
    return ['', '', '', '', '',
            'l', 'Q', '7', 'n', 'Y', 'U', 'p', 'd', 'z', 'h',
            'E', 'O', 'B', '5', 'u', 'X', '8', 'y', '4', 'g',
            'A', 'o', 'f', 'v', '2', '0', 'K', 'C', 'R', 'W',
            'N', 'T', 'S', 'q', 'G', 'V', 't', 'k', 's', 'M',
            '1', 'r', 'e', 'j', '6', 'i', 'P', 'c', 'J', 'H',
            'L', 'w', 'm', 'l', '3', 'a', 'D', 'b', 'F', 'x',
            'Z', '9']


def get_font_nine():
    return ['', '', '', '', '',
            '2', 'R', 'G', 'h', 'm', '9', 'O', 'q', 'B', 'Z',
            'S', 'g', '5', 'H', 'K', 't', 'k', 'a', 'z', 'W',
            'D', 'N', 'c', 'u', 'r', 'L', 'l', 's', 'i', 'E',
            '3', 'M', 'T', 'X', 'b', 'p', 'x', 'y', 'v', 'Y',
            '0', '4', 'Q', 'w', 'f', 'U', 'o', 'C', 'A', '8',
            '6', 'j', 'P', 'F', 'V', 'J', 'd', '7', 'e', 'l',
            '1', 'n']


def get_font_ten():
    return ['', '', '', '', '',
            'v', 'S', 'G', 'H', 'K', '4', 'R', 'x', 'V', 'l',
            'M', 'F', '3', 'J', 'I', 'i', '2', '0', 'A', 'U',
            'y', 'T', 'Q', '9', 'Y', 'B', 'h', 'j', 'E', 'D',
            'P', '7', 'Z', 'f', 'd', 'e', 'L', 'b', 'u', 'W',
            'm', '1', 's', 'C', '8', 'g', 'o', 'w', 'r', 't',
            'n', 'z', 'k', '5', 'c', 'a', 'N', 'X', 'q', 'O',
            '6', 'p']


def get_font_eleventh():
    return ['', '', '', '', '',
            'C', 'Q', 'h', 'W', 'A', 'a', '7', '5', 'z', 'y',
            'r', 'K', '6', 'k', '3', 'H', 'R', '8', 'G', 'v',
            'D', 'e', 'B', 'p', 'V', 'f', 'j', 'X', 'w', 'I',
            'E', 'o', 'S', 'T', 'q', 'F', 'g', 'P', 'c', 'd',
            'M', 'U', 'N', '0', 'm', 'Y', 'i', 'I', '2', 'n',
            't', '1', '9', 'b', 'L', 'u', 's', 'O', 'x', 'J',
            '4', 'Z']


if __name__ == '__main__':
    print(get_font_select(6))

#!/usr/bin/env python
# coding:utf-8

from fontTools.ttLib import TTFont

import config
import font_dictionary


def file_write(fileName, content):
    if config.DEBUG:
        print('Main :: file_write > ' + f'{fileName}' + f'{content}')
    with open(fileName, "a+") as f:
        f.write(content + '\n')
        f.close()


def get_font_analyze(select):
    if config.DEBUG:
        print('Main :: get_font_analyze > ' + f'{select}')
    fonts = TTFont('./font/sfont' + str(select) + ".woff")
    fonts_names = fonts.getGlyphOrder()
    texts = font_dictionary.get_font_select(select)
    fonts_name = {}
    for index, value in enumerate(texts):
        a = fonts_names[index].replace('uni', '').lower()
        fonts_name[a] = value
    return fonts_name


def get_font_restore(text, select):
    if config.DEBUG:
        print('Main :: get_font_restore > ' + f'{text}' + f'{select}')
    texts = text.replace('', '')
    texts = repr(texts.encode('utf-8').decode('utf-8'))
    texts = eval(repr(texts).replace('u\'', ''))
    texts = eval(repr(texts).replace('\'', ''))
    font_analyze = get_font_analyze(select)
    for key in font_analyze:
        texts = texts.replace(r'\u' + key, str(font_analyze[key]))
    # result = texts.encode('latin-1').decode('unicode_escape')
    result = texts.encode('utf-8').decode('utf-8')
    result = result.replace('\\', '')
    return result


if __name__ == '__main__':
    print(get_font_restore("", 10))

    save_file_path = './data/data1.txt'
    t = 'eqwqeqewqew'
    file_write(save_file_path, t)

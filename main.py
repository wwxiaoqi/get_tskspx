#!/usr/bin/env python
# coding:utf-8
import random
import re
import time

import config
import tools
import web

if __name__ == '__main__':
    web.tskepx_login()
    web.onclick_select_topic()

    question_line = int(web.get_question_line())

    current_num = 0
    while current_num <= question_line:
        print('%s : %s' % (current_num, question_line))
        web.onclick_check_answer()
        time.sleep(random.uniform(1, 3))

        topic = web.get_question_topic()
        a = web.get_question_option_a()
        b = web.get_question_option_b()
        c = web.get_question_option_c()
        d = web.get_question_option_d()
        answer = web.get_question_answer()

        topic_encryption_data = int(re.compile(r'\d+').findall(str(web.get_question_topic_decrypt()))[0])
        answer_encryption_data = int(re.compile(r'\d+').findall(str(web.get_question_answer_decrypt()))[0])
        topic_decrypt = tools.get_font_restore(str(topic), topic_encryption_data)
        answer_decrypt = tools.get_font_restore(str(answer), answer_encryption_data)
        a_decrypt = tools.get_font_restore(str(a), topic_encryption_data)
        b_decrypt = tools.get_font_restore(str(b), topic_encryption_data)
        c_decrypt = tools.get_font_restore(str(c), topic_encryption_data)
        d_decrypt = tools.get_font_restore(str(d), topic_encryption_data)

        save_file_path = './data/data.txt'
        save_texts = (
            f'{topic_decrypt}'
            f'{a_decrypt}'
            f'{b_decrypt}'
            f'{c_decrypt}'
            f'{d_decrypt}'
            f'{answer_decrypt}'
        )
        tools.file_write(save_file_path, save_texts)

        if config.DEBUG:
            print('Main :: ' + f'{save_file_path}' + f'{save_texts}')

        web.onclick_next_title()
        time.sleep(random.uniform(1, 3))
        current_num += 1

#!/usr/bin/env python
# coding:utf-8

from selenium import webdriver

import config

driver = webdriver.Chrome(executable_path=r'C:\Program Files Tools\Python27\Scripts\chromedriver.exe')


def tskepx_login():
    if config.DEBUG:
        print('Main :: tskepx_login')
    driver.get(config.WEBSITE)
    input_name = driver.find_element_by_id('userid')
    input_password = driver.find_element_by_id('password')
    input_login = driver.find_element_by_class_name('btn_indexlog1')
    input_name.send_keys(config.ACCOUNT)
    input_password.send_keys(config.PASSWORD)
    input_login.click()


def get_question_line():
    if config.DEBUG:
        print('Main :: get_question_line')
    return driver.find_element_by_xpath("//table[2]//table[1]//tr//td/table//td/input[1]").get_attribute('value')


def get_question_topic():
    if config.DEBUG:
        print('Main :: get_question_topic')
    return is_selenium_element("//table[2]//table[1]//tr//td//tr/td")


def get_question_option_a():
    if config.DEBUG:
        print('Main :: get_question_option_a')
    return is_selenium_element("//table[2]//table[1]//tr//td//table//tr[2]//td")


def get_question_option_b():
    if config.DEBUG:
        print('Main :: get_question_option_b')
    return is_selenium_element("//table[2]//table[1]//tr//td//table//tr[3]//td")


def get_question_option_c():
    if config.DEBUG:
        print('Main :: get_question_option_c')
    return is_selenium_element("//table[2]//table[1]//tr//td//table//tr[4]//td")


def get_question_option_d():
    if config.DEBUG:
        print('Main :: get_question_option_d')
    return is_selenium_element("//table[2]//table[1]//tr//td//table//tr[5]//td")


def get_question_answer():
    if config.DEBUG:
        print('Main :: get_question_answer')
    return is_selenium_element("//table[2]//table[1]//tr//td//table[2]//tr")


def get_question_topic_decrypt():
    if config.DEBUG:
        print('Main :: get_question_topic_decrypt')
    return driver.find_element_by_xpath("//table[2]//table[1]//tr//td//table[2]//tr//span").get_attribute('class')


def get_question_answer_decrypt():
    if config.DEBUG:
        print('Main :: get_question_answer_decrypt')
    return driver.find_element_by_xpath("//table[2]/tbody//table/tbody//table/tbody//td/span[2]").get_attribute('class')


def onclick_check_answer():
    if config.DEBUG:
        print('Main :: onclick_check_answer')
    driver.find_element_by_xpath('//table[2]//table[1]//tr//td/table//td/a[1]').click()


def onclick_next_title():
    if config.DEBUG:
        print('Main :: onclick_next_title')
    driver.find_element_by_xpath('//table[2]//table[1]//tr//td/table//td/a[4]').click()


def onclick_select_topic():
    if config.DEBUG:
        print('Main :: onclick_select_topic')
    driver.find_element_by_xpath('/html/body/table/tbody/tr/td//dd[2]').click()
    driver.find_element_by_xpath('/html/body/table/tbody/tr//table[2]/tbody/tr[2]//td[2]//a').click()


def is_selenium_element(path):
    try:
        xpath = driver.find_element_by_xpath(path).text
        if config.DEBUG:
            print('Main :: is_selenium_element > ' + xpath)
        return xpath
    except Exception as e:
        if config.DEBUG:
            print('Main :: is_selenium_element > find_element_by_xpath > None ' + str(e))
        return ''

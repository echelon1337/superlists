#coding: utf-8
#TDD_1 functional_tests
#21.02.2017 eezme


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title

def some_test_funtion():
    """Description"""
    var = 0
    var2 = 11
    pass
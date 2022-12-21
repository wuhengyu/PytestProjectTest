# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 20:07
# @Author  : Walter
# @File    : test_sample.py
# @License : (C)Copyright Walter
# @Desc    : 创建一个简单的测试用例
def func(x):
    return x + 1

def test_answer1():
    assert func(3) == 5

def test_answer2():
    assert func(4) == 5
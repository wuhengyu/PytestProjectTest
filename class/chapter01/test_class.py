# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 23:42
# @Author  : Walter
# @File    : test_class.py
# @License : (C)Copyright Walter
# @Desc    :
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "Te1stClass")
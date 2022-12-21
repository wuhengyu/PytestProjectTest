# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 1:17
# @Author  : Walter
# @File    : test_foocompare.py
# @License : (C)Copyright Walter
# @Desc    :

# test_foocompare.py内容
class Foo(object):
    def __init__(self,val):
        self.val = val

    def __eq__(self,other):
        return self.val == other.val

def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2

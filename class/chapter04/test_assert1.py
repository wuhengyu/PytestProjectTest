# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 0:48
# @Author  : Walter
# @File    : test_assert1.py
# @License : (C)Copyright Walter
# @Desc    :

# test_assert1.py文件内容
def f():
    return 3

def test_function():
    assert f() == 4


def test_function2():
    a = 1001
    assert a % 2 == 0, "值为奇数,应为偶数"
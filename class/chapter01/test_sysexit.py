# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 23:39
# @Author  : Walter
# @File    : test_sysexit.py
# @License : (C)Copyright Walter
# @Desc    : 断言抛出了指定异常

import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
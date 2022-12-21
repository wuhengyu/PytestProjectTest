# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 1:04
# @Author  : Walter
# @File    : test_match.py
# @License : (C)Copyright Walter
# @Desc    :

import pytest

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError,match=r'.* 123 .*'):
        myfunc()
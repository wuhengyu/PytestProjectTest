# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 0:51
# @Author  : Walter
# @File    : test_zero_division.py
# @License : (C)Copyright Walter
# @Desc    : 使用pytest.raises作为上下文管理器来进行异常断言

import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
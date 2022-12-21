# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 0:58
# @Author  : Walter
# @File    : test_ZeroDivisionError.py
# @License : (C)Copyright Walter
# @Desc    :
import pytest


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
        1 / 0
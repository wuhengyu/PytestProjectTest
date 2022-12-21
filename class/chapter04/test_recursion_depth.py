# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 0:54
# @Author  : Walter
# @File    : test_recursion_depth.py
# @License : (C)Copyright Walter
# @Desc    :
import pytest


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)
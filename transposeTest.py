#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'zsy'
__mtime__ = '2016/10/22'"""
import pickle

with open('csrtest_pickle', 'rb') as f:
    csrtest = pickle.load(f)

csrtesttrans = csrtest.transpose().tocsr()
print(csrtesttrans)
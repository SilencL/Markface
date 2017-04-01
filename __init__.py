#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2017/3/31 15:21
@author: Silence
'''
import os

abs_uploadface = os.path.join(os.getcwd(),'static','uploads')
abs_markedface = os.path.join(os.getcwd(),'static','markface')

rela_uploadface = os.path.join('static','uploads')
rela_markface = os.path.join('static','markface')

print abs_uploadface,abs_markedface,rela_uploadface,rela_markface

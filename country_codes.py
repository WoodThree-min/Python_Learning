#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:36:13 2020

@author: risugi
"""

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回 Pygal 使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # 如果没有找到指定的国家，就返回 None

    return None
    
# print(get_country_code('Arab World'))
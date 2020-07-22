#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:31:54 2020

@author: risugi
"""

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])
    
    
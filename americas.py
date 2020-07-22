#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:46:14 2020

@author: risugi
"""

from pygal.maps.world import World

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz','cr','gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
                         'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
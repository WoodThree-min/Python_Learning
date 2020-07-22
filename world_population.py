#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 22:12:45 2020

@author: risugi
"""

import json
from pygal.maps.world import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from country_codes import get_country_code



#%% download data to a list
filename = '/Users/risugi/Desktop/course1/pcc/chapter_16/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    

#%% Create a dict with populations
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        #     print(code + ":" + str(population))
        # else:
        #     print('Error - ' + country_name)
            
        # print(country_name + ": " + str(population))
        
#%% set 3 groups of all the countries
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop
        
#%% see how many countries each group contains
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))


#%%

wm_style = RotateStyle('#993366', base_style=LightColorizedStyle)
wm = World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_populations.svg')


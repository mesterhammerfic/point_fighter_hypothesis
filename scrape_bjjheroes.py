#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:46:26 2019

@author: root
"""

import requests, bs4
res = requests.get('https://www.bjjheroes.com/a-z-bjj-fighters-list')
res.raise_for_status()
bjjheroes = bs4.BeautifulSoup(res.text, features = 'lxml')



def label_maker(name, number_of_elements):
    list_of_elements = []
    for number in list(range(1,number_of_elements+1)):
        suffix = ''
        if number%2 == 0:
            suffix = 'even'
        else:
            suffix = 'odd'
        element = ".{}-{} {}".format(name, number, suffix)
        list_of_elements.append(element)
    return list_of_elements

rows = label_maker("row", 5)

#list_of_names = list(map(lambda class_tag: bjjheroes.select(class_tag).text(), rows))

#print(list_of_names)

print(bjjheroes.select('tr')[1])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:43:22 2023

@author: havardalme
"""

import lister_for_del_1



def liste_tall_over_5(liste):
    sum = 0
    for element in liste:
        if element>5:
            sum += element-5
        else:
            sum += 0
    return sum
    
    


resultat = liste_tall_over_5(lister_for_del_1.temperaturer)
print(resultat)
    
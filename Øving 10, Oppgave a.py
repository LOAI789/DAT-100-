#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:45:22 2023

@author: havardalme
"""
from datetime import datetime

def int_konvertering(verdi):
    try:
        return int(verdi)
    except ValueError:
        return None

def float_konvertering(verdi):
    try:
        return float(verdi.replace(',', '.'))
    except ValueError:
        return None

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, '%d.%m.%Y')
    except ValueError:
        return None

def les_værdata(filnavn):
    with open(filnavn, 'r', encoding='utf-8') as file:
        next(file)  
        værdata = []
        for linje in file:
            navn, stasjon, dato_str, snoedybde_str, nedbor_str, temp_str, skydekke_str, vind_str = linje.strip().split(';')
            dato = parse_date(dato_str)
            snoedybde = int_konvertering(snoedybde_str) if snoedybde_str not in ['-', ''] else None
            nedbor = float_konvertering(nedbor_str) if nedbor_str not in ['-', ''] else None
            temp = float_konvertering(temp_str) if temp_str not in ['-', ''] else None
            skydekke = float_konvertering(skydekke_str) if skydekke_str not in ['-', ''] else None
            vind = float_konvertering(vind_str) if vind_str not in ['-', ''] else None
            
            værdata.append({
                'Dato': dato,
                'Snødybde': snoedybde,
                'Nedbør': nedbor,
                'Middeltemperatur': temp,
                'Skydekke': skydekke,
                'Vind': vind
            })
    return værdata


værdata=les_værdata('snoedybder_vaer_en_stasjon_dogn.csv')













#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Atakan Tüsüz - Final 1. Soru

liste = []

with open('sayi.txt', 'r') as oku:

 veri = oku.readlines()

for line in veri :
    liste.append(int(line[11:14]))
    liste.sort()

print liste
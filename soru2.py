#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Atakan Tüsüz - Final 2. Soru

liste = []
with open('sayi.txt', 'r') as oku:
 veri = oku.readlines()
for line in veri :
    liste.append(int(line[11:14]))
    liste.sort()


for i in range(len(liste)/2):
  liste2 = [liste[-1-i], liste[i], liste.pop(i+2)]   # "Pop index out of range" veriyor ama çalışıyor

  print liste2
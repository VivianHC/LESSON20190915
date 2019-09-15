#!/usr/bin/python
# -*- coding: UTF-8 -*-

Sn = 100.0
Hn = Sn / 2

for n in range(2,11):
    Sn += 2 * Hn
    Hn /= 2

print ('Total of road is %0.4f' % Sn)
print ('The tenth is %0.4f meter' % Hn)

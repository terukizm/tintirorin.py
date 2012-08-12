#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import random

cnt = 0
rep = 1000000
throw = 3

for r in range(rep):
    for i in range(1,throw):
        deme1 = random.randint(1,6)
        deme2 = random.randint(1,6)
        deme3 = random.randint(1,6)
        demes = set([deme1, deme2, deme3])
        deme123 = set([1,2,3])
        deme456 = set([4,5,6])
        if(demes == deme456):
            # win(456)
            break
        if(deme1 == deme2 or deme2 == deme3 or deme1 == deme3):
            # win or draw
            break
        if(demes == deme123):
            # lose(123)
            cnt += 1
            break
        if(i == throw):
            # lose(no part)
            cnt += 1

print cnt / float(rep)


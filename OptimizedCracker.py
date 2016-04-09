#!/usr/bin/python

import sys
import random

num = int(sys.argv[1])
count = 0

numlist = []

for i in range(2, num-1):
	numlist.append(i)

random.shuffle(numlist)

for i in range(0, len(numlist)):
	one = numlist[i]
	two = num / numlist[i]

	count = count + 1

	print (("Try %s: %s * %s: %s") % (count, one, two, one * two))

	if one * two == num:
		break
#!/usr/bin/python

import sys
import random

num = 179425579
count = int(sys.argv[1])

while True:
	one = random.randint(2, num - 1);
	two = random.randint(2, num - 1);

	count = count + 1

	print (("Try %s: %s * %s: %s") % (count, one, two, one * two));

	if one * two == num:
		break;

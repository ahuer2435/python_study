# -*- coding: utf-8 -*-
import itertools
for key, group in itertools.groupby("AAAADDADGGGH"):
	print key, list(group)
#只选取相邻元素，为啥要用list？
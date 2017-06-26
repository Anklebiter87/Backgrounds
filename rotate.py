#!/usr/bin/env python

import os
import re
import random



filelist = []
BackgroundDir = "{}/Backgrounds".format(os.getenv("HOME"))

os.chdir(BackgroundDir)
for i in os.listdir('.'):
	if(re.match(i,"rotate.*") != -1):
		filelist.append(re.sub(' ', '\ ',i))

number = random.randrange(0,len(filelist))
cmd = "feh --bg-scale {}".format(filelist[number])
os.system(cmd)

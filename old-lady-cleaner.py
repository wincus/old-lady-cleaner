#!/usr/bin/env python

__author__ = "jmoyano@silice.biz"
__relase__ = "29/06/2008"
__license__ = "GPL"

import os
import shutil
import tarfile

class conf:
	pass

if len(os.sys.argv) <> 2:
	os.sys.stderr.write("Use: " + os.sys.argv[0] + " target\n")
	os.sys.exit(1)
else:
	target=os.sys.argv[1]

# tweak accordingly to your convenience
c = conf()
c.nrou = 12
c.comp = 128
c.dir = target

if not os.path.isdir(c.dir):
	os.sys.stderr.write("Oops, dir doesnt exists\n")
	os.sys.exit(1)

items = []

if c.dir[-1] <> "/":
	c.dir+="/"

for item in os.listdir(c.dir):
		items.append((os.stat(c.dir+item).st_mtime, c.dir+item))

items.sort(reverse=True)

for timestamp,item in items[c.nrou:c.comp+c.nrou]:
	if os.path.isdir(item):
		mytar = tarfile.open(item+'.tgz', "w:gz")
		mytar.add(item)
		mytar.close()
		os.utime(item+'.tgz',(timestamp,timestamp))
		shutil.rmtree(item, True)
		
for timestamp,item in items[c.nrou+c.comp:]:
		if os.path.isdir(item):
				shutil.rmtree(item,True)
		elif os.path.isfile(item):
				os.unlink(item)
		else:
			os.sys.stderr.write("Oops dont know what " + item + " is\n")

os.sys.exit(0)

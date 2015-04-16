from numpy import *
from os import listdir
from os.path import isfile, join
from os import rename
from os import chdir

if __name__=='__main__':
	filepath = '/homeappl/home/gcao/Dataset/FamilyAttribute/QPdecomp/d0/'
	chdir(filepath)
	onlyfiles = [ f for f in listdir(filepath) if isfile(join(filepath, f)) ]
	p = '.model'
	for f in onlyfiles:
		if p in f:
			l = f.split("_")
			num = l[1].split(".")[0]
			newname = l[0] + "_" + num.zfill(4) + ".model"
			print newname
			rename(f, newname)

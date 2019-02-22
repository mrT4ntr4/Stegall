#!/usr/bin/python

import subprocess as sb
import sys
import os

sys.path.append('..')
import stegall as stg

def launch(arg2):
	prog = 'Stegsolve.jar'
	print stg.color.OKBLUE + "\nStegsolve does not support Command Line Execution... Sry :(\nYou have to open the file manually!! C'mon Don't be Lazy XD" + stg.color.END
	stg.spinning_cursor()
	dotLoc = arg2.find('.')
	ext = arg2[dotLoc+1::]
	if ext in ['jpeg','jpg','gif','tiff','png','bmp','tif','jif','jfif','jp2','jpx','j2k','j2c','fpx','pcd']:
		os.system('chmod +x ' + prog)
		os.system('./'+prog)
	else :
		stg.io_error()
		exit()	

def stsolve(arg2):

	if os.path.isfile('Stegsolve.jar'):
		launch(arg2)
	else:
		stg.dep_check()
		stg.download("http://www.caesum.com/handbook/Stegsolve.jar",'Stegsolve.jar')
		launch(arg2)

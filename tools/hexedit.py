#!/usr/bin/python

import subprocess as sb
import sys
import os

import stegall as stg

prog = 'hexcurse'

def launch(arg2):
	if  os.path.isfile(arg2):
		os.system(prog +' ' +arg2)
	else:
		stg.io_error()
		exit()

def hedit(arg2):
	try :
		launch(arg2)
		
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			stg.prog_install(prog)
			launch(prog)
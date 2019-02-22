#!/usr/bin/python

import subprocess as sb
import sys

import stegall as stg

prog = 'exiftool'

def lauch(arg2):
	test = sb.Popen([prog,arg2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = output.find('File not found')
	if res==7:
		stg.io_error()
		exit()
		return
	else:
		test = sb.call([prog,arg2]) 	


def ef(arg2):
	try :
		lauch(arg2)
		
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			stg.prog_install(prog)
			lauch(arg2)

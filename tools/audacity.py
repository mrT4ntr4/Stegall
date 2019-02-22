#!/usr/bin/python

import subprocess as sb
import sys
import os

import stegall as stg

prog = 'audacity'

def launch(arg2):
 	if os.path.isfile(arg2):
		dotLoc = arg2.find('.')
		ext = arg2[dotLoc+1::]
		if ext in ['wav','ogg','mp3','m4a']:
			print stg.color.OKYELLOW +"Opening "+arg2+" in Audacity"+stg.color.END
			stg.spinning_cursor()
			sb.check_output(['xhost','+'])
			sb.call([prog,arg2], shell=False,stdout=sb.PIPE, stderr=sb.PIPE)
		else:
			stg.io_error()
			exit()
	else:		
		stg.io_error()
		exit()


def auda(arg2):
 try:
 	launch(arg2)

 except OSError as e:
 	if e.errno == os.errno.ENOENT:
		stg.prog_install([prog,arg2])
		launch(arg2)	
#!/usr/bin/python

import subprocess as sb
import sys
import os

import stegall as stg

prog = 'pngcheck'

def dwn_pngcsum(prog2):
	stg.dep_check()
	stg.download("http://schaik.com/png/pngcsum/pngcsum-v01.tar.gz","pngcsum-v01.tar.gz")
	sb.call(["tar","-xvf", "pngcsum-v01.tar.gz"])
	os.system('chmod +x '+prog2)						


def launch(arg2):
	test = sb.Popen([prog,arg2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = 'No such file or directory' in output
	if res:
		stg.io_error()
		exit()
		return
	else:
		try:
			print output
			prog2 = 'pngcsum'
			p = sb.Popen(['./'+prog2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
			yn1 = 'y'
			while yn1:
				while (yn1):
					yn1 = raw_input('Do you want to use '+prog2+' to correct any checksum error if present (y/n)')

					if yn1=='y':
						try:
							target_img=raw_input('\nEnter the Target Corrected Image name\n')
							os.system('./'+prog2 +' ' + arg2 +' ' + target_img)	
							exit()
						except OSError as e:
							if e.errno == os.errno.ENOENT:
								dwn_pngcsum()
								target_img=raw_input('\nEnter the Target Corrected Image name\n')
								os.system('./'+prog2 +' ' + arg2 +' ' + target_img)	
								fire()
								exit()
					elif yn1=='n':
						print stg.color.FAIL
						exit("Program Exited")
					else :
						print("Please enter a vaild choice")
				continue

		except OSError as e:
			if e.errno == os.errno.ENOENT:
				dwn_pngcsum('pngcsum')				



def pngch(arg2):
	dotLoc = arg2.find('.')
	ext = arg2[dotLoc+1::]
	if ext == 'png':	
		try :
			launch(arg2)
		except OSError as e:
			if e.errno == os.errno.ENOENT:
				stg.prog_install(prog)
				launch(arg2)
	else:
		stg.io_error()
		exit()


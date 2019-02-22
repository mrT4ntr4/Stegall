#!/usr/bin/python


import subprocess as sb
import sys
import os

import stegall as stg

def strings(arg2):
	prog = 'strings'
	try :
		test = sb.Popen([prog,arg2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
		output = test.communicate()[0]
		res = output.find('No such file')
		if res>22:
			stg.io_error()
			exit()
			return
  		else:
			yn1 = 'y'
			while yn1:
				while (yn1):
					print stg.color.OKBLUE
					yn1 = raw_input('Do you want to search for some specific strings (y/n)')
					print stg.color.END
					if yn1=='y':
							grep_string=raw_input("\nEnter the Pattern/String to search for \n")
							os.system('strings '+arg2+' | grep '+grep_string)
							exit()
					elif yn1=='n':
						sb.call([prog,arg2])
						exit()
						
					else :
						print("Please enter a vaild choice")
				continue			 			 
		
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			stg.prog_install('binutils')


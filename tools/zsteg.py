#!/usr/bin/python

import subprocess as sb
import sys
import os

import stegall as stg

prog = 'zsteg'

def launch(arg2):
	test = sb.Popen([prog,arg2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = 'No such file or directory' in output
	if res:
		stg.io_error()
		exit()
		return
	else:
		dotLoc = arg2.find('.')
		ext = arg2[dotLoc+1::]
		if ext in ['bmp','png']:
			yn1 = 'y'
			while yn1:
				while (yn1):
					print stg.color.OKBLUE
					yn1 = raw_input('Do you want run zsteg with additional flags (y/n)')
					print stg.color.END
					if yn1=='y':
						try:
							flags=raw_input("\nEnter the flags in a one liner\n")
							os.system(prog +' ' + arg2 +' ' + flags)	
							exit()
						except OSError as e:
							if e.errno == os.errno.ENOENT:
								stg.prog_install(prog2)
								flags=raw_input("\nEnter the flags in a one liner\n")
								os.system(prog +' ' + arg2 +' ' + flags)	
								fire()
								exit()
					elif yn1=='n':
						os.system(prog+' '+arg2)
						exit()
						
					else :
						print("Please enter a vaild choice")
				continue
		else:
			stg.io_error()
			exit()


def zst(arg2):
	try :
		launch(arg2)
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			print stg.color.OKYELLOW + "Cooking ruby Today XD " +stg.color.END
			stg.prog_install('ruby-full')
			if os.geteuid() == 0:
				print stg.color.OKYELLOW + "Better take zsteg as salad"+ stg.color.END
				os.system('gem install zsteg')
				print stg.color.OKYELLOW + "zsteg Successfully Installed"+ stg.color.END
			else:
				root_exit()
			launch(arg2)


#!/usr/bin/python

import subprocess as sb
import sys
import os

import stegall as stg

prog = 'Steganography/WavSteg.py'


def execute(arg2):
 no_lsb=raw_input("\nEnter the no. of LSB's to use\n")
 os.system('chmod +x ' + prog)
 os.system('python3 '+prog + ' -r -s '+arg2+' -o output.txt -n '+ no_lsb)
 print stg.color.OKBLUE + "\nHidden contents have been saved to output.txt" + stg.color.END


def launch(arg2):
	test = sb.Popen(['python3','--version'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = 'Python 3.' in output
	if not res:
		print "You need to have Python ver_3.* to run WavSteg"
		yn1 = 'y'
		while yn1:
			while (yn1):
				yn1 = raw_input('Do you want to install it now (y/n)')
				if yn1=='y':
					stg.prog_install('python3.6')
					execute(arg2)
				elif yn1=='n':
					print stg.color.FAIL
					exit("Program Exited")
				else :
					print("Please enter a vaild choice")
			continue
	else:
		execute(arg2)			

def wave(arg2):
	dotLoc = arg2.find('.')
	ext = arg2[dotLoc+1::]
	if ext == 'wav':
		if os.path.isfile(prog):
			launch(arg2)
		else:
			print stg.color.OKBLUE + "Gathering necessary files for wavsteg\n" + stg.color.END			
			spinning_cursor()
			try:
				os.system("git clone https://github.com/ragibson/Steganography.git")
				launch(arg2)
			except OSError as e:
				if e.errno == os.errno.ENOENT:
					stg.prog_install('git')
					launch(arg2)
	else :
		stg.io_error()
		exit()


#!/usr/bin/python

import subprocess as sb
import sys
import os

sys.path.append('..')
import stegall as stg

def sonic(arg2):
 prog = 'sonic-visualiser'
 try:
 	if os.path.isfile(arg2):
		dotLoc = arg2.find('.')
		ext = arg2[dotLoc+1::]
		if ext in ['wav','ogg','mp3']:
			sb.call([prog,arg2])
		else:
			stg.io_error()
			exit()
	else:		
		stg.io_error()
		exit()

 except OSError as e:
 	if e.errno == os.errno.ENOENT:
		stg.dep_check()
  		stg.download("https://code.soundsoftware.ac.uk/attachments/download/2438/sonic-visualiser_3.2.1_amd64.deb",'sonic-visualiser_3.2.1_amd64.deb')
		sb.call(["dpkg","-i", "sonic-visualiser_3.2.1_amd64.deb"])
		sb.call(["apt", "--fix-broken", "install"])		
		sb.call([prog,arg2])
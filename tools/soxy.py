#!/usr/bin/python

import subprocess as sb
import sys
import os


import stegall as stg

prog = 'sox'

def show_image(width=None, height=None):
	import matplotlib.pyplot as plt
	import matplotlib.image as mpimg
	import matplotlib as mpl
	mpl.rcParams['savefig.pad_inches'] = 0
	figsize = None if width is None else (width, height)
	fig = plt.figure(figsize=figsize)
	ax = plt.axes([0,0,1,1], frameon=False)
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)
	plt.autoscale(tight=True)
	img = mpimg.imread('spectrogram.png')
	plt.imshow(img)
	plt.show()
    


def launch(arg2):
 	if os.path.isfile(arg2):
		dotLoc = arg2.find('.')
		ext = arg2[dotLoc+1::]
		if ext in ['wav','ogg','mp3','flac']:
			sp = sb.Popen([prog,'--version'], shell=False,stdout=sb.PIPE, stderr=sb.PIPE)
			print stg.color.OKYELLOW +"Opening "+arg2+" using Sox"+stg.color.END
			yn1 = 'y'
			while yn1:
				while (yn1):
					print stg.color.OKBLUE
					yn1 = raw_input('Do you want to trim the spectrogram (y/n)')
					print stg.color.END
					if yn1=='y':
							trim_point=raw_input("\nEnter the Trim Start Point \n")
							trim_length=raw_input("\nEnter the Trim Length \n")
							sp = sb.Popen([prog,arg2,'-n','trim',trim_point,trim_length,'spectrogram'], shell=False,stdout=sb.PIPE, stderr=sb.PIPE)
							stg.spinning_cursor()
							show_image()
							print stg.color.FAIL + "Program Exited by User"
							exit()
					elif yn1=='n':
						sp = sb.Popen([prog,arg2,'-n','spectrogram'], shell=False,stdout=sb.PIPE, stderr=sb.PIPE)
						stg.spinning_cursor()
						show_image()
						print stg.color.FAIL + "Program Exited by User"
						exit()
					else :
						print("Please enter a vaild choice")
				continue			
		else:
			stg.io_error()
			exit()
	else:		
		stg.io_error()
		exit()


def soxy(arg2):
 
 if os.geteuid() == 0:
	try:
		launch(arg2)

	except OSError as e:
		if e.errno == os.errno.ENOENT:
			stg.prog_install([prog,arg2])
			launch(arg2)	
 else:
 	stg.root_exit()


#!/usr/bin/python

import subprocess as sb
import sys
import os

sys.path.append('..')
import stegall as stg


prog = 'steghide'

def launch(arg2):
	yn1 = 'y'
	while yn1 == 'y':
		print stg.color.OKBLUE	+  "Enter the Password to demystify the image" +stg.color.END
		Pass = raw_input()
		
		try:
			p = sb.Popen([prog,'extract','-sf',arg2,'-p',Pass,'-f'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
			output = p.communicate()[0]
			outlist = str(output).split()
			catter = outlist[4][1:-2] 
			try: 
				with open(catter,'r') as fl:
					print stg.color.OKBLUE + "=======================================\n"
					print stg.color.OKGREEN + fl.read() + stg.color.OKBLUE + "\n=======================================" + stg.color.END
				break
			except IOError:
					print stg.color.FAIL + "	 Wrong Password :( 		"  + stg.color.END
					while (yn1!='y' or yn1!='n'):
						yn1 = raw_input('Do you want to enter password once more (y/n)')
						if yn1=='y':
							break
						elif yn1=='n':
							scrk(arg2)
							exit
						else :
							print("Please enter a vaild choice")
						continue	

		except sb.CalledProcessError as e:
			print stg.color.FAIL + "Error Hit", e.output


def scrk(arg2):
	try:
		prog2 = 'stegcracker'
		p = sb.Popen([prog2,'--version'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
		yn2 = 'y'
		while yn2:
			while (yn2):
				yn2 = raw_input('Do you want to brute-force with stegcracker (y/n)')
				if yn2=='y':
						wordlist=raw_input('\nEnter the location of your wordlist\n')
						os.system(prog2 +' ' +arg2 +' '+ wordlist)
						exit()
				elif yn2=='n':
					print stg.color.FAIL
					exit("Program Exited")
				else :
					print("Please enter a vaild choice")
			continue
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			sb.call(["sudo","curl","https://raw.githubusercontent.com/Paradoxis/StegCracker/master/stegcracker", ">","/usr/local/bin/stegcracker"])
			sb.call(["sudo", "chmod", "+x","/usr/local/bin/stegcracker"])		
			sb.call([prog,arg2])	

def sh(arg2):

 dotLoc = arg2.find('.')
 ext = arg2[dotLoc+1::]	


 try:
	test = sb.Popen([prog,'extract','-sf',arg2,'-p','testpass'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = output.find('could not open the file')

 	if res==10:
		stg.io_error()
		exit()
		return

	elif ext in ['jpg','bmp','jpeg']:
  		launch(arg2)
  	else:
  		stg.io_error()
  		exit()

 except OSError as e:
	if e.errno == os.errno.ENOENT:
		prog_install(prog)

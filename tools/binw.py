#!/usr/bin/python

import subprocess as sb
import sys
import os
import magic
import zipfile

import stegall as stg

prog = 'binwalk'

def launch(arg2):
	test = sb.Popen([prog,arg2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = output.find('Cannot open file')
	if res==16:
		stg.io_error()
		exit()
		return
	else:
		test = sb.call([prog,'-e',arg2])
		print "Embedded Files :"
		folder = '_'+arg2+'.extracted'
		overwrite = '_'+arg2+'-0.extracted'
		if os.path.isdir(overwrite):
			os.system('mv '+overwrite+'/* '+folder+'/ && rm -rf '+overwrite)
		if os.path.isdir(folder):
			os.system('cd '+folder+'&&'+'file *')

		print "" ;stg.spinning_cursor(); print ""
		print "Contents have been saved to " + stg.color.OKYELLOW +folder+ stg.color.END + " in my directory :)\n"

		if os.path.isdir(folder):
		 for file in os.listdir(folder):
			path = folder+'/'+file
			chk_ext = magic.from_file(path, mime=True)
			if (chk_ext=='text/plain'):
				print stg.color.OKBLUE + "Reading txt's if present" + stg.color.END
				print "----------"+file+"----------";os.system('cat ' + path);print "\n---------------------------\n";
			elif (chk_ext=='application/zip'):
				zf = zipfile.ZipFile(path)
				try:
					zf.testzip()
				except RuntimeError as e:
					if 'encrypted' in str(e):
						print 'H0ly Sh1t !!, '+file+' is encrypted!'
						try:
							prog2 = 'fcrackzip'
							p = sb.Popen([prog2,'--version'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
							yn1 = 'y'
							while yn1:
								while (yn1):
									yn1 = raw_input('Do you want to crack this zip with fcrackzip (y/n)')
									if yn1=='y':
											wordlist=raw_input('\nEnter the location of your wordlist\n')
											os.system(prog2 + ' -u -D -p '+ wordlist +' ' + path)	
											exit()
									elif yn1=='n':
										print stg.color.FAIL
										exit("Program Exited")
									else :
										print("Please enter a vaild choice")
								continue
						except OSError as e:
							if e.errno == os.errno.ENOENT:
								stg.prog_install(prog2)

		else:
		 print "\nNo Embedded Files Found.."	



def bin(arg2):
	try :
		launch(arg2)
	except OSError as e:
		if e.errno == os.errno.ENOENT:
			stg.prog_install(prog)
			launch(arg2)


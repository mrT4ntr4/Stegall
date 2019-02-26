#!/usr/bin/python

import os
import sys
import time
import subprocess as sb
import threading
import signal

sys.path.append('tools/')

import steghide as sh
import exiftool as ef
import binw as bw
import sonic_visualiser as sv
import stegsolve as ss
import pngcheck as pc
import hexedit as he
import zsteg as zs
import strings as str
import wavest as wv
import audacity as au
import soxy as sx

class color:
    HEADER = '\033[7;49m'
    BLINK = '\x1b[6;5;48m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    OKYELLOW = '\033[1;33m'
    UNDERLINE = '\033[4m'

def version():
	print color.OKYELLOW  + "Stegall version 1.0" + color.END

def spinning_cursor():
	print "processing...\\",
	syms = ['\\', '|', '/', '-']
	bs = '\b'

	for _ in range(4):
		for sym in syms:
 			sys.stdout.write("\b%s" % sym)
			sys.stdout.flush()
			time.sleep(0.1)
	print "\n"		

def root_exit():
	print color.FAIL
	print "You need to have root privileges for this function.\nPlease try again, this time using 'sudo'"
	print color.END
	spinning_cursor()
	exit("\nProgram Exited")	


def help():
			print color.OKYELLOW
			print "###################################################" 
			print "#```````````````````````````````````(c) MrT4ntr4``#" 
			print "#`````  |^|  `````````````````````````````````````#" 
			print "#``````  \ \ |^|_```````````````__|^|^|   ````````#" 
			print "#```````  \ \|  _)/^^^^)^^^^|/^^  | | |   ````````#" 
			print "#`````_____) ) |_( (/ ( ( | ( ( | | | |   ````````#" 
			print "#``` (______/ \___)____)_|| |\_||_|_|_|   ````````#" 
			print "#```````````````````` (_____| `````````````v_1.0``#" 
			print "###################################################"

			print "\n\n"
			print  "Stegall version 1.0"
			print  "---------------------Automating the boring stego work for you"
			print  "\nthe first argument must be one of the following:"
			print  "-sug         for some advice on selection of tools"
			print  "-sh          use steghide with/without stegcracker for extracting embedded text from jpg/jpeg files"
			print  "-ef          use exiftool to extract metadata from image"
			print  "-bw          use binwalk to find hidden files in image, Option to use fcrackzip along with it"
			print  "-str         use the strings built-in utility to search for readable strings"
			print  "-zs          use zsteg to detect hidden data in png and bmp files."
			print  "-sv          to make use of sonic_visualiser for audio-stego "
			print  "-ss          make use of stegsolve to change RGB planes etc."
			print  "-pc          use pngcheck and pngcsum utility to check for IHDR errors and correct at the same time if any"
			print  "-he          use the powerful hexeditor 'hexcurse' XD"
			print  "-wv          use wavsteg for detecting LSB in wav audio files"
			print  "-au          make use of audacity to see hidden messages"
			print  "-sx          use Sound eXchange, Sox, the Swiss Army knife of audio manipulation"
			print  "--version    display version information"
 			print  "-h,--help    display this usage information"

 			print "\nthe second argument:"
 			print "<filename> with extension"
 			print "\nThe image file must reside in this directory only"
 			print "\nExample :: \n ./stegall.py -sh example.jpg"
 			print "Also, Run this script as R00t if you want to use a tool which is not installed "
			print color.END	

def arg_err():
	print color.FAIL
	print "****************************"
	print "Please Specify correct args\n Use help(-h) for more info"
	print "****************************"
	print color.END

def io_error():
	print color.FAIL + "Couldn't find your file\n 	OR	\nEither Format Unspecified or Unsupported !" + color.END	

def prog_install(prog):
	print color.FAIL + prog +" not installed!!" + color.END
	yn3 = raw_input("Do you want to install now (y/n)")
	if yn3=='y':
		if os.geteuid() == 0:
			os.system('sudo apt-get install '+prog)
		else:
			root_exit()
	elif yn3=='n':
		spinning_cursor()
		exit("\nProgram Exited")	

def suggest(arg2):
	test = sb.Popen(['ls',arg2], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT) 
	output = test.communicate()[0]
	res = output.find('cannot access')
	if res==4:
		io_error()
		exit()

	dotLoc = arg2.find('.')
	ext = arg2[dotLoc+1::]
	print "\nSuggested Tools for "+ext+ " extension :"
	print color.OKBLUE
	if ext in ['jpeg','jpg']:
		print "  steghide  ( -sh )\n  stegsolve  ( -ss )"
	elif ext in ['png','bmp']:
		print "  zsteg  ( -zs )\n  stegsolve  ( -ss )\n  pngcheck & pngcsum ( -pc )"	
	elif ext in ['mp3','m4a','wav','ogg','flac']:
		print "  sox  ( -sx )\n  audacity  ( -ad )\n  sonicVisualizer  ( -sv )"
	elif ext == 'wav':
		print "  wavsteg  ( -ws )"	
	print color.END

	print "Universal Tools : "
	print color.OKBLUE
	print "  binwalk  ( -bw )\n  strings  ( -str )\n  exiftool  ( -ef )\n  hexcurse ( -he )"
	print color.END		


def download(link,file_name):
    with open(file_name, "wb") as f:
        print "Downloading %s" % file_name
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

def install_dep(*deps):
    import importlib
    for pkg in deps:
		try:
			importlib.import_module(pkg, package=None)
		except ImportError:
			sb.call([sys.executable, "-m","pip", "install", pkg])
		finally:
			globals()[pkg] = importlib.import_module(pkg)

def dep_check():
	deps=('progressbar','requests')
	dep_thread = threading.Thread(target=install_dep, args=deps)
	dep_thread.start()
	while dep_thread.isAlive():
		print color.OKBLUE + "\nInstalling required libraries\r" + color.END
		spinning_cursor()
	print "\nAll Set !!\n"

def kb_interrupt_handler(signal, frame):
    print color.FAIL + "\nYou choosed to exit"
    sys.exit(0)



if __name__ == "__main__":

	signal.signal(signal.SIGINT, kb_interrupt_handler)
	kb = threading.Event()

	argc = len(sys.argv)
	arg_list = ['-h','--help','-sug','--version','-sh','-ef','-bw','-str','-ss','-sv','-pc','-he','-zs','-wv','-au','-sx']

	if argc==1 or argc>3:
		arg_err()
		exit()

	try:
		arg1 = sys.argv[1]

		if (argc == 2):
			if(arg1 == arg_list[0] or arg1 == arg_list[1]):
				help()
			elif(arg1 == arg_list[3]):
				version()
			else:
				arg_err()	
				exit()
		else :
			arg2 = sys.argv[2]


			if arg1 == arg_list[2]:
				suggest(arg2)
			elif arg1 == arg_list[4]:
				sh.sh(arg2)
			elif arg1 == arg_list[5]:   
				ef.ef(arg2)
			elif arg1 == arg_list[6]:
				bw.bin(arg2)	
			elif arg1 == arg_list[7]:
				str.strings(arg2)
			elif arg1 == arg_list[8]:
				ss.stsolve(arg2)
			elif arg1 == arg_list[9]:
				sv.sonic(arg2)
			elif arg1 == arg_list[10]:
				pc.pngch(arg2)
			elif arg1 == arg_list[11]:
				he.hedit(arg2)	
			elif arg1 == arg_list[12]:
				zs.zst(arg2)
			elif arg1 == arg_list[13]:
				wv.wave(arg2)
			elif arg1 == arg_list[14]:	
				au.auda(arg2)	
			elif arg1 == arg_list[15]:	
				sx.soxy(arg2)	

			else:
				arg_err()	
							
	except IndexError:
		arg_err()



	
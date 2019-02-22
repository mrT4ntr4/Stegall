# Stegall

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![version_1.0](https://img.shields.io/badge/version-1.0-blue.svg)](https://github.com/mrT4ntr4/Stegall)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:mrt4ntr4@gmail.com))


Automating the boring stego work for you..  
Stegall version_1.0  
Made with <3 by MrT4ntr4  

This script acts as an automation tool for Suggesting,Using as well as Installing the most popular steganography tools.   
It is made keeping CTF challenges in mind.  

## Tools Included

12 Tools and 3 sub-Tools

* Steghide
   * Stegcracker
* Exiftool
* Binwalk
   * Fcrackzip 
* Strings
* Zsteg
* Sonic Visualiser
* StegSolve
* pngcheck
   * pngcsum
* Hexcurse
* WavSteg
* Audacity
* SoX 

# Requirements

Python 2.7.*  

This is the X-Factor for this tool. XD
Stegall takes care of everything else...

## Usage

the first argument must be one of the following:
```
-sug         for some advice on selection of tools
-sh          use steghide with/without stegcracker for extracting embedded text from jpg/jpeg files
-ef          use exiftool to extract metadata from image
-bw          use binwalk to find hidden files in image, Option to use fcrackzip along with it
-str         use the strings built-in utility to search for readable strings
-zs          use zsteg to detect hidden data in png and bmp files.
-sv          to make use of sonic_visualiser for audio-stego 
-ss          make use of stegsolve to change RGB planes etc.
-pc          use pngcheck and pngcsum utility to check for IHDR errors and correct at the same time if any
-he          use the powerful hexeditor 'hexcurse' 
-wv          use wavsteg for detecting LSB in wav audio files
-au          make use of audacity to see hidden messages
-sx          use Sound eXchange, SoX, the Swiss Army knife of audio manipulation
--version    display version information
-h,--help    display this usage information
```
the second argument:
```
<filename> with extension
```

Example:
```
 ./stegall.py -sh example.jpg
```

## Note

The image file must reside in this directory only  
Also, Run this script as R00t if you want to use a tool which is not installed   

## Demo

![stegall-demo](demo.gif)

## Acknowledgements

Credit for all the tools stegall uses, go to their original authors.  

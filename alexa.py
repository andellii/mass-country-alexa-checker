#!/bin/python2.7
# contact Whatsapp: 085886343536
# 19 January 2020
# Sterben404

import os,sys,re,time
import urllib2
import socket
import bs4
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[96m'
purple = '\033[95m'
reset = '\033[0m'
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
pass

print(green+"  ___  __   _  _  __ _  ____  ____  _  _ ")
print(" / __)/  \ / )( \(  ( \(_  _)(  _ \( \/ )")
print("( (__(  O )) \/ (/    /  )(   )   / )  / ")
print(" \___)\__/ \____/\_)__) (__) (__\_)(__/  "+reset)
print(blue+"Mass Web Country Checker By Sterben404\n"+reset)

def error():
	try:
		sys.argv[1]
		open(sys.argv[1], 'r')
		socket.gethostbyname('www.google.com')
	except IndexError:
		print(blue+"[ * ]"+green+" Usage  :"+reset+" python (file.py) (listweb.txt)")
		print(blue+"[ * ]"+green+" Example:"+reset+" python country.py list.txt")
		exit()
	except IOError:
		print(red+"[ ! ]"+reset+" File Tidak Di Temukan")
		exit()
	except socket.gaierror:
		print(red+"[ ! ]"+reset+"Tidak Ada Koneksi Internet")
	pass
error()

def proc(url):
	url = url.replace('http://','').replace('http://www.','').replace('https://www.','').replace('https://','').replace('www.','')
	ip = socket.gethostbyname(url)
	alexa = bs4.BeautifulSoup(urllib2.urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url=http://'+url), "xml").find("REACH")['RANK']
	country = bs4.BeautifulSoup(urllib2.urlopen('http://data.alexa.com/data?cli=10&dat=snbamz&url=http://'+url), "xml").find("COUNTRY")['NAME']
	print(green+"\nWeb 	: "+url+reset+"\nIP 	: "+ip+"\nAlexa 	: "+alexa+"\nCountry : "+country+"\n")
	with open('result.txt', 'ab') as result:
		result.write(url+" --> "+ip+" --> "+alexa+" --> "+country+"\n")
		result.close()
ls = open(sys.argv[1], 'rb').read().splitlines()
t = ThreadPool(100)
t.map(proc, ls)
t.close()
t.join()

if __name__ == '__main__':
	print("Save File : result.txt")

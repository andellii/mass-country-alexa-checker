#!/bin/python2.7
# contact Whatsapp: 085886343536
# 19 January 2020
# Sterben404

import os,sys,re,time
import urllib2
import socket
import threading
import json

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[96m'
purple = '\033[95m'
reset = '\033[0m'
os.system('clear')
os.system('cls')

def write(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.0010)

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

def process(web):
	for file in web:
		ls = file.replace('http://','').replace('https://','').replace('/','')
		ip = socket.gethostbyname(ls)
		r_country = urllib2.urlopen('http://free.ipwhois.io/xml/%s' % ip)
		r_alexa = urllib2.urlopen('http://tools.mercenie.com/alexa-rank-checker/api/?format=json&urls=http://%s' % ls).read()
		parsing_json = json.loads(r_alexa)
		alexa = parsing_json['alexaranks']['first']['alexarank']['0']
		country = re.findall('(?<=<country>)(.*?)(?=<)',r_country.read())

		print("Website    : ")+green+ls+reset
		print("Alexa      : "+green+"{:,}".format(float(alexa)).replace('.0','')+reset)
		print("IP Address : "+green+"".join(ip)) + reset
		print("Country    : "+green+"".join(country)) + reset +'\n'

		with open('success.txt', 'ab') as live:
			live.write(ls+" | "+"".join(country)+" | "+"{:,}".format(float(alexa)).replace('.0','')+'\n')
			live.close()
	pass
	print("Hasil Di Simpan : "+green+"success.txt"+reset)
if __name__ == "__main__":
	print(green+"  ___  __   _  _  __ _  ____  ____  _  _ ")
	print(" / __)/  \ / )( \(  ( \(_  _)(  _ \( \/ )")
	print("( (__(  O )) \/ (/    /  )(   )   / )  / ")
	print(" \___)\__/ \____/\_)__) (__) (__\_)(__/  "+reset)
	write(blue+"Mass Web Country Checker By Sterben404\n"+reset)
	file = sys.argv[1]
	web = open(file, 'r').read().splitlines()
	t = threading.Thread(target=process, args=(web, ))
	t.start()

#!/usr/bin/python
import os

def parse(n):
	s = ""
	for line in n:      #for each line in file, make it readable
		if line == '\n':
			s+='next frame: \n'		#if no content, newline
		else:
			s += readable(line) + '\n'
	return s

def flip(n):
	s = n[2:] + n[:2]
	return str(int(s,16))

def flips(n):
	s = n[2:] + n[:2]
	return (int(s,16))

def readable(n):
	s = ''
	s += 'checksum:' + flip(n[:4]) + " "				#all of the specificied registrars of the object block (shifted down one because the sync is turned into a newline)
	s += 'sig:' + flip(n[4:8]) + " "
	s += '(' + flip(n[8:12]) + ',' + flip(n[12:16]) + ") "
	s += "width:" + flip(n[16:20]) + " "
	s += "height:" + flip(n[20:24]) + " "
	s += "oursum" + str(flips(n[4:8]) + flips(n[8:12]) + flips(n[12:16]) + flips(n[16:20]) + flips(n[20:24])) 
	return s

filename = raw_input("enter filename: ")		#writing to the file, should be called "readable.txt"
preParse = 'pixylog.pre'

f = open(filename)
data = f.read()
f.close()

print "replacing"

data2 = data.replace('55aa', '\n')				#replaces sync bit with newline

print "writing"
f2 = open(preParse, 'w+')
f2.write(data2)
f2.close()

f3 = open("pixylog.pre")
f4 = open("readable.txt", "w+")
bigS = parse(f3)								#makes it readable
f3.close()
f4.write(bigS)
f4.close()

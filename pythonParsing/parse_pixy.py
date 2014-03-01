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


def readable(n):
	s = ''
	s += 'checksum:' + n[:2] + " "				#all of the specificied registrars of the object block (shifted down one because the sync is turned into a newline)
	s += 'sig:' + n[2:4] + " "
	s += '(' + n[4:6] + ',' + n[6:8] + ") "
	s += "width:" + n[8:10] + " "
	s += "height" + n[10:12] + " "
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
os.remove(preParse)




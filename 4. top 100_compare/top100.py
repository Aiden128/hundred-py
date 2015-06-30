# coding=UTF-8
#! /usr/bin/python

f = open("/Users/klein/Desktop/top100_raw", "r+")
com = open("/Users/klein/Desktop/compare", "r+")

inAnotinT = open("/Users/klein/Desktop/inAnotinT.csv", "w+")
inTnotinA = open("/Users/klein/Desktop/inTnotinA.csv", "w+")

s = f.read().replace("\n","").lower().split('",')
s_com = com.read().replace("\n","").lower().split(',')

s_lst = list()

i = 0
while i<300:
	#d = '{},{},{}\n'.format(s[i].replace('"',''), s[i+1].replace('"',''), s[i+2].replace('"',''))
	d = s[i+1].replace('"','')
	# in sour but not in com
	s_lst.append(d)
	if d not in s_com:
		e = '{},{},{}\n'.format(s[i].replace('"',''), s[i+1].replace('"',''), s[i+2].replace('"',''))
		inAnotinT.write(e)
	i+=3


for d in s_com:
	if d not in s_lst:
		inTnotinA.write(d+"\n")
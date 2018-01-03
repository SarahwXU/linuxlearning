#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

# all graduated students
class Graduates:
	dnumCount = 0 # count the number of doctors
	mnumCount = 0 # count the number of masters
	dcheckCount = 0 # count the number of checked d
	mcheckCount = 0 # count the number of checked m
	
	def __init__(self, name='', address='', cal=''):
		self.name = name # name
		self.address = address # communicating address
		self.cal = cal # two class, 1 for doctors, 2 for masters
		self.check_flag = '0' # indicator of whether checked
		if int(cal) == 1:
			Graduates.dnumCount += 1
			self.cal_name = 'Doctor'
		elif int(cal) == 2:
			Graduates.mnumCount += 1
			self.cal_name = 'Master'
		else:
			pass		

	def displayCount(self):
		print('Total doctoral graduates are ', Graduates.dnumCount)
		print('Total master graduates are ', Graduates.mnumCount)

	def displayGraduates(self):
		print ('Classes : ', self.cal_name, 'Name : ', self.name, 'Address : ', self.address) 

	def dispalyState(self):
		if int(self.check_flag) == 0:
			print(self.name + ' is not checked')
		elif int(self.check_flag) == 1:
			print(self.name + ' is checked')



with open('studenttable.txt', 'r') as stu:
	lines = stu.readlines()
i = 0
for line in lines:
	stu_info = re.split(' ',line)
# questions remianed
# bug here
	Graduates(stu_info[1], stu_info[2], stu_info[3])
	i+=1

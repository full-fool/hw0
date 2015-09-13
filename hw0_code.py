#coding=utf-8
# HW0, INTRODUCTION TO DATABASES
# Yiqing Cui, yc3121
# Sep 13, 2015


import os

filePath = './'
fileName = 'iowa-liquor-sample.csv'


matchedNum = 0
for line in open(os.path.join(filePath, fileName)):
	# change each line into lower case
	if 'single malt scotch' in line.lower():
		matchedNum += 1
print matchedNum
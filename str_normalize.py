#! /usr/bin/python3

import string
import re	#future#

def make_alphanumeric( strname ):
	fname = strname

	for c in [' ', '(', ')', '&', '#', '	', '%', '{', '}', '@', '?', '*', ',', '\'' , '^']:
		fname1 = fname.replace(c, '_')
		fname  = fname1
		# print(f"{c} --> {fname}")

	return fname 

def fold_two_underscores( strname ):
	return strname.replace('__', '_')

def fold_multiple_underscores( strname ):
	while ('__' in strname):
		strname = fold_two_underscores(strname)
	return strname

#
# TO DO -
#	put in the ifdef __main__ thing 
#	also the __init__ thing
#	turn it into a class
#	change fold_xxx to lambda
# 

strings_list = [
		'abcd &%99_  efg @hij ( kl.fifi'  ,
		'abcd &%99_  efg @#hij } kl.fifi'
	]

for fname in strings_list:
	print(f"file name is:   {fname}")
	fname = make_alphanumeric (fname)
	print("result  --> ", fold_multiple_underscores(fname))


'''
Created on 29-Jan-2017

@author: abhay
'''
import os

def generate_key_value_pair(filePath,sep='='):
	dict_of_ip = {}
	with open(filePath,"rt") as f:
		for line in f:
			stripped_line = line.strip()
			if stripped_line and stripped_line[0].isdigit():
				print "Found Ip: {0}".format(stripped_line.split(sep)[0])
				ip = stripped_line
				dict_of_ip[ip] = {} 
			elif stripped_line and stripped_line[0].isupper():
				print "Found attributes: {0}".format(stripped_line)
				key_value = stripped_line.split(sep)
				key  = key_value[0].strip()
				value =key_value[1].strip()
				dict_of_ip[ip][key] = value
	return dict_of_ip


if __name__ == '__main__':
	generate_key_value_pair('slaves.properties')









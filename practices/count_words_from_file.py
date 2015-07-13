'''
Created on 2015-07-05

@author: abner0908
'''
import re
from collections import Counter

def get_except_list():
	result = []
	with open('except list.txt', 'r') as f:
			for line in f:
				result.extend(line.lower().split())
	return result

counter = Counter();
with open('Animal Farm.txt', 'r') as f:
		for line in f:
			words = re.findall('[\w]+', line.lower())
			accept_words = list(set(words) - set(get_except_list()))
			counter.update(accept_words)
			
for item in counter.most_common(30): 
			print("{0}\t{1}".format(*item))
import re

def test_patterns(text, patterns = []):
	
	for pattern, desc in patterns:
		print("Pattern: {0}  ({1})\n".format(pattern, desc))
		print("  {0}".format(text))
		
		for match in re.finditer(pattern, text):
			start = match.start()
			end = match.end()
			stars = '*' * start
			print("  {0}{1}".format(stars, text[start:end]))
		print	
	return

if __name__ == '__main__':
	test_patterns('abbaaabbbbaaaaa',
					[	('ab*', 	'a followed by zero or more b'), 
						('ab+', 	'a followed by one or more b'), 
						('ab?', 	'a followed by zero or one b'),
						('ab{3}', 	'a followed by three b'), 
						('ab{2,3}', 'a followed by two to three b')
					])
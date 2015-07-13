import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

m = re.match(pattern, text)
print("Match: {0}", m)

s = re.search(pattern, text)
print("Search: {0}", s)
'''
Created on 2015-05-21

@author: abner0908
'''

f = open('words.txt', mode= 'r',  encoding = 'utf8')

# for line in f:
#     for words in line.split():
#         print(words)

words = []
for word in f.read():
    words.append(word)
     
words.append("!!")
  
for word in words:
    print(word, end='')    
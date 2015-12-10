# coding=UTF-8

import sys
file = open(sys.argv[1], 'r')
content = file.read()
print sys.argv[1] + '\'s content is "' + content + '"'
file.close()
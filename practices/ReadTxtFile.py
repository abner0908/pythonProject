'''
Created on 2015-09-19

@author: abner0908
'''
           
from os import listdir
from os.path import isfile, join

def findContent(txt, keyword):
    content = ""
    for line in txt:
        lower = line.lower()
        found = lower.find(keyword.lower())
        if found >= 0:
            start = found + len(keyword)
            content = line[start:].strip()
            break
        
    return content

def showBookInfo(txt, keywords, count):
    import string 
    
    result = ""
    
    for keyword in keywords:
        content = findContent(txt, keyword)
    
        if len(content) > 0:
            result += "\n" + string.capwords(keyword) + " " + content
            
    if len(result) > 0:
        result =  "\nNo." + str(count) + result
        
    print result

folderPath = "D:\\Dropbox\\eBook\\novels"

onlyfiles = [ f for f in listdir(folderPath) if isfile(join(folderPath,f)) ]
for f in onlyfiles:
    print join(folderPath, f)
    


attributes = []
attributes.append("title:")
attributes.append("author:")
attributes.append("release date:")
attributes.append("language:")

count = 0
for fileName in onlyfiles:
    filePath = join(folderPath, fileName)
    txt = open(filePath)
    count = count + 1
    showBookInfo(txt, attributes, count)    
    
print "Total:", len(onlyfiles)        
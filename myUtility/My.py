'''
Created on 2015-9-20

@author: abner0908
'''
from genericpath import isfile

class Setting(object):
    '''
    To get my settings.
    '''


    def __init__(self, name):
        self.name = name
        
    def getValue(self, attribute):
        value = ""
        settingFile = "D:\\Dropbox\\Settings\\PySettings.txt"
        if isfile(settingFile) == False:
            print "No such file exist!!"
            return ""
        f = open(settingFile)
        accessible = False
        for line in f:
            name = ""
            line = line.strip()
            if len(line) == 0 or line[0] == "#":
                continue
            if line[0] == "[" and line[-1] == "]":
                name = line[1:-1].strip()
                if name == self.name:
                    accessible = True
                else:
                    accessible = False
            
            if line.find(attribute) >= 0 and accessible:
                start = line.find("=") + len("=")
                value = line[start:].strip()
                   
        return value
    
if __name__ == '__main__':
    dbSetting = Setting("MySQL")
    print dbSetting.getValue("hostname")
    
    userSetting = Setting("User")
    print userSetting.getValue("name")
    
    
        
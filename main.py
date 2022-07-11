from ntpath import join
import os
import shutil
import time

class Main:
    def __init__(self, days, path, seconds):
        self.days = days
        self.path = path
        self.seconds = seconds
    def checkIfPathExists(self):
        return os.path.exists(self.path)
    def getItemAge(self):
        return os.stat(self.path).st_ctime
    def removeFolder(self, folder):
        shutil.rmtree(folder)
    def removeFile(self, file):
        os.remove(file)

def foo():
    days = 30
    path = ""
    seconds = time.time() - (days * 24 * 60 * 60)
    handler = Main(days, path, seconds)
    path_exists = handler.checkIfPathExists()
    
    if path_exists == True:
        for item, folders, files in os.walk(path):
            for file in files:
                joined_file = os.path.join(item, file)
                age = handler.getItemAge(joined_file)

                if seconds >= age:
                    handler.removeFile(joined_file)

            for folder in folders:
                joined_file = os.path.join(item, file)
                age = handler.getItemAge(joined_file)

                if seconds >= age:
                    handler.removeFolder(joined_file)
    else:
        print(path, " Does not exist")
foo()
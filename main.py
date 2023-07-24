import os
if (os.path.exists("file.txt") == False):
    f = open("file", "w")
else:
    print("File Exists")  
    

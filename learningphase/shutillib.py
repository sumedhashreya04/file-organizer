#FOR PRACTICE
import shutil
import os
os.chdir("Users/sumedhashreya/Desktop/Coding/Python")
def ignorereturnlist(directory,files):
  return [f for f in files if f=="example.txt"]
shutil.copytree("deleteit","deletit2",ignore=ignorereturnlist)  
""" 
"""
os.chdir("Users/sumedhashreya/Desktop/Coding/Python")
print(os.getcwd())
os.mkdir("deleteit")
path=os.path.abspath("deleteit")
os.chdir(path)
with open("example.txt",'w') as f:
    f.write("Hello World")
shutil.copy("example.txt","example2.txt")
'''
'''
os.chdir("Users/sumedhashreya/Desktop/Coding/Python")
shutil.move("deleteit2","deletit2")

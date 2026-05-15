import os
os.chdir("/Users/sumedhashreya/Desktop/testFile")
list=os.listdir()
print(list)
list2=[]
list3=[]
large="No files"
size=0
for i in list:
    ext=os.path.splitext(i)[1]
    if size<os.path.getsize(i):
        large=i
        size=os.path.getsize(i)
    if(ext==".jpg"):
        list2.insert(len(list2),i)
    elif(ext==".pdf"):
        list3.insert(len(list3),i)
print("Images",list2,len(list2))
print("Total files",len(list))
print("PDF:",list3,len(list3))
print("Largest File",large," : ",size)

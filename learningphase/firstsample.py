import shutil
import os
folder=input("Enter address of folder")
os.chdir(folder)
list=os.listdir()
#GroupingLists
# listtxt=[]
# listimg=[]
# listaud=[]
# listvid=[]
# listoth=[]
#Scanning
# for files in list:
#     if files.endswith(".txt") or files.endswith(".docx") or files.endswith(".doc") or files.endswith(".pdf") or files.endswith(".rtf") :
#         listtxt.insert(len(listtxt),files)
#     elif files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".png") or files.endswith(".gif") :
#         listimg.insert(len(listimg),files)
#     elif files.endswith(".mp3") or files.endswith(".wav"):
#         listaud.insert(len(listaud),files)
#     elif files.endswith(".mp4") or files.endswith(".mkv"):
#         listvid.insert(len(listvid),files)
#     else:
#         listoth.insert(len(listoth),files)
#CreateFiles
os.mkdir("Images")
os.mkdir("Texts")
os.mkdir("Audio")
os.mkdir("Video")
os.mkdir("Others")
#MovesFiles
for files in list:
    if files.endswith(".txt") or files.endswith(".docx") or files.endswith(".doc") or files.endswith(".pdf") or files.endswith(".rtf") :
        shutil.move(files,"Texts")
    elif files.endswith(".jpg") or files.endswith(".jpeg") or files.endswith(".png") or files.endswith(".gif") :
        shutil.move(files,"Images")
    elif files.endswith(".mp3") or files.endswith(".wav"):
        shutil.move(files,"Audio")
    elif files.endswith(".mp4") or files.endswith(".mkv"):
        shutil.move(files,"Video")
    else:
        shutil.move(files,"Others")

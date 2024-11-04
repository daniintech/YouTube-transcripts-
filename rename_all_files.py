import os

#for all files in a specified folder (path1), adds specified name at the very beginning of file
#this was used for creating a better overview of the transcripts in terms of which youtuber they belonged to
#useful for working in AntConc
path1 = ''
files = os.listdir(path1)

#changes working directory to path specified in path1
os.chdir(path= path1)


#name that should be added at the beginning of the file (name of youtuber the transcripts belong to)
youtuber_name = ""

for file in files:
    os.rename(file, youtuber_name + file)
    

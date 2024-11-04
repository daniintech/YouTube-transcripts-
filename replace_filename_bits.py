import os

#for all files in a specified folder (path1), adds specified name at the very beginning of file
#this was used for creating a better overview of the transcripts in terms of which youtuber they belonged to
#useful for working in AntConc
path1 = 'C:/Users/jawie/Documents/Uni/Bachelor/Transcript_py/mitNameVorne_Incels_FinalCorpus/new_Brutal'
files = os.listdir(path1)

#changes working directory to path specified in path1
os.chdir(path= path1)

for file in files:
    new_name = file.replace("It’s ", "")
    os.rename(file, new_name)   


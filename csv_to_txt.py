import pandas as pd
import os

#converts csv files into txt files using only the transcript data (metadata is discarded)
#path from which the csv file(s) should be used. txt files will be saved in same path
path1 = 'C:/Users/jawie/Documents/Uni/Bachelor/R_stylo/csv_to_txt_einzelne_Youtuber/whatever_one_transcript_per_youtuber'
files = os.listdir(path1)

for file in files:
    if file.endswith('.csv'):
        data = pd.read_csv(path1 + '/' + file )


        new_file_name = file.replace("csv", "txt")
        df = pd.DataFrame(data['transcript'])
        df.to_csv( path1 + '/' + new_file_name, sep='\t', index=False)
    else:
        continue


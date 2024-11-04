YouTube Transcript Corpus Builder

This repository contains Python scripts designed to retrieve YouTube transcripts and assist in the preprocessing of the corpus files for a bachelor's thesis project. 
The preprocessing steps can be useful when using AntConc and the R_stylo package for a corpus or stylometric analysis of YouTube trascripts.

Repository Contents

    general.py: A script to retrieve all available YouTube transcripts from a specified channel name and save them as individual CSV files. 
                Each CSV file includes metadata such as publish date and video title, but excludes timestamps from the transcript.

    combine_csv_original.py: A utility to combine all CSV files from a specified folder into a single CSV file.

    csv_to_txt.py: This script converts CSV files into TXT files, retaining only the transcript data and discarding metadata, useful when working with R_stylo.

    rename_all_files.py: A script that prefixes a specified name to all files in a given folder. This was particularly useful for organizing transcripts
                         by YouTuber, facilitating easier analysis in AntConc.

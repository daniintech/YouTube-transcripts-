import csv
import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi as yta
from pathlib import Path 
from pytube import extract, YouTube 





#extracts id from a single url
def extract_video_id(url): 
    id=extract.video_id(url)
    return id 

#after retrieving the transcript from a youtube video, returns transcriptdata without timestamps etc.
def only_print_plain_transcript(id):
    data = yta.get_transcript(id)
    plain_text_transcript = ''
    for dicts in data:
        plain_text_transcript = plain_text_transcript + ' ' + dicts["text"] 
    #print(plain_text_transcript)
    return plain_text_transcript



#creates .csv file and writes header with videotitle, channelname, seconds, publishdate, transcript
def create_csv(id):
    # extract id from url
    #videoid = extract_video_id(url)
    #store transcript of video in variable transcriptdata
    transcriptdata = only_print_plain_transcript(id)
    #create YouTube object for retrieving metadata
    yt = YouTube('https://www.youtube.com/watch?v=' + id ) 
    title = yt.title
    author = yt.author
    videolength = yt.length
    publishdate = yt.publish_date

    #The Path may be named after the channelname the video was published on
    outpath = Path( author + "/" + id + ".csv")
    outpath.parent.mkdir(exist_ok=True)


    with outpath.open('w', newline="", encoding = "utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, ["id", "videotitle", "channelname", "videolength", "publishdate", "transcript"], dialect= 'excel')
        writer.writeheader()
        new_row = {"id": id, "videotitle": title, "channelname": author, "videolength": videolength, "publishdate": publishdate , "transcript": transcriptdata}
        writer.writerow(new_row)



# the following code creates csv-files for all available transcripts from the youtuber specified in youtube_channel_name
youtube_channel_name = ""
video_ids = scrapetube.get_channel(channel_username= youtube_channel_name)


for id in video_ids:
    try:
        create_csv(id.get('videoId'))
        print( 'creating transcript for ' + id.get('videoId'))
    except:
        print('error with ' + id.get('videoId'))
        continue





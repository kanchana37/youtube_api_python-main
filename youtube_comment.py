from youtube_comment_scraper_python import *
import pandas as pd
import time

url=input("enter the video url =")
file=input("enter the output file name =")

youtube.open(url)

fullcomments=[]
for i in range(0,1):

    result=youtube.video_comments()
    data=result['body']
    fullcomments.extend(data)

df = pd.DataFrame(fullcomments)
print(df)
time.sleep(5)
df.to_csv(file)
# -*- coding: utf-8 -*-
"""
Created on Fri May 30 13:55:59 2025

@author: Rodrigo
"""

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd


load_dotenv()
key = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey = key)
request_id = youtube.search().list(
    part = "snippet",
    q = "ClaudiaSheinbaumP",
    type = "channel",
    maxResults = 1)

response_id = request_id.execute()

sheimbaum_id = response_id["items"][0]["id"]["channelId"]

request_uploads = youtube.search().list(
    part='snippet',
    channelId=sheimbaum_id,
    maxResults=10,
    order='date',
    type='video'
)

result_uploads = request_uploads.execute()

df = pd.DataFrame(columns = ['comment_id', 'text', 'video_id', 'url'])

for item in result_uploads['items']:

    url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
    
    video_id = item["id"]["videoId"]
    
    request_comments = youtube.commentThreads().list(
    
        part='snippet',
    
        videoId='_4xyDnDgSV4',
    
        maxResults=100,
    
        textFormat='plainText'
    )
    response_comments = request_comments.execute()

    for item in response_comments["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comment_id = response_comments["items"][0]["snippet"]["topLevelComment"]["id"]
        df.loc[len(df)] = [comment_id, comment, video_id, url]
        
data_path = os.path.abspath(os.path.join(os.pardir, 'data'))
df.to_csv(os.path.join(data_path, "data.csv"))
    

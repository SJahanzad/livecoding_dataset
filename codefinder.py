from youtube_transcript_api import YouTubeTranscriptApi
import json
import os
from bs4 import BeautifulSoup
import re
import requests
from tqdm import tqdm

playlists = [
    'neetcode', 
    # 'nickwhite',
]

for playlist in playlists:
    # create a directory for each playlist if it doesn't exist
    # try:
    #     os.mkdir(playlist)
    # except FileExistsError:
    #     pass

    with open(f'{playlist}_video_info.json') as f:
        video_info = json.load(f)
    for video in tqdm(video_info):
        video_id = video['video_id']
        soup = BeautifulSoup(requests.get(f'https://www.youtube.com/watch?v={video_id}').content, 'html.parser')
        pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
        caption = pattern.findall(str(soup))[0].replace('\\n','\n')
        # print(caption)
        problem_link = re.findall(r'(https://neetcode.io/problems.*)', caption)[0]
        video['problem_link'] = problem_link
    with open(f'{playlist}_video_info.json','w') as f:
        json.dump(video_info,f,indent=4)
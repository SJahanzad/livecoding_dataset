import re
import json
from bs4 import BeautifulSoup
import requests

def get_video_info(video):
    video_id = video['playlistVideoRenderer']['videoId']
    title = video['playlistVideoRenderer']['title']['runs'][0]['text']
    length = video['playlistVideoRenderer']['lengthSeconds']
    return {
        'video_id': video_id,
        'title': title,
        'length': length,
    }

def get_playlist_videos(playlist_id):
    url = f'https://www.youtube.com/playlist?list={playlist_id}'
    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
    data = json.loads(data)
    videos = (
        data['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]
            ['tabRenderer']['content']['sectionListRenderer']['contents'][0]
            ['itemSectionRenderer']['contents'][0]
            ['playlistVideoListRenderer']['contents']
    )
    # print(videos[0]['playlistVideoRenderer'].keys())
    return videos

playlists = {
    'neetcode': 'PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf',
    'nickwhite': 'PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-',
}

for name, playlist_id in playlists.items():
    videos = get_playlist_videos(playlist_id)
    print(len(videos))
    video_info = []
    for video in videos:
        if 'playlistVideoRenderer' not in video.keys():
            continue
        video_info.append(get_video_info(video))
    with open(f'{name}_video_info.json','w') as f:
        json.dump(video_info,f,indent=4)

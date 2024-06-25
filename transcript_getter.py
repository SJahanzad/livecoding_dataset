from youtube_transcript_api import YouTubeTranscriptApi
import json
import os

playlists = ['neetcode', 'nickwhite']

for playlist in playlists:
    # create a directory for each playlist if it doesn't exist
    try:
        os.mkdir(playlist)
    except FileExistsError:
        pass

    with open(f'{playlist}_video_info.json') as f:
        video_info = json.load(f)
    for video in video_info:
        video_id = video['video_id']
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            with open(f'{playlist}/{video_id}_transcript.json','w') as f:
                json.dump(transcript,f,indent=4)
        except Exception as e:
            pass

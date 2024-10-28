from youtube_transcript_api import YouTubeTranscriptApi
import json
import os
from bs4 import BeautifulSoup
import re
import requests
from tqdm import tqdm
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By

playlists = [
    'neetcode', 
    # 'nickwhite',
]

# c_service = webdriver.FirefoxService(executable_path='./geckodriver1')
# driver = webdriver.Firefox(service=c_service)  

for playlist in playlists:
    # create a directory for each playlist if it doesn't exist
    dirpath = os.path.join('codes', playlist, 'images')
    try:
        os.mkdir(dirpath)
    except FileExistsError:
        pass

    with open(f'{playlist}_video_info.json') as f:
        video_info = json.load(f)
    for video in tqdm(video_info):
        video_id = video['video_id']
        video_len = int(video['length'])
        desired_position = video_len - 3
        url = f'https://www.youtube.com/watch?v={video_id}'
        mins = int(desired_position // 60)
        secs = int(desired_position % 60)
        if secs == 59:
            secs -= 1
        # print(f'./yt-dlp --download-sections "*{mins}:{secs}-{mins}:{secs + 1}" -o "{dirpath}/{video_id}.mp4" "{url}"')
        os.system(f'./yt-dlp-m --download-sections "*{mins}:{secs}-{mins}:{secs + 1}" -o "{dirpath}/{video_id}.mp4" "{url}"')
        # print(f'ffmpeg -i {dirpath}/{video_id}.mp4* -vf "select=eq(n\,34)" -vframes 1 {dirpath}/{video_id}.png -y')
        os.system(f'ffmpeg -i {dirpath}/{video_id}.mp4* -vf "select=eq(n\,34)" -vframes 1 {dirpath}/{video_id}.png -y')
        # os.system(f'rm {dirpath}/{video_id}.mp4*')

        # driver.get(url)
        # driver.implicitly_wait(10)
        # driver.execute_script(f'document.getElementsByTagName("video")[0].currentTime = {video_len - 20}')
        # driver.get_screenshot_as_file(f'{dirpath}/{video_id}.png') 
        # sucess = False  
        # while not sucess:
        #     try:
        #         driver.find_element(By.XPATH, "//span[text()='Solution']").click()
        #         sucess = True
        #     except:
        #         pass
        # sucess = False
        # while not sucess:
        #     try:
        #         code = driver.find_element(By.XPATH, "//app-code").text
        #         sucess = True
        #     except:
        #         pass
        # with open(f'{dirpath}/{video_id}_code.py','w') as f:
        #     f.write(code)

# driver.quit()
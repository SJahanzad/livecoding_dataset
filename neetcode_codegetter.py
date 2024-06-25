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

c_service = webdriver.FirefoxService(executable_path='./geckodriver1')
driver = webdriver.Firefox(service=c_service)  

for playlist in playlists:
    # create a directory for each playlist if it doesn't exist
    dirpath = os.path.join('codes', playlist)
    try:
        os.mkdir(dirpath)
    except FileExistsError:
        pass

    with open(f'{playlist}_video_info.json') as f:
        video_info = json.load(f)
    for video in tqdm(video_info):
        video_id = video['video_id']
        url = video['problem_link']
        driver.get(url)
        sucess = False  
        while not sucess:
            try:
                driver.find_element(By.XPATH, "//span[text()='Solution']").click()
                sucess = True
            except:
                pass
        sucess = False
        while not sucess:
            try:
                code = driver.find_element(By.XPATH, "//app-code").text
                sucess = True
            except:
                pass
        with open(f'{dirpath}/{video_id}_code.py','w') as f:
            f.write(code)

driver.quit()
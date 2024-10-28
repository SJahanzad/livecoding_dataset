# Livecoding dataset

This dataset contains solutions for Leetcode problems from YouTube channels [Nick White](https://www.youtube.com/c/NickWhite) and [NeetCode](https://www.youtube.com/@NeetCode).

To extract the data, we use the Leetcode playlists the channels provide and take the following steps.

- `scraper.py`: Extract the list of videos in the playlist, along with their useful metadata, using [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/).
- `youtube_codegetter.py`: For each video, download one second from the final few seconds of it using [yt-dlp](https://github.com/yt-dlp/yt-dlp). Then take one single frame from it using [ffmpeg](https://www.ffmpeg.org/). 
- In the previous step we assume the last few seconds of the video contain the final solution, which is usually true but sometimes is not the case. So we have to check if every screenshot "looks fine".
- `ask_gpt_for_codes.py`: For each image, we ask ChatGPT-4o to extract the code for the `Solution` class in the image.
- `convert_gpt_responses.py`: Extract the codes from the ChatGPT responses.
- `transcript_getter.py`: Get the transcripts for the videos using the [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/).
- `ask_gpt_for_alignments.py`: For each code-transcript pair, ask ChatGPT-4o to align the code with the transcript.
- `convert_alignment_gpt_responses.py`: Same as before, extract the alignments from the ChatGPT responses.
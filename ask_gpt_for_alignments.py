import base64
import requests
import os
from tqdm import tqdm
import json

# OpenAI API Key
api_key = "API_KEY"

CATEGORIES = ['nickwhite', 'neetcode']
CODE_EXTENSIONS = {'nickwhite': '.java', 'neetcode': '.py'}

category_name = CATEGORIES[1]
code_extension = CODE_EXTENSIONS[category_name]
codes_prefix_path = os.path.join('./codes', category_name)
all_codes = os.listdir(codes_prefix_path)

transcripts_prefix_path = os.path.join('./transcripts', category_name)
all_transcripts = os.listdir(transcripts_prefix_path)

transcripts_youtube_ids = [transcript.split('_transcript')[0] for transcript in all_transcripts]
code_youtube_ids = [code.split('_code')[0] for code in all_codes]

youtube_ids = list(set(transcripts_youtube_ids).intersection(set(code_youtube_ids)))

print(len(transcripts_youtube_ids), len(code_youtube_ids), len(youtube_ids))

response_prefix_path = os.path.join('./alignments/responses', category_name)
if not os.path.exists(response_prefix_path):
    os.makedirs(response_prefix_path)
existing_responses = os.listdir(response_prefix_path)


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

for youtube_id in tqdm(youtube_ids):
    if youtube_id + '.json' in existing_responses:
        continue

    code_path = os.path.join(codes_prefix_path, youtube_id + '_code' + code_extension)
    with open(code_path) as f:
        code = f.read()

    transcript_path = os.path.join(transcripts_prefix_path, youtube_id + '_transcript.json')
    with open(transcript_path) as f:
        transcript = json.load(f)
    
    # message_header = "We have a video where a coding problem is discussed and solved. The following are the transcript to the video and the final code of the solution. Can you please align the code with the transcript? In other words, add a key named \"code\" to each entry in the json file where the value would contain the lines of code connected to the text of that entry. If no line of code is related to that entry, do not include it in the answer."
    message_header = "We have a video where a coding problem is discussed and solved. The following are the transcript to the video and the final code of the solution. Can you please align the code with the transcript? In other words, add a key named \"code\" to each entry in the json file where the value would contain the lines of code connected to the text of that entry. Please just include the \"text\" and \"code\" keys. If no line of code is related to that entry, do not include it in the answer. In other words, do not include any entry in the json file where the \"code\" key is an empty list."
    # message = 'We have a video where a coding problem is discussed and solved. The following are the transcript to the video and the final code of the solution. Can you please align the code with the transcript? In other words, for each entry in the transcript, include an item with a "key" and a "value" where the "key" would contain the integer index of the item in the transcript and the "value" would contain the integer indices of the lines of code connected to the text of that entry. If no line of code is related to that entry, do not include it in the answer. Please just reply with the resulting json.'
    message_header = '''We have a video where an algorithmic problem is solved. The following are the transcript of the video and the final solution to the problem. Can you please align the transcript with the code, and include your confidence score for each of the items?

In other words, for each entry in the transcript, add the related line of code and its corresponding alignment confidence score.'''

    result = []
    for i in range(0, len(transcript), 200):
        partial_transcript = json.dumps(transcript[i:i+500])
        message = message_header + f"\n\nTranscript:\n```json\n{partial_transcript}\n```\n\nCode:\n```{code_extension[1:]}\n{code}\n```"

        payload = {
            "model": "gpt-4o",
            "messages": [
            {
                "role": "user",
                "content": [
                {
                    "type": "text",
                    "text": message
                }
                ]
            }
            ],
            "max_tokens": 4096
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_json = json.loads(response.text)
        result.append(response_json)

    response_path = os.path.join(response_prefix_path, youtube_id + '.json')
    with open(response_path, 'w') as f:
        json.dump(result, f, indent=4)

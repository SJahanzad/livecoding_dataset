import base64
import requests
import os
from tqdm import tqdm
import json

# OpenAI API Key
api_key = "API_KEY"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

channels = ['nickwhite', 'neetcode']
channel = channels[1]

prefix_path = f'./codes/{channel}/images/'
all_images = os.listdir(prefix_path)

response_prefix_path = f'./codes/{channel}/gpt_responses/'
if not os.path.exists(response_prefix_path):
    os.makedirs(response_prefix_path)
existing_responses = os.listdir(response_prefix_path)


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

for image in tqdm(all_images):
    if image[:-4] + '.json' in existing_responses:
        with open(response_prefix_path + image[:-4] + '.json') as f:
            response_json = json.load(f)
        if 'choices' in response_json:
            continue
    if not image.endswith('.png'):
        continue
    image_path = prefix_path + image

    base64_image = encode_image(image_path)

    payload = {
        "model": "gpt-4o",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "Can you give me the code for the class `Solution` that is seen in this image?"
            },
            {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/png;base64,{base64_image}"
                }
            }
            ]
        }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    with open(response_prefix_path + image[:-4] + '.json', 'w') as f:
        f.write(response.text)

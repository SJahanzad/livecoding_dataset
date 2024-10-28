import json
import os
import re

CHOSEN_INDEX = 1

channels = ['nickwhite', 'neetcode']
channel = channels[CHOSEN_INDEX]

suffixes = ['java', 'py']
suffix = suffixes[CHOSEN_INDEX]

prefix_path = f'./codes/{channel}/gpt_responses/'
all_responses = os.listdir(prefix_path)

result_prefix_path = f'./codes/{channel}/final_code/'
if not os.path.exists(result_prefix_path):
    os.makedirs(result_prefix_path)

for response in all_responses:
    with open(prefix_path + response) as f:
        try:
            response_json = json.load(f)
        except:
            print("Failed to load", response)
            continue
    if 'choices' not in response_json:
        continue
    result = response_json['choices'][0]['message']['content']
    code_lines = result.split('```')[1].split('\n')
    if not code_lines[0].strip().startswith('class'):
        code_lines = code_lines[1:]
    code = '\n'.join(code_lines)
    with open(result_prefix_path + response[:-5] + '_code' + '.' + suffix, 'w') as f:
        f.write(code)
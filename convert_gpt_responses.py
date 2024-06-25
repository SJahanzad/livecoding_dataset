import json
import os
import re

prefix_path = './codes/nickwhite/gpt_responses/'
all_responses = os.listdir(prefix_path)

result_prefix_path = './codes/nickwhite/final_code/'
if not os.path.exists(result_prefix_path):
    os.makedirs(result_prefix_path)

for response in all_responses:
    with open(prefix_path + response) as f:
        response_json = json.load(f)
    if 'choices' not in response_json:
        continue
    result = response_json['choices'][0]['message']['content']
    code_lines = result.split('```')[1].split('\n')
    if not code_lines[0].strip().startswith('class'):
        code_lines = code_lines[1:]
    code = '\n'.join(code_lines)
    with open(result_prefix_path + response[:-5] + '.java', 'w') as f:
        f.write(code)

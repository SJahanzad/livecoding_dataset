import os
import json
from tqdm import tqdm

CATEGORIES = ['nickwhite', 'neetcode']
category_name = CATEGORIES[1]

CODE_EXTENSIONS = {'nickwhite': '.java', 'neetcode': '.py'}

code_extension = CODE_EXTENSIONS[category_name]
codes_prefix_path = os.path.join('./codes', category_name)
transcripts_prefix_path = os.path.join('./transcripts', category_name)

response_prefix_path = os.path.join('./alignments/responses', category_name)
responses = os.listdir(response_prefix_path)

result_prefix_path = os.path.join('./alignments/results', category_name)
if not os.path.exists(result_prefix_path):
    os.makedirs(result_prefix_path)

errors_prefix_path = os.path.join('./alignments/errors', category_name)
if not os.path.exists(errors_prefix_path):
    os.makedirs(errors_prefix_path)

for response in tqdm(responses):
    print(response)
    response_path = os.path.join(response_prefix_path, response)
    with open(response_path, 'r') as f:
        response_data = json.load(f)
    
    result_json = []
    for partial_response in response_data:
        try:
            if partial_response['choices'][0]['finish_reason'] != 'stop':
                result_json = []
                break
            result_json.extend(
                json.loads(
                    partial_response['choices'][0]['message']['content']
                    .split('```json\n')[1]
                    .split('\n```')[0]
                )
            )
        except Exception as e:
            print(e)
            print('Error')
            print(partial_response)
            print()
            result_json = []
            break
    if not result_json:
        continue
    youtube_id = response.split('.json')[0]
    code_path = os.path.join(codes_prefix_path, youtube_id + '_code' + code_extension)
    with open(code_path) as f:
        code = f.read()
        code = code.split('\n')
    transcript_path = os.path.join(transcripts_prefix_path, youtube_id + '_transcript.json')
    with open(transcript_path) as f:
        transcript = json.load(f)
    timings = {
        item['text']: {
            'start': item['start'],
            'duration': item['duration']
        } for item in transcript
    }
    
    prev_item = transcript[0]
    for item in transcript[1:]:
        extended_text = prev_item['text'] + ' ' + item['text']
        timings[extended_text] = {
            'start': prev_item['start'],
            'duration': prev_item['duration'] + item['duration']
        }
        prev_item = item

    result = []
    for item in result_json:
        try:
            transcript_text = item['text']
            codes = item['code']
            result_timing = timings[transcript_text]
            result_item = {
                'text': transcript_text,
                'start': result_timing['start'],
                'duration': result_timing['duration'],
                'code': codes
            }
            result.append(result_item)
        except Exception as e:
            print(e)
            print('Error')
            print(item)
            print()

    result_path = os.path.join(result_prefix_path, youtube_id + '.json')
    with open(result_path, 'w') as f:
        json.dump(result, f, indent=4)
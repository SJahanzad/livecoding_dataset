import os
import json

lengths = []
path = 'alignments/results/nickwhite'
results = os.listdir(path)
for result in results:
    with open(os.path.join(path, result), 'r') as f:
        result_data = json.load(f)
        # lengths.append(len([x for x in result_data if len(x['code']) > 0])) 
        lengths.append(len([x for x in result_data])) 

print('Mean:', sum(lengths) / len(lengths))
print('Max:', max(lengths))
print('Min:', min(lengths))
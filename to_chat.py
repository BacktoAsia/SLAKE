import os
import json 

# ----------- Merge the train and validate  dataset ---------
current_dir = os.getcwd()
train_path = current_dir + '/chat_json/train.json'
test_path = current_dir + '/chat_json/test.json'
raw_train_path = current_dir + '/raw_data/train.json'
raw_test_path = current_dir + '/raw_data/test.json'
raw_valid_path = current_dir + '/raw_data/validate.json'

with open(raw_train_path, 'r') as file:
    raw_train = json.load(file)
with open(raw_valid_path, 'r') as file:
    raw_valid = json.load(file)
    
train = raw_train + raw_valid
with open(raw_test_path, 'r') as file:
    test = json.load(file)

# Wrtie train and test dataset to current_dir
with open(train_path, 'w') as file:
    json.dump(train, file)
with open(test_path, 'w') as file:
    json.dump(test, file)
    
# ---------- Transfer json data to chat form --------------
# We only preserve 'img_id', 'img_name', 'question', 'answer', 'qid'
# 'qid' is unique, so we preserve to seperate the dataset

train_chat = []
test_chat = []
keys = {'img_id': 'img_id',
        'img_name': 'img_name', 
        'question': 'question',
        'answer': 'answer', 
        'q_lang': 'q_lang', 
        'location': 'location',
        'modality': 'modality', 
        'answer_type': 'answer_type', 
        'base_type': 'base_type', 
        'content_type': 'content_type', 
        'triple': 'triple',
        'qid': 'qid'}

# Convert them to chat form
with open(train_path, 'r') as file:
    train = json.load(file)
with open(test_path, 'r') as file:
    test = json.load(file)

for point in train:
    input = f"Question: {point['question']}"
    output = f"The answer is {point['answer']}."
    
    train_chat.append({
                "qid": point['qid'],
                "image": point['img_name'],
                "conversations": [
                    {'from': 'human', 'value': f"{input}\n<image>"},
                    {'from': 'gpt', 'value': f"{output}"},
                ],
            })
    
for point in test:
    input = f"Question: {point['question']}"
    output = f"The answer is {point['answer']}."
    
    test_chat.append({
                "qid": point['qid'],
                "image": point['img_name'],
                "conversations": [
                    {'from': 'human', 'value': f"{input}\n<image>"},
                    {'from': 'gpt', 'value': f"{output}"},
                ],
            })
    
# ------------ Write result into json -------------
train_chat_path = current_dir + '/chat_json/train_chat.json'
test_chat_path = current_dir + '/chat_json/test_chat.json'

with open(train_chat_path, 'w') as file:
    json.dump(train_chat, file)
with open(test_chat_path, 'w') as file:
    json.dump(test_chat, file)


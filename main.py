import json
import pandas as pd
from clients_split import get_cleaned_data, non_iid_split_dirichlet, save_clients_json

train_path = '/Users/shuogudaojin/Public/Database/SLAKE/chat_json/train_chat.json'
raw_data_path = '/Users/shuogudaojin/Public/Database/SLAKE/chat_json/train.json'
saving_folder = '/Users/shuogudaojin/Public/Database/SLAKE/iid_clients_with_only_VQA'
cleaned_data = get_cleaned_data(raw_data_path)

with open(train_path, 'r') as file:
    train_chat = json.load(file)
    
# Drop the idx without image
cleaned_data = get_cleaned_data(raw_data_path)

# Get all of the topics
raw_data_pandas = pd.read_json(raw_data_path)
topics = raw_data_pandas['location']
topics = pd.unique(topics)
topics = topics.tolist()

#=============== Set the parameter to split clients ==================#
clients = non_iid_split_dirichlet(raw_data=cleaned_data, train=train_chat, topics=topics,
                                  ideal_counts=1000, n_clients=10, alpha=100)
save_clients_json(saving_folder, clients)
    

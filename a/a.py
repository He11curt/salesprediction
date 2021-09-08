import pickle
import json
import numpy as np
def load_artifacts():
    global _data_columns
    global _model
    
    print('Loading Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['data-columns']

    with open('./big_mart.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts...Loaded')

print(load_artifacts())

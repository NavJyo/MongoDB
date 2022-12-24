import pymongo  
import pandas  as pd 
import json 
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB") 
database = client['aps'] 
collection = database['sensor'] 
data_file_path = '/config/workspace/aps_failure_training_set1.csv' 
if __name__=="__main__": 
    df = pd.read_csv(data_file_path)  
    print(f'Number of Rows and Columns{df.shape}')   
    json_records = list(json.loads(df.T.to_json()).values())  
    collection.insert_many(json_records)  



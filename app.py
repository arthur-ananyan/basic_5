import json

def read_data(file_name):
    with open(file=file_name) as f:
        data = json.load(f)
        print(data)

read_data("data.json")
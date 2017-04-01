import json
from pprint import pprint

with open('./Dataset/exampleJSON.json') as data_file:
  data = json.load(data_file)
  pprint(data)
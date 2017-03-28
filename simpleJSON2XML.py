import json
from dicttoxml import dicttoxml

with open('data.json') as data_file:    
    json_obj = json.load(data_file)
    xml = dicttoxml(json_obj)
    print xml
import json
import pickle

with open('group.json', 'r', encoding='UTF8') as file:
    result = json.load(file)
print(result)
print(type(result))

with open('group.pickle', 'rb') as file:
    result = pickle.load(file)
print(result)
print(type(result))

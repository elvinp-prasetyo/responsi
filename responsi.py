# Python program to download
# json file
  
  
import json
  
# Opening JSON file
f = open('sample2.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)

a = '{"name": "Bob", "languages": "English"}'
  
# deserializes into dict 
# and returns dict.
y = json.loads(a)
  
print("JSON string = ", y)
print()
  
# Reading from file
data = json.loads(f.read())
  
# Iterating through the json
# list
for i in data['emp_details']:
    print(i)
  
# Closing file
f.close()
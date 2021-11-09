import requests # Allows you to send HTTP requests
import json # built in pacakge to work with json data

# convert from JSON to Python

#some json
x = '{ "name":"John", "age":30, "city":"New York"}'

#parse x
y = json.loads(x)

#result as a python dictionary
print(y["city"])
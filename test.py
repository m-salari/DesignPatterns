import json

d = {'name': 'mostafa', 'age': 30, 'city': 'tehran'}
print(json.dumps(d, indent=1, separators=(",,,,", ":W:"), sort_keys=True ))

# js = '{"name": "mostafa", "age": 30, "city": "tehran"}'
# print(json.loads(js))
import json
a = {'name': 'she', 'age': 21}
for i in a.keys():
    print(i)

data = json.dumps(a)
print(data)
print(a)
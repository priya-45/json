import json
a={
    '6': 5, 
    '8': 7, 
    '3': 3, 
    '4': 4}
b=sorted(a.items())
m={}
for i in b:
    m.update({i[1]:i[1]})
print(type(m))
h=json.dumps(m)
print(h)
print(type(h))
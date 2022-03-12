import json
a='{"a":1,"b":2,"c":3,"d":4}'
print(type(a))
b=json.loads(a)
print(type(b))
print(b)

a={"a":34,"b":56,"c":78,"d":29,"e":90}
m=[]
for l in a:
    m.append(a[l])
i=0
max=0
min=m[i]
while i<len(m):
    if m[i]>max:
        max=m[i]
    if m[i]<min:
        min=m[i]
    i=i+1
print(max)
print(min)
import json
dict1 ={
    1: {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    2: {
        "name": "Elis",
        "designation": "Trainee", 
        "age": "24",
        "salary": "40000"
    },}
print(type(dict1))
k=open("json_file.json","w")
json.dump(dict1,k,indent=4)
k.close()

# k=open("json_file.json","r")
# m=k.read()
# print(type(m))



a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
w,x,y,z={},{},{},{}
for i in range(len(a)):
    for i in range(len(b)):
        for i in range(len(c)):
            for bi in range(len(d)):
                p,q,r,s={},{},{},{}
                q.update({"name":a[0]})
                q.update({"Designation":a[1]})
                q.update({"Age":a[2]})
                q.update({"salary":a[3]})
                p["name"]=b[0]
                p["Designation"]=b[1]
                p["Age"]=b[2]
                p["salary"]=b[3]
                r["name"]=c[0]
                r["Designation"]=c[1]
                r["Age"]=c[2]
                r["salary"]=c[3]
                s["name"]=d[0]
                s["Designation"]=d[1]
                s["Age"]=d[2]
                s["salary"]=d[3]
            w.update({"emp1":q})
            x["emp2"]=p
            y["emp3"]=r
            z["emp4"]=s

print(w)
print(x)
print(y)
print(z)
# {"emp1":{ "name":"nilam","Designation":"programmer","Age":"34","salary":"24000",}}
# {"emp2":{ "name":"komal","Designation":"Trainee","Age":"24","salary":"20000",}}
# {"emp3":{ "name":"anuradha","Designation":"HR","Age":"25","salary":"40000",}}
# {"emp4":{ "name":"Abhishek","Designation":"Manager","Age":"29",}}
 


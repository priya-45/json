dic={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
item=input("enter item:")
price=int(input("enter price:"))
f=open("json1_file.json","w")
for i in dic:
    for j in dic[i]:
        if item==dic[i]:
            if item==j:
                print(dic)

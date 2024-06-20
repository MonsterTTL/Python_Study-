namebook = { "Name" : "Alex", "Age" : 18 , "Class" : "First" }
print(namebook.get("Name"))
# 只读Key
for key in namebook:
    print(key, namebook[key])
# 同时读KV
for key,value in namebook.items():
    print(key, value)

    
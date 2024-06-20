list = ["Red", "Green", "Blue"]
# insert函数添加元素
list.insert(0,"Yellow")
list.insert(1,"Grey")
# del语句删除数组元素
del list[0]
# pop函数弹出最后一个元素
last = list.pop()
# pop函数弹出指定元素
mid = list.pop((len(list)/2).__int__() + 1)
# 根据值移除元素
list.remove("Red")
print(last)
print(mid)
print(list)

mutiList = ["name", "age", 18]
print(mutiList)
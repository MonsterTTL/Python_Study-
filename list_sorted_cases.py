import copy

colors = [["Red", "Green"], ["Blue", "Grey", "Yellow"]]
colors2 = colors.copy()
#利用sort函数进行排序
colors.sort()
print(colors)
#传入reversed=True进行逆序排序
colors.sort(reverse = True)
print(colors)
#copy的第一层实际是实现了深拷贝，但如果有嵌套的话就是浅拷贝了
print(colors2)
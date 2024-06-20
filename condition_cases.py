str = ""
str += input()
if str == "a":
    print("A")
elif str == "b":
    print("B")
elif str == "c":
    print("C")
else:
    print("not match")

match(str):
    case "a": print("match a")
    case "b": print("match b")
    case "c": print("match c")
    case _: print("not match")
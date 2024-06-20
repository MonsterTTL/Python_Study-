def sayHello():
    print("hello python")

def mutiReturnType(clazz, a = 10):
    print("a = " + str(a))
    match(clazz):
        case "String": return "string"
        case "Number": return 1
        case "List": return [1,2,3,4,5]
        case _: print("not match")

def defaultParaMethod(a = 10, b = 11, c = 12, d = 13):
    print(a,b,c,d)

sayHello()
clazz = input()
result = mutiReturnType(clazz, a = 13)
print(result)
defaultParaMethod(d = 16)
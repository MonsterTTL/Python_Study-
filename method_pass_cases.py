def passingParam(str = "", int = 0, list = [], dic = {}):
    if (len(str) > 0):  str *= 2
    elif (int != 0):  int *= 2
    elif (len(list) > 0):  list *= 2
    elif (len(dic) > 0): dic["sp"] = 22
def biggestNumber(*numbers):
    biggest = numbers[0]
    for number in numbers[1:]:
        if number > biggest:
            biggest = number
    return biggest

bigNumber = biggestNumber(-1,5,6,10,-9,105)
print("biggest", bigNumber)


# string
print("===================string=====================")
para = "abc"
result = passingParam(str = para)
print(para)

# int
print("===================int=====================")
para = 11
result = passingParam(int = para)
print(para)
# list
print("===================list=====================")
para = [1,2,3]
result = passingParam(list = para)
print(para)
# dic
print("===================dic=====================")
para = {"gender":"man", "age":16}
result = passingParam(dic = para)
print(para)
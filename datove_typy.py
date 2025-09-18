tuple = (1, "a", 2, 5, 4)
print("tuple: ", tuple)

list = [1, "a", 2, 5, 4]
print("list: ", list)

set = {1, "a", 2, 5, 4}
print("set: ", set)

dict = {
        1 : "a",
        "a" : "b",
        2 : 1000,
        5 : "d",
        4 : "e",
}

print("dict: ", dict)

try:
    string = "132" + int(1) + "54"
    print("string: ", string)
except Exception as e:
    print(e)


tuple = (1, 2, 3, 4, 5)
print("tuple[2]: ", tuple[2])

list = [1, 2, 3, 4, 5]
print("list[2]: ", list[2])

try:
    set = {1, 2, 3, 4, 5}
    print("set[2]: ", set[2])
except Exception as e:
    print(e)


dictionary = {
        1 : "a",
        2 : "b",
        3 : "c",
        4 : "d",
        5 : "e",
}

print("dictionary[2]: ", dictionary[2])

string = "12345"
print("string[2]: ", string[2])

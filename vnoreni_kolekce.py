tuple = ((1, 2), (3, 4))
print("tuple: ", tuple)

list = [[1, 2], [3, 4]]
print("list: ", list)

try:
    set = {{1, 2}, {3, 4}}
    print("set: ", set)
except Exception as e:
    print(e)


dictionary = {
        1 : "a",
        2 : {1 : 3},
        3 : "c",
        4 : "d",
        5 : "e",
}

print("dictionary: ", dictionary)

# tohle proste nejde :(
string = "12345"
print("string: ", string)

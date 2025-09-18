tuple = (None)
print("tuple: ", tuple)

list = [None]
print("list: ", list)

set = {None}
print("set: ", set)

dict = {
        None : None,
}

print("dict: ", dict)

try:
    string = "" + None
    print("string: ", string)
except Exception as e:
    print(e)

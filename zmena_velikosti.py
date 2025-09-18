tuple = (1)
print(dir(tuple))
# nema zadnou funkci pro upravu velikosti

list = [1]
print("list len: ", len(list))
list.append(2)
print("list len: ", len(list))

set = {1}
print("set len: ", len(set))
set.add(2)
print("set len: ", len(set))

dict = {
    1 : "a"
}
print("dict len: ", len(dict))
dict[2] = "b"
print("dict len: ", len(dict))

string = "1"
print(dir(string))
# nema zadnou funkci pro upravu velikosti

tuple = (1,2,3,4,5)
try:
    tuple[2] = 1000
except Exception  as e:
    print(e)

list = [1, 2, 3, 4, 5]
list[2] = 1000
print("list: ", list)

set = {1, 2, 3, 4, 5}
try:
    set[2] = 1000
except Exception as e:
    print(e)

dict= {
        1 : "a",
        2 : "b",
        3 : "c",
        4 : "d",
        5 : "e",
}
dict[2] = 1000
# tohle nemusi byt 3 prvek v dict 
print("dictionary: ", dict)

string = "12345"
try:
    string[2] = "A" 
except Exception as e:
    print(e)

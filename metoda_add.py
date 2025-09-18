tuple = (1, 2)
try:
    tuple.add(3)
except Exception as e:
    print(e)

list = [1]
try:
    list.add(2)
except Exception as e:
    print(e)

set = {1}
try:
    set.add(2)
except Exception as e:
    print(e)

dict = {
    1 : "a"
}
try:
    dict.add(2)
except Exception as e:
    print(e)

string = "1"
try:
    string.add(2)
except Exception as e:
    print(e)

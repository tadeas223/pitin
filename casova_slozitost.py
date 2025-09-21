import time

def calc_times(first_list,last_list, t1, t2, t3):
    first_list.append(t2 - t1)
    last_list.append(t3 - t2)

first_list = []
last_list = []

tuple = tuple(range(1000))
for _ in range(1000):
    t1 = time.time_ns()
    a = tuple[0]
    t2 = time.time_ns()
    a = tuple[-1]
    t3 = time.time_ns()

    calc_times(first_list, last_list, t1, t2, t3)

print("tuple[0]: ", sum(first_list) / len(first_list))
print("tuple[-1]: ", sum(last_list) / len(last_list))

first_list = []
last_list = []

list = list(range(1000))
for _ in range(1000):
    t1 = time.time_ns()
    a = list[0]
    t2 = time.time_ns()
    a = list[-1]
    t3 = time.time_ns()

    calc_times(first_list, last_list, t1, t2, t3)

print("list[0]: ", sum(first_list) / len(first_list))
print("list[-1]: ", sum(last_list) / len(last_list))

first_list = []
last_list = []

set = set(range(1000))
for _ in range(1000):
    t1 = time.time_ns()
    a = 0 in set
    t2 = time.time_ns()
    a = 256 in set
    t3 = time.time_ns()

    calc_times(first_list, last_list, t1, t2, t3)

print("set[0]: ", sum(first_list) / len(first_list))
print("set[-1]: ", sum(last_list) / len(last_list))

first_list = []
last_list = []

dict = {}
for i in range(1000):
    dict[i] = i

for _ in range(1000):
    t1 = time.time_ns()
    a = dict[0]
    t2 = time.time_ns()
    a = dict[999]
    t3 = time.time_ns()

    calc_times(first_list, last_list, t1, t2, t3)

print("dict[0]: ", sum(first_list) / len(first_list))
print("dict[999]: ", sum(last_list) / len(last_list))

first_list = []
last_list = []

string = 'a' * 1000
for _ in range(1000):
    t1 = time.time_ns()
    a = string[0]
    t2 = time.time_ns()
    a = string[-1]
    t3 = time.time_ns()

    calc_times(first_list, last_list, t1, t2, t3)

print("string[0]: ", sum(first_list) / len(first_list))
print("string[-1]: ", sum(last_list) / len(last_list))

first_list = []
last_list = []

print("O(N) reference: ")
list = range(1000)
for _ in range(100):
    t1 = time.time_ns()
    a = list[0]
    t2 = time.time_ns()
    for i in list:
        if list[i] == 999:
            break;
    t3 = time.time_ns()
    
    calc_times(first_list, last_list, t1, t2, t3)

print("list[0]: ", sum(first_list) / len(first_list))
print("list[-1]: ", sum(last_list) / len(last_list))

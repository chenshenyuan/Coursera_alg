

list_test = [3,1,3,1,2,3,4,5]
b = [1,2]
print(list_test)
new_list = [v for i, v in enumerate(list_test) if i not in b]
print(new_list)
a = '123'
d = '22'
c = a+d
print(int(c))



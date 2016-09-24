# Author: Tian
a = [1, 2, 3]
print("a is")
print(a)

print("the first element in a is")
print(a[0])

file = open('local_file.txt', 'w')
for i in a:
    file.write(str(i)+'\n')
file.close()
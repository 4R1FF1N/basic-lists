sum = 0 
for i in range(1000):
    sum = sum + 1
    print(sum)


list = [1,2,3,4,5,6,7,8,9,10]
print(list)
append = input("Enter your number to append...: ")

list.append(append)
print(list)

remove = input("Enter your number to remove...: ")
list.remove(int(remove))
print(list)


list1 = ["hello", 2, 5, "goodbye"]
list2 = []
list3 = []



for item in reversed(list1):
    list2.append(item)

print(list2)

counter2 = len(list1)
print(counter2)

for x in range(0, counter2):
    list3.insert(x,list1[counter2-1])
    print(list3)
    counter2 -=1


print(list3)
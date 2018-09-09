import random
list1=[1]
for n in range(2,50):
    list1.append(n)

list2=random.sample(list1,6)
list2.sort()
for m in range(0,6):
    list1.remove(list2[m])

special=random.choices(list1,k=1)
print(list2)
print(special)

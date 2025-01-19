data_list = [-5,8 ,-23, 5, 0, 23, -6, 23,7, 67]



for i in range(len(data_list)):
    for j in range(i+1,len(data_list)):
        if data_list[i]>data_list[j]:
            data_list[i],data_list[j]=data_list[j],data_list[i]
            print(data_list)

# Code to determine which all numbers are divisible by 2
# Get the number of elements 
n = int(input("Enter the number of elements in the array: ")) 
#Collecting elements from the user 
dl = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
print(dl)
div_t=[]
for b in dl:
    if b%2==0:
        div_t.append(b)
print(div_t)

largest_num=data_list[0]
for m in data_list:
    if m>largest_num:
        largest_num=m
        print(m)
        print(largest_num)
print(largest_num)

smallest=data_list[0]
for n in data_list:
    if n<smallest:
        smallest=n
print(smallest)

print(data_list)
print("largest_num is:",data_list[-1])


for k in range(len(data_list)):
    print(k)

import numpy as np


rand_vals = np.random.rand()
print(rand_vals)

a=[0,1,2,3,4,5,6,7,8,9]
j=0
while j<len(a):
    for i in range(len(a)):
        if (a[i]+a[j])%9==0:
            print(a[i],a[j])
    j+=1

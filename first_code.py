print("Helloworld")
a=2
b=3
c=a+b
print(c)
print("Hello how do you do?")
d=c+3
print(d)
abc=d-2
print(abc)

a=60
b=160/a
print(int(b))
na="Michael Jackson"
for i in na:
    print('M',i)
bh='is the best'
print(na[0],na[0:5:3],na[::2])
cv=na+bh;print(cv)
bh.find('goal')

name = 'Lizz';print(name[0:2])

tup=(0,1.5,'goal')
type(tup)
tu2=(5,4,3,2)
tu2=sorted(tu2)
print(tu2)
tu3=[0,12,5]
j=['a,b,c,d','d']
j.split(",")
A=(0,1,2,3)
print(A[-1])
A[-1:]
k=set(j)
# Example dictionary
my_dict = dict(name="Alice", age=25, city="New York")
print(my_dict)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
a=range(10,15)

for i in range(0,len(a)):
    print(a[i])

n=17
for i in range(0,len(a)):
    print(n+a[i])
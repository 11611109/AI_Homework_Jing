import random
#Question1
fruit_list=["banana","apple","mango","orange","watermelon"]

#Question2
print("Queston2")
for fruit in fruit_list:
    if fruit=="apple":
        print("I found it!")

#Queston3
fruit_list.append("grapes")
fruit_list.append("pear")

#Question4
print("Queston4")
letter_number=[]
for fruit in fruit_list:
    letter_number.append(len(fruit))
print(letter_number)

#question 5
print("Queston5")
def half_squared(list):
    for number in range(0,len(list)):
        list[number]=list[number]**2/2
        #print(list[number])
    return list
print(half_squared([3,3]))

#question 6
print("Queston6")
a=int(input("input the score"))
if(a>100|a<0):
    print("Wrong input.Please input a integer  number(0-100)")
elif(a>=90):
    print("A")
elif(a>=60):
    print("B")
else:
    print("C")

#Question7
print("Queston7")
def sort(a,b,c):
    if(a<b):
        a,b=b,a
    if(a<c):
        a,c=c,a
    if(b<c):
        b,c=c,b
    return a,b,c
print(sort(30,12,4))

#Question8
print("Queston8")
list1=[1,2,3]
list2=[4,5]
array=[list1,list2]
sum=0
#Method1
for i in range (len(array)):
    for j in range(len(array[i])):
        print(str(array[i][j])+" ",end="")
print()
#Method2利用句柄
for m in array:
    for n in m:
        print(str(n)+" ",end="")
print()

#Question9
print("Queston9")
test=[1]
for num in range(2,101):
    test.append(num)
def f(x):
    return x**3
ii=1
for y in map(f,test):
    sum=0
    for t in str(y):
        sum+=int(t)
    if(sum==ii):
        print(str(ii)+" ",end="")
    ii+=1
print()

#Question10
print("Queston10")
x=random.randint(1,10)
y=random.randint(1,10)
print("The random numbers generated are "+str(x)+" and "+str(y))
z=x
x=y
y=z
print("The random numbers exchanged are "+str(x)+" and "+str(y))

#Question11
print("Queston11")
lines=4
for p in range(1,5):
    print(' '*(6-p),end=""),
    print('*'*(2*p-1))
for q in range(1,4):
    print(' '*(q+2),end=""),
    print('*'*(7-2*q))

#Question12
print("Queston12")
for z in range(1,7):
    for w in range (z,(z+6)):
        if (w%6==0):
            print(6,end="")
        else:
            print(w%6,end="")
    print()

#Question13
print("Queston13")
players=['charles','martina','michael','florence','eli']
for name in players[0:3]:
    print(name.title(),end="")

#ques 1
rev=[1,2,3,4,5,6,7,8]
rev.reverse()
print(rev)

#ques 2
text=input("enter the string")
null=" "
for i in text:
    if i.isupper():
        null=null+i+','
print(null)

#ques 3
li=[]
li1=[]
p=input()
li=p.split(',')
for i in range (len(li)):
    li1.append(int(li[i]))
print(type(li1[0]))#string input got converted into int 
print(li1)

#ques 4
number=(input('enter no'))
temp=number
rev=number[::-1]
if(temp==rev):
    print("pallindrome")
else:
    print("not a pallindrome")
#Another method by reversing the number
'''
temp=number
rev=0
while(number>0):
    number=number%10
    rev=rev*10+number
    number=number/10
if(temp==rev):
    print("pallindrome")
else:
    print("not a pallindrome")
'''
#ques 5
#shallow copy
import copy as c
list1=[1,2,[3,4],5]
list2=c.copy(list1)
list1[2][1]='world'
print(list1)
print(list2)

#ques 6
#deep copy
import copy as c
list1=[1,2,[3,4],5]
list2=c.deepcopy(list1)
list1[2][1]='world'
print(list1)
print(list2)

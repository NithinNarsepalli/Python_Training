'''n=int(input())
ans=n*(n+1)/2
print(ans)
#in python the main synntax is indentation
-------------------------------------------
#convert the asci value into python and python into asci value
n=input()
print(ord(n))
x=int(input())
print(chr(x))
-------------------------------------------
#number is immutable in python
a=10
print(id(a))
a=20
print(id(a))
-------------------------------------------
#eval function
a=input()
print(eval(a))
-------------------------------------------
Type casting:-to convert the dat type we need to use constructors->
To change any data type into integer data type we use int().
To change any data type into float data type we use float().
To change any data type into string data type we use str().
To change any data type into complex data type we use complex().
NOTE:- To check the data type of the variable we use type(variable).
-------------------------------------------
format specifiers
a=float(input())
print('{:.2f}'.format(a))
print("%.2f"%a)
-------------------------------------------
Random function
import random
print(random.randrange(1,10))
-------------------------------------------
#To print quotes:
a="Hello\"Ramu\""
print(a)
-------------------------------------------
Boolean outputs true if the variable contains any values in it and it returns false when the given value is null or 0.
a=bool(input())
print(a)
-------------------------------------------
Operators:->
-Arithmetics operators[+,-,*,/,%,//,**]
-Assignment operators[+=,-=,*=,/=,%=,//=,**=]
-Conditional operators[<,>,>=,<=,==]
-Logical operators[ and,or,not]
-Bitwise operators[]
-Membership operators[in,not in](compares the values)
-Identity operators[is](compares the object)
-Ternary operator:(shortend if else)
num= int(input())
print("even") if(num%2==0) else print("odd")

-------------------------------------------
'''
'''
NOTE:id() is used to check the address of the object.
Memories that availabe in python:->
1.Stack:Functions,variables will be stored in here in a continuous manner.
2.Heap:Classes are stored in here.Inside this small integer cache will be present
--->Small Integer Cache[-5 to 256]
--->Static memory uses same address
3.String Pool: String literals will be stored in the string pool.when the string is 
assigned statically.
--->the address values will be same for the strings
-------------------------------------------
Control Statements: It controls the flow of the program.It is used to control the 
flow of statements in program.
-------------------------------------------
A).Decision making Statements:
It decides which code to be execute and when.There are two type of Statements in it they are
a.IF Statement:
1.Simple if:-
syntax:-
if(cond):#if the Condition is true then the below Statements will execute
-Statements

short hand if(age>=18): print("Eligible to vote")
-------------------------------------------------------------------------------
2.Else:-In the else block there will be no condition if the if block condition 
fails to execute then else block Statements will be executed.
syntax:-
if(cond): if it fails then else will be executed
    Statements
else:
    statements
-------------------------------------------
example1:
n=input().lower()
if(n=="meghana died"):
    print("Surya meets Priya")
else:
    print("Surya Weds Meghana")
-------------------------------------------
example2:
result=input().lower()
if(result=="won"):
    print("E Sala Cup Namade")
else:
    print("Tata bye bye")
-------------------------------------------  
example3:
n=int(input())
if(n%2==0):
    print("even")
else:
    print("odd")
-------------------------------------------
example4:
year=int(input())
if(year%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")
-------------------------------------------
example 5:
a=200
b=33
c=500
if a>b and c>a:# we can use and,or,not in the if condition Statements
    print(true)

-------------------------------------------------------------------------------
3.If-Elseif Ladder:In this first there will be if Statement and there after elif 
block and therenext else block will be present.

Syntax:
    
if(condition):
    Statement1
elif(condition):
    Statement2
else:
    Statement3
----------------------------------------
example1:
    
num=int(input())
if(num>0):
    print("Positive")
elif(num<0):
    print("Negative")
else:
    print("Zero")
----------------------------------------
4.Nested If: The if block containing another if block is know as the nested if.

Syntax:

if(cond1):
    if(cond2):
        Statements
else:
    statements
----------------------------------------
Example1:-

age=int(input())
weight=int(input())
if(age>=20):
    if(weight>=50):
        print("Eligible for the military")
else:
    print("Not Eligible")
-------------------------------------------------------------------------------


'''
'''
k=input().lower()
if(k.isnumeric()): #checks whether the given number is numeric or not. isnumeric is a method in python.
    print("Entered value is numeric")
elif(k.isalpha()): #checks whether the given number is alphabet or not. isalpha is a method in python.
    if(k in "aeiou"):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Given value is Special Character")

'''
'''
-------------------------------------------------------------------------------
examples:
----------------------------------------
1
marks=int(input())
if(marks>35):
    print("pass")
else:
    print("fail")
----------------------------------------
2
income=int(input())
if(income<7000):
    print("eligible for scholarship")
else:
    print("Not eligible for scholarship")
------------------------------------------
3
n=int(input())
if(n%3==0 and n%5==0):
    print("It is divisible by 3 and 5")
else:
    print("It is not divisible by 3 and 5")
------------------------------------------
4
marks=int(input())
if(marks>70):
    print("Good")
elif(marks>=35 and marks<=70):
    print("Average")
else:
    print("Poor")

-------------------------------------------------------------------------------
#mini calculator
num1=int(input())
num2=int(input())
op=input().lower()
oper=["add","sub","mul","div","+","-","*","/"]
if(op in oper):
    if(op =="add" or op=="+"):
        print(num1+num2)
    elif(op == "sub" or op=="-"):
        print(num1-num2)
    elif(op=="mul" or op=="*"):
        print(num1*num2)
    else:
        print(num1//num2)
else:
    print("Give the crct operation")
-------------------------------------------------------------------------------
#check whether the candidate is eligible for drive or not
per=float(input())
if(per>70):
    name=input('Enter your name:')
    Dept=input('Enter your Department:')
    loc=input("Enter your location:")
    print("You are eligible.")
else:
    print("Sorry you are not eligible for the drive!")
-------------------------------------------------------------------------------
#check whether the candidate is eligible for drive or not
per=float(input())
if(per>70):
    name=input('Enter your name:')
    Dept=input('Enter your Department:')
    loc=input("Enter your location:")
    print("You are eligible.")
else:
    print("Sorry you are not eligible for the drive!")
-------------------------------------------------------------------------------
#checking weather the consumer is elgible for loan or not
sal=int(input("Salary:"))
age=int(input("Age:"))
if(sal>=20000 or age<=25):
    loan_amt=int(input("Enter Loan Amount:"))
    if(loan_amt<=50000):
        print("You are elgible for loan")
    else:
        print("Maximum loan amount is 50,000")
else:
    print("You are not eligible for loan")
-------------------------------------------------------------------------------

B).Match Statement:- Match Statement is a Conditional statement in python which 
is similar to switch in java and c.In match statement we dont need to give break 
in python as it is  required in c and java.It is introduced on 3.1.
Note: In match case the sinlg line symbol'|' is considerd as or operator

Syntax:
match variable_name:
    case "pattern1": Statement1
    case "pattern2": Statement2
    .
    .
    .
    case "n" : statement n
    case_: default statement_     #default statement is denoted using '_'. 
-------------------------------------------------------------------------------
Example1:
n=int(input("enter number:"))
match n:
    case 10: print("ten")
    case 20: print("twenty")
    case 30: print("thirty")
    case _: print("not 20,10,30")
------------------------------------------
Example2:
n=int(input("enter number:"))
match n:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("not a valid input")
------------------------------------------
Example3:
n=int(input("enter number:"))
match n:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6|7: print("Weekend")
    case _: print("not a valid input")
------------------------------------------
Example4:
user=input().lower()
match user:
    case "admin"|"manager": print("Have full access")
    case "guest": print("limited access")
    case _: print("no access")
------------------------------------------
Example5:
alpha=input().lower()
match alpha:
    case "a"|"e"|"i"|"o"|"u": print("Vowels")
    case _: print("Consonant")
-------------------------------------------------------------------------------
#Checking whether the given input is alphabet and checking whether is Vowel or Consonant
alpha=input().lower()
if (alpha.isalpha()):
 match alpha:
    case "a"|"e"|"i"|"o"|"u": print("Vowels")
    case _: print("Consonant")
else:
    print("not an alphabet")
-------------------------------------------------------------------------------
Looping Statement:
A).For: For loop is used to iterate the sequence.For loop is used for list,string,dictionary,set,tuple.
Syntax:
for i in range:
    Statements
------------------------------------------
Example1:
for i in "apple":
    print(i,end=" ")
------------------------------------------
Example2:
a=input()
for i in a:
    print(i,end=" ")
------------------------------------------
Example3:
#check how many vowels and consonants are present in the given string
name=input().lower()
k=0
z=0
for i in name:
    if i in "aeiou":
        k+=1
    else:
        z+=1
print("Number of vowels= ",k)
print("Number of Consonants=",z)
-------------------------------------------------------------------------------
B).While:
example:
-----------------------------------
#take inputs  until we get zero
while(True):
    a=int(input())
    if(a==0):
        print("You entered zero")
        break
    else:
        print("Enter number again")
o/p:-
7
Enter number again
7
Enter number again
0
You entered zero
--------------------------------------











-------------------------------------------------------------------------------
Jumping Statements: It is basically used to break or jump to particualr Statement
when it mets the condition.
-------------------------------------------------------------------------------
1.Break:-It will break the loop when it meets the condition.
syntax:-
if(cond):
    break
-----------------------------------------------------
example:-
n=10
for i in range(1,n+1)
if(i==5):
    break
else:
    print(i)
o/p:-
1 2 3 4 
--------------------------------------------------
2.Continue:- It jumps the particular condition.
syntax:-
if(cond):
 Continue
else:
 print(i)
----------------------------------------------------
example:
n=10
for i in range(1,n+1)
if(i==5):
 Continue
else:
 print(i)
------------------------------------------------------
o/p:-
1 2 3 4 6 7 8 9
------------------------------------------------------
3.Pass:If statement cannot be empty but for some reason
you need to leave the if statement empty then it will show error
to avoid those errors we need to use the keyword called pass.
------------------------------------------------------------
syntax:
if(cond):
 pass
statements
------------------------------------------------------------
example:
n=10
for iin range(1,n+1):
 if(n==5):
    pass
 print(i,end=" ")
o/p:-
1 2 3 4 5 6 7 8 9 10
-------------------------------------------------------------------------------
****************************Types of collection or iterables*********************
In python there are 4 types of iterables.4 of them are used to store different 
values in one variable.And 4 of them have different properties.
1.List
2.Tuple
3.Dictionary
4.Set
-------------------------------------------------------------------------------
List:- List is ordered colleciton of item.List allows duplicates.It index starts
from 0.Size is not fixed we are not needed to specify the size of the list.List 
is mutable.List is a class in python.It allows any datatype unlike array.
syntax:
list_name=[val1,val2,...,valn]
-------------------------------------------------------------------------------
examples:
---------------------------------------------------------------------
L=["NITHIN","RAMESH"]
TO access:
print(L[1])
o/p:-"RAMESH"
-------------------------------------------
#to find the length of list
print(len(L))
o/p:-2
-------------------------------------------
#to print the values of list one by one.
for i in li:
    print(i)
o/p:-
NITHIN
RAMESH
-------------------------------------------
for i in range(0,len(li)):
    print(li[i])
o/p:-
NITHIN
RAMESH
*******************Functions in the List******************************
----------------------------------------------------------------------
#to insert values into the list
Insert function is used to insert at the particular position.
li=[1,2,3,4]
li.insert(2,"Nithin")
print(li)
o/p:-
[1,2,"Nithin",4]
----------------------------------------------------------------------
#append function
Append function is used to add the element at the end of the list.
li=[1,2,3,4]
li.append("Nithin")
print(li)
o/p:-
[1,2,3,4,Nithin]
----------------------------------------------------------------------
#to get list size and there after list values and then print them one by one
n=int(input()) #size of list
li=[] #list assignment
for i in range(n): 
    i=input()
    li.append(i)
for k in li:
    print(k)
o/p:-
1
nithin
1
nithin
----------------------------------------------------------------------
#Split function in list
k=input().split(" ")
print(k)
o/p:-
hello this is split function 
['hello', 'this', 'is', 'split', 'function']
----------------------------------------------------------------------
#Extend function
Extend function is used to add two lists.
syntax:
list_name.extend(list_name)
-------------------------------------------
example:
a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
print(a)
o/p:-
[1, 2, 3, 4, 5, 6, 7, 8]
-------------------------------------------
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
o/p:-
[1, 2, 3, 4, 5, 6]
-------------------------------------------
a=[1,2,3]
b=(4,5,6)
a.extend(b)
print(a)
o/p:-
[1, 2, 3, 4, 5, 6]
-------------------------------------------

Displaying the list:-
If we want to fetch the particular index value element
then we can use the index to see.
----------------------------------------
li=[1, 2, 3, 4, 5, 6, 7, 8]
print(li[2:5])
o/p:-
[3, 4, 5]
----------------------------------------
print(li[-1])
o/p:-
8
----------------------------------------
li=[1, 2, 3, 4, 5, 6, 7, 8]
print(li[:4])
o/p:-
[1, 2, 3, 4]
----------------------------------------
li=[1, 2, 3, 4, 5, 6, 7, 8]
print(li[2:])
o/p:-
[3, 4, 5, 6, 7, 8]
----------------------------------------
li=[1, 2, 3, 4, 5, 6, 7, 8]
print(li[::-1])
o/p:-
[8, 7, 6, 5, 4, 3, 2, 1]
----------------------------------------
k="ramu"
print(k[::-1])
o/p:-
umar
----------------------------------------
#to modify values in the list we use the particular index to update
li=[3, 4, 5, 6, 7, 8]
li[3]="three"
print(li)
o/p:-
[3, 4, 5, 'three', 7, 8]
----------------------------------------
#to Update the specified index values
li=["abc","123","efg","456","xyz"]
li[2:4]=["lmn","789"]
print(li)
o/p:-
['abc', '123', 'lmn', '789', 'xyz']
----------------------------------------
Remove():- The remove function will remove the specified item.
syntax:
list_name.remove(value)
----------------------------------------
example:
li=["abc","123","efg","456","xyz","efg"]
li.remove("efg") #it removes the only first "efg" in the list
print(li)
o/p:-
['abc', '123', '456', 'xyz', 'efg']
----------------------------------------
pop():- It is used to delete the values in the list
syntax:-
list_name.pop()
example:
li=["abc","123","efg","456","xyz","efg"]
li.pop()#removes the last value in the list
print(li)
o/p:-
['abc', '123', 'efg', '456', 'xyz']
----------------------------------------
clear():-it is used to clear all the values is the list.
syntax:-
list_name.clear()
-------------
li=["abc","123","efg","456","xyz","efg"]
li.clear()#removes the last value in the list
print(li)
o/p:-
[]
---------------------------------
del:-it is a keyword used to delete the list in the memory
syntax:
del list_name
-------------
example:-
li=["abc","123","efg","456","xyz","efg"]
del li
print(li)
o/p:-
 File "/home/main.py", line 639, in <module>
    print(li)
NameError: name 'li' is not defined
----------------------------------------------------------------
#Important functions in the Iterables
Sort():-It will sort ascending to descending.
syntax:-
list_name.sort()
-------------
example:
li=[10,20,30]
li.sort()
print(li)
o/p:-
[10, 20, 30]
-------------
#for descending to ascending
li=[200,300,800]
li.sort(reverse=True)
print(li)
o/p:-
[800, 300, 200]
----------------------------------------------------------------
#to reverse the list
reverse():-to reverse the given list
syntax:-
list_name.reverse()
-------------
li=[1,2,3]
li.reverse()
print(li)
o/p:-
[3, 2, 1]
----------------------------------------------------------------
li=["abc","xyz","123","456"]
li.sort()
print(li)
o/p:-
['123', '456', 'abc', 'xyz']
----------------------------------------------------------------

#to copy one list to other
#method1
li=['123', '456', 'abc', 'xyz']
copy=li
print(copy)
o/p:-
['123', '456', 'abc', 'xyz']
-------------
#method2
k=li.copy()
o/p:-
['123', '456', 'abc', 'xyz']
-------------
#method3
k=[1,2,3]
li1=list(k)
print(li1)
o/p:-
[1, 2, 3]
-------------
#to concatenate two lists
li1=[1]
li2=list(li1)
li3=li1+li2
print(li3)
o/p:-
[1, 1]
-------------
#to return the maximum value in the list
li=[1,2,3]
print(max(li))
o/p:-
3
-------------
#to return the minimum value in the list
li=[1,2,3]
print(min(li))
o/p:-
1
-------------
#to return the sum of the values in the list
li=[1,2,3]
print(sum(li))
o/p:-
6
-------------
#to count values in the list
li=[1,2,3,3,3]
print(li.count(3))
o/p:-
3
----------------------------------------------------------------
#index function is used to find in which index the value is present
li=[1,2,3,4,5,6]
print(li.index(3))
o/p:-
2
----------------------------------------------------------------
Nested List:List inside alist is known as the nested.
syntax:-
li=[[li1],[li2],.,.,[lin]]
----------------------------------------------------------------
#printing the nested list
li=[[1,2,3],[1,2,3],[1,2,3]]
print(li)
o/p:-
[[1,2,3],[1,2,3],[1,2,3]]
----------------------------------------------------------------
#modifying values in the nested list
li=[[1,2,3],[1,2,3]]
li[0][1]=100
print(li)
o/p:-
[[1, 100, 3], [1, 2, 3]]
----------------------------------------------------------------
#to modify the particular element in the list 
li=[[1,2,3],[2,3,4],[4,5,6]]
li1=li[0]
li.pop(0)
print(li)
o/p:-
[[2, 3, 4], [4, 5, 6]]
----------------------------------------------------------------
li=li=[[1,2,3],[2,3,4],[4,5,6]]
li[0].remove(2)
o/p:-
[[1, 3], [2, 3, 4], [4, 5, 6]]
----------------------------------------------------------------
li=[[1,2,3],[2,3,4],[4,5,6]]
li[0].pop(0)
print(li)
o/p:-
[[2, 3], [2, 3, 4], [4, 5, 6]]
----------------------------------------------------------------
li=[[1,2,3],[2,3,4],[4,5,6]]
s=0
for i in range (0,len(li)):
 s=s+sum(li[i])
print(s)
o/p:-
30
----------------------------------------------------------------
Tuples:-It comes under a collection it also stores the different values in it
and it has the index.It is a immutable and ordered.It allows duplicate values.
Index starts from 0.Tuple is denoted "()".
Syntax:-
TUPLE_NAME=(val1,val2,...valn)
-------------
example:-
tpl=(1,2,3)
print(tpl)
o/p:-
(1,2,3)
-------------
#length of tuple can be determined using len(TUPLE_NAME)
tpl=(1,2,3)
print(len(tpl))
o/p:-
3
-------------
tpl=("abc",)
print(type(tpl))
o/p:-
<class 'tuple'>
-------------
tpl=("abc")
print((type(tpl)))
o/p:-
<class 'str'>
-------------
#convert it into tuple
lis=[1,2,3]
tpl=tuple(lis)
print(tpl)
o/p:-
(1,2,3)
-------------
#convert it into list
tup=(1,2,3)
tpl=list(tup)
print(tpl)
print(lis(tup))
o/p:-
[1, 2, 3]
-------------
tpl=(1,2,3)
print(tpl[1:])
o/p:-
(2, 3)
-------------
Slicing
[start:stop:step]
-------------
#updating tuple
tpl=(1,2,3)
li=list(tpl)
li[2]=10
tpl=tuple(li)
print(tpl)
o/p:-(1, 2, 10)
-------------
#inserting value in tuple
tpl=(1,2,3)
li=list(tpl)
li.insert(0,10)
li.append(20)
li[0]=100
tpl=tuple(li)
print(tpl)
o/p:-
(100, 1, 2, 3, 20)
-------------
#removing the value
tpl=(1,2,3)
li=list(tpl)
li.remove(2)
tpl=tuple(li)
print(tpl)
o/p:-
(1, 3)
-------------
tpl=(1,2,3)
li=list(tpl)
li.pop(2)
tpl=tuple(li)
print(tpl)
o/p:-
(1, 2)
-------------
#packing the tuple
tpl=(1,2,3)
print(tpl)
#unpacking the tuple
(one,two,three)=tpl
print(three)
o/p:-
(1, 2, 3)
3
-------------
tpl=(1,2,3,4)
(A100,B200,*B300)=tpl
print(B300)
O/P:-
[3, 4]
-------------
TPL=(1,2,3)
for i in TPL:
    print(i)
o/p:-
1
2
3
-------------
tpl=("1","2")
t=tpl*2
print(t)
o/p:-
('1', '2', '1', '2')
-------------
tpl=(1,2,3,4)
print(tpl.count(3))
o/p:-
1
-------------
tpl=(1,2,3,4)
print(tpl.index(3))
o/p:-
2
-----------------------------------------------------------------------------
Set:- It is used to store multiple values in a single variable.Set is unordered and
unindexed.Set is unchangeable.We can add and remove the value.Set wont allow duplicates.
Set is mutable.
Syntax:-
set_name={setvalues}
-------------
#set will print randomly
set={"ramu","raju","ramu"}
print(se)
o/p:-
{'raju', 'ramu'} #filtered duplicate values
-------------
#if there are 1 and true as a value in set it will return true only
sse={"abc",1,True,False}
print(se)
o/p:-
{False, 1, 'abc'}
-------------
#len function
se={False, 1, 'abc'}
print(len(se))
o/p:-
3
-------------
#type of variable
se={False, 1, 'abc'}
print(type(se))
o/p:-
<class 'set'>
-------------
#printing one by one values
se={False, 1, 'abc'}
for i in se:
    print(i)
o/p:-
False
1
abc
-------------
#check whether the given value is present in the set or not
name=input().lower()
se={"ford","bmw","suzuki"}
if name in se:
    print("yes")
else:
    print("no")
o/p:- 
bmw
yes
-------------
Add():-Add method is used to add values into the set.
Syntax:-
set_name.add()
-------------
example:-
se={"ford","bmw","suzuki"}
se.add("maruthi")
print(se)
o/p:-
{'suzuki', 'maruthi', 'bmw', 'ford'}
-------------
#to concatenateone set with another we use update function
se={'suzuki', 'maruthi', 'bmw', 'ford'}
se2={'suki', 'maruti', 'bmw', 'fod'}
se2.update(se)
print(se2)
o/p:-
{'bmw', 'ford', 'maruti', 'suzuki', 'maruthi', 'suki', 'fod'}
-------------
#if we want to add value of set into list we use extend
#if we want to add value of list into set we use update
li=["mustang"]
se={'suzuki', 'maruthi', 'bmw', 'ford'}
li.extend(se)
print(li)
se.update(li)
print(se)
o/p:-
['mustang', 'bmw', 'ford', 'maruthi', 'suzuki']
{'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
-------------
Discard:-It is used to remove the element in the set.
Syntax:
Setname.discard()
se={'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
se.discard('maruthi')
print(se)
o/p:-
{'bmw', 'mustang', 'ford', 'suzuki'}
-------------
Pop:-It will remove any value in the set.
Syntax:-
set_name.pop()
example:
se={'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
se.pop()
print(se)
o/p:-
{'maruthi', 'mustang', 'suzuki', 'ford'}
-------------
Clear():- It will clear the whole set.
Syntax:-
se.clear()
-------------
se={'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
se.clear()
print(se)
o/p:-
set()
-------------
#Remove:-It removes the particular element in the set
se={'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
se.remove("suzuki")
print(se)
o/p:-
{'mustang', 'maruthi', 'bmw', 'ford'}
-------------
Del keyword is used to delete the entire se.
Syntax:
del set_name
-------------
Example:
se={'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
del se
print(se)
-------------
Frozen Set :It is used to convert the mutable set into immutable set.
Which means we cant add or remove the values in the set.For that we use 
frozenset().
Syntax:-
frozenset("set_name")
example:-
se={'mustang', 'maruthi', 'suzuki', 'bmw', 'ford'}
b=frozenset(se)
se.remove(b)
print(se)
o/p:-
Traceback (most recent call last):
  File "/home/main.py", line 1049, in <module>
    se.remove(b)
KeyError: frozenset({'suzuki', 'maruthi', 'ford', 'bmw', 'mustang'})
-------------
#convert set to list
a={"a","b","c"}
b=list(a)
print(b)
o/p:-
['a', 'c', 'b']
-------------
a={"a","b","c"}
b={1,2,3}
c=a | b
print(c)
output:
{'a', 1, 2, 3, 'c', 'b'}
-------------
a={"a","b","c"}
b={1,2,3}
c=a.union(b)
print(c)
output:
{1, 2, 3, 'a', 'b', 'c'}
-------------
a={"a","b","c"}
b={1,2,3}
e={1,2,3,"r"}
c=a.union(b,e)
print(c)
output:
{1, 2, 3, 'c', 'b', 'a', 'r'}
-------------
b={1,2,3}
e={1,2,3,"r"}
c=b.intersection(e)
d=e&b
print(c)
output:
{1, 2, 3}
-------------
b={1,2,3}
e={1,2,3,"r"}
d=e&b
print(d)
output:
{1, 2, 3}
-------------
b={1,2,3,4,5}
e={1,2,3,"r"}
b.intersection_update(e)
print(b)
output:
{1, 2, 3}
-------------
b={1,2,3,4,5}
e={1,2,3,"r"}
c=b-e
print(e)
ouput:-
{1, 2, 3, 'r'}
-------------
b={1,2,3,4,5}
e={1,2,3,"r"}
b.difference_update(e)
print(b)
ouput:
{4, 5}
-------------
b={1,2,3,4,5}
e={1,2,3,"r"}
k=b.symmetric_difference(e)
print(k)
output:
{'r', 4, 5}
-------------
-------------
b={1,2,3,4,5}
e={1,2,3,"r"}
k=b^e#symmetric_difference
print(k)
output:
{4, 5, 'r'}
-------------
b={1,2,3,4,5}
e={1,2,3,"r"}
b.symmetric_difference_update(e)
print(b)
output:
{4, 5, 'r'}
-------------
#sorted is used to sort the set by converting set into the list
a={"1","e","f"}
li=sorted(a)
print(li)
output:
['1', 'e', 'f']
-------------
a=['1', 'e', 'f']
li=sorted(a)
print(" ".join(li))
output:
1 e f
-------------
Dicitionary:- It is used to store the value in the form of key and value pairs.
It stores the value in ordered manner it is changeable and it doesnt allow duplicate 
keys.It allow duplicate values.
Syntax:-
Dictionary_name={key: values,key: values}
-------------
Example:
dic={1:"name",2:"age"}
print(dic)
o/p:-
{1: 'name', 2: 'age'}
-------------
dic={1:"name",2:"age",2:"Height"}
print(dic)
o/p:
{1: 'name', 2: 'Height'}
-------------
dic={1:"name",2:"age",2:"Height"}
print(len(dic))
o/p:-
2
-------------
dic={1:"name",2:["Height","Weight"]}
print(dic)
o/p:-
{1: 'name', 2: ['Height', 'Weight']}
-------------
dic={1:"name",2:["Height","Weight"]}
print(type(dic))
o/p:-
<class 'dict'>
-------------
dic={1:"name",2:["Height","Weight"]}
dic["age"]=19
print(dic)
o/p:-
{1: 'name', 2: ['Height', 'Weight'], 'age': 19}
-------------
#accept values from user into Dictionary
n=int(input())
dic={}
for i in range(n):
    key=int(input())
    val=input()
    dic[key]=val
print(dic)
o/p:-
2
2
nithin
1
b
{2: 'nithin', 1: 'b'}
-------------
d1={1:"a",2:"b",3:"c:"}
d2={4:4,5:5,6:6}
d1.update(d2)
print(d1)
o/p:-
{1: 'a', 2: 'b', 3: 'c:', 4: 4, 5: 5, 6: 6}
-------------
d1={1:"a",2:"b",3:"c:"}
d2={4:4,5:5,6:6}
d3=d1|d2
print(d3)
o/p:
{1: 'a', 2: 'b', 3: 'c:', 4: 4, 5: 5, 6: 6}
-------------
d1={1:"a",2:"b",3:"c:"}
d2={4:4,5:5,6:6}
d3={**d1,**d2}
print(d3)
o/p:
{1: 'a', 2: 'b', 3: 'c:', 4: 4, 5: 5, 6: 6}
---------
d1={1:"a",2:"b",3:"c:"}
print(d1[1])
o/p:
a
---------
d1={1:"a",2:"b",3:"c"}
print(d1.get(3))
o/p:
c
---------
d1={1:"a",2:"b",3:"c"}
l=d1.keys()
print(l)
output:
dict_keys([1, 2, 3])
---------
d1={1:"a",2:"b",3:"c"}
l=d1.values()
print(l)
output:
dict_values(['a', 'b', 'c'])
---------
d1={1:"a",2:"b",3:"c"}
l=d1.values()
for i in l:
    print(i)
output:
a
b
c
---------
items():
d1={1:"a",2:"b",3:"c"}
item=list(d1.items())
print(item)
output:
[(1, 'a'), (2, 'b'), (3, 'c')]
---------
d1={1:"a",2:"b",3:"c"}
item=list(d1.items())
print(item[1][0])
o/p:2
---------
d1={1:"a",2:"b",3:"c"}
d1[3]="d"
print(d1)
output:
{1: 'a', 2: 'b', 3: 'd'}
---------
d1={1:"a",2:"b",3:"c"}
d1.update({3:"d"})
print(d1)
output:
{1: 'a', 2: 'b', 3: 'd'}
---------
#delete particular key value pair in dict we use pop
d1={1:"a",2:"b",3:"c"}
d1.pop(3)
print(d1)
output:
{1: 'a', 2: 'b'}
---------
#it deletes the last key in dict
d1={1:"a",2:"b",3:"c"}
d1.popitem()
print(d1)
output:
{1: 'a', 2: 'b'}
---------
d1={1:"a",2:"b",3:"c"}
del d1
print(d1)
o/p:
Traceback (most recent call last):
  File "/home/main.py", line 1304, in <module>
    print(d1)
NameError: name 'd1' is not defined
---------
#clear all the values in the dictionary
d1={1:"a",2:"b",3:"c"}
d1.clear() 
print(d1)
o/p:
{}
---------
d1={1:"a",2:"b",3:"c"}
for i in d1:
    print(i)
output:
1
2
3
---------
d1={1:"a",2:"b",3:"c"}
for i in d1.values():
    print(i)
output:
a
b
c
---------
d1={1:"a",2:"b",3:"c"}
for i in d1.items():
    print(i)
output:
(1, 'a')
(2, 'b')
(3, 'c')
---------
d1={1:"a",2:"b",3:"c"}
for x,y in d1.items():
    print(x,y)
output:
1 a
2 b
3 c
---------
d1={1:"a",2:"b",3:"c"}
d2=d1.copy()
print(d2)
output:
{1: 'a', 2: 'b', 3: 'c'}
---------
d1={1:"a",2:"b",3:"c"}
d2=d1
print(d2)
output:
{1: 'a', 2: 'b', 3: 'c'}
---------
d1={1:"a",2:"b",3:"c"}
d2=dict(d1)
print(d2)
output:
{1: 'a', 2: 'b', 3: 'c'}
---------
d1={2:"a",1:"b",3:"c"}
l=sorted(d1.keys())
print(l)
output:
[1, 2, 3]
Strings:String is a collection of chracters.In python there are inbuilt functions 
for string handling.String in python is surrounded by single or double quotes.
Syntax:-
String_variable="Value"
String_variable='value'
-------------
#to print string with quotes
s1="'hi'"
s='"hello"'
print(s)
print(s1)
output:
"hello"
'hi'
-------------
#to access elements of the string
s1="hello"
print(s1[2])
output:
l
-------------
#to print characters one by one in a string
s1="hello"
for i in s1:
 print(i)
output:
h
e
l
l
o
-------------
s="i am here"
if "am" in s:
    print("yes")
output:
yes
-------------
#slicing
s="i am here"
print(s[1:])
print(s[:1])
print(s[::-1])
output
 am here
i
ereh ma i
-------------
inp=input().lower()
k=inp[::-1]
if(inp==k):
    print("Pallindrome")
else:
    print("Not a pallindrome")
-------------
#CHECKING WHETHER THE GIVEN STRING IS A pallindrome OR NOT WITHOUT USING ANY INBUILT functions
inp=input().lower()
s=""
si=len(inp)-1
while(si>=0):
    s=s+inp[si]
    si=si-1
if(s==inp):
    print("Palindrome")
else:
    print("Not a pallindrome")
OUTPUT:
mom
Palindrome
-------------
#Modifying the STRING
s="Hello"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.swapcase())
OUTPUT:
hello
HELLO
Hello
hELLO
-------------
S="HELLO WORLD"
print(S.title())
OUTPUT:
Hello World
-------------
#to remove white spaces beginning and end of the string
s="  Hello World "
print(s.strip())
OUTPUT:
Hello World
-------------
#replacing characters
s="Hello World"
print(s.replace("l","0"))
OUTPUT:
He00o Wor0d
-------------
#removing white spacing
s="Hello World"
print(s.replace(" ",""))
OUTPUT:
HelloWorld
-------------
#splitting the string 
s="hello#world"
print(s.split("#"))
OUTPUT:
['hello', 'world']
-------------
#concating the string or combining the string
s="Ramu"
s1="Gopal"
s=s+" "+s1
print(s)
OUTPUT:
Ramu Gopal
-------------
#string formating
age=20
txt="My age is"+age
print(txt)
OUTPUT:
Traceback (most recent call last):
  File "/home/main.py", line 1492, in <module>
    txt="My age is"+age
TypeError: can only concatenate str (not "int") to str
-------------
#string formating
age=20
txt=f"My age is {age}"
print(txt)
OUTPUT:
My age is 20
-------------
#we can perfrom arithmetic operations
age=20
txt=f"My age is {age*100}"
print(txt)
Output:
My age is 2000
-------------
age=20
txt=f"I am {age*100:.2f} years old"
print(txt)
Output:
My age is 2000.00
-------------
age=20
txt=f"I am {age*100:.2f} years old"
print(txt)
Output:
I am 2000.00 years old
-------------
s="Hello world"
print("\""+s+"\"")
Output:
"Hello world"
-------------
\b-backspace
\n-newline
\t-tabspace
-------------
#center function leaves the as much spaces we want
txt="hello"
x=txt.center(10)
print(x)
output:
  hello 
-------------
txt="hello ramu"
x=txt.count("l")
y=txt.index("am")
print(x)
print(y)
output:
2
7
-------------
#check true or False
txt="hello ramu"
print(txt.startswith("hello"))
print(txt.endswith("ramu"))
print(txt.isupper())
print(txt.islower())
print(txt.isalpha())
print(txt.isnumeric())
print(txt.isalnum())
output:
True
True
False
True
False
False
False
-------------
----------------------------------------------------------------
Function: Function is a block of code only it runs when
you call it We can The passing data is known as parameters.It returns the data as returns
.There are two types of functions.
1.Inbuilt functions
2.User defined functions
Syntax:
def function_name():#def is the keyword to create a function
function body
-------------
#Function without parameter and without return value
Example:
def painter():
    print("Painting")
painter()
output:
Painting
-------------
#function with parameter without return value
def painter(msg):
    print(msg)
painter("Paint my house")
output:
Paint my house
--------------------------------------------------
#function without parameter with return value
def add():
    a=int(input())
    b=int(input())
    c=a+b
    print("Addition:",c)
def sub():
    a=int(input())
    b=int(input())
    c=a-b
    print("Subtraction:",c)
def mul():
    a=int(input())
    b=int(input())
    c=a*b
    print("Multiplication:",c)
def div():
    a=int(input())
    b=int(input())
    c=a/b
    print("Division:",c)
add()
sub()
mul()
div()
output:
10
20
Addition: 30
20
10
Subtraction: 10
100
100
Multiplication: 10000
200 
3
Division: 66.66666666666667
--------------------------------------------------
#function to chcek whether the given number is even or odd
def findoddoreven(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
n=int(input())
findoddoreven(n)
OUTPUT: 
24
Even
--------------------------------------------------
def findfailorpass(m):
    if(m>=35):
        print("Pass")
    else:
        print("Fail")
m=int(input())
findfailorpass(m)
Output:
89
Pass
--------------------------------------------------
#function to print the number range
def printrange(a,b):#parameters
    for i in range(a,b+1):
        print(i)
a=int(input("Start:"))
b=int(input("Range:"))
printrange(a,b)#arguments
Output:
Start:1
Range:10
1
2
3
4
5
6
7
8
9
10
--------------------------------------------------
Arbitary Argument: This arbitary argument is used when we dont know how many 
parameters will be passed.It will return as tuple of arguments.
Syntax:
def function_name(*parameter):
 body
--------------------------------------------------
def fun(*name):
    print(name)
fun("a","b","c")
Output:
('a', 'b', 'c')
--------------------------------------------------
#function without parameter and with return type
def add():
    a=10
    b=20
    return a+b
print(add())
Output:
30
--------------------------------------------------
#function with parameter and with return type
def add(a,b):#parameter
   #actual parameters k=a
   #formal parameters p=b
                      return k+p
print(add(10,20))#arguments 10,20
Output:
30
--------------------------------------------------
Recursion:Calling a function by itslef is called recursion.
Syntax:
def function_name():
    statements
    .
    .
    .
    funnction_name()
function_name()
--------------------------------------------------
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
def fun():
    print("Hi")
    fun()
Output:
2000
--------------------------------------------------
#recursion about factorials
def fact(n):
  if(n==0):
        return 1
  else:
        return n*fact(n-1)
print(fact(5))
Output:
120
--------------------------------------------------

****************OOPS in Python**********************
OOPS-Objected Oriented programming system.In oops everything is based only
classes and objects.
-Class is a logical entity.
-Object is a real world entity
Features of oops:
-> OOPS focuses on reusable code.
->OOPS is mainly used to solve realworld problem by creating object.
OOPS Pillars are:
1.Class
2.Object
3.Methods
4.Inheritance
5.Polymorphism
6.Encapsulation
7.Abstraction
--------------------------------------------------
1.Class:It is a blue print of an object.Class is a logical entity.
Class contains another class,methods,and varibles.
Syntax:
class class_name:
Example:
#creating a class
class goa:
    def party(self):
        print("Lets enjoy party")
    def beach(self):
        print("Lets enjoy beach")
--------------------------------------------------
2.Object:It is instance of the class.To access the function or variable that present 
in the class we need an object.
Syntax:
obj_name=class_name()
--------------------------------------------------
Example:
class goa:
    def party(self):
        print("Lets enjoy party")
    def beach(self):
        print("Lets enjoy beach")
ramesh=goa()
suresh=goa()
ramesh.party()
suresh.beach()
Output:
Lets enjoy party
Lets enjoy beach
--------------------------------------------------
Scopes of variable:
1.Local variable:If we are creating the variable inside the class
and inside the method it is known as local variable.
2.Global variable:The variable which present outside the method and inside the class
is called global variable.
--------------------------------------------------
class goa:
    drink=""
    def party(self):
        print("Lets enjoy party")
    def beach(self):
        print("Lets enjoy beach")
ramesh=goa()
suresh=goa()
ramesh.drink="yes"
suresh.drink="no"
ramesh.party()
print(ramesh.drink)
suresh.beach()
print(suresh.drink)
output:
Lets enjoy party
yes
Lets enjoy beach
no
--------------------------------------------------
#local variable demonstration
class laptop:
    def __init__(self):
        price=0
        print("hello programmer")
    def disp(self):
        print("it is display")
h=laptop()
h.price=100
print(h.price)
output:
hello programmer
100
--------------------------------------------------
#form function and creating objects for it
class form:
    nam=""
    roll=""
st1=form()
st1.nam="nithin"
st1.roll="25"
st2=form()
st2.nam="raju"
st2.roll="24"
print(st1.nam,",",st1.roll)
print(st2.nam,",",st2.roll)
output:
nithin , 25
raju , 24
--------------------------------------------------
#CREATING A CLASS LAPTOP AND PASSING THE OBJECTS
class Laptop:
    price=""
    processor=""
    Ram=""
HP=Laptop()
DELL=Laptop()
Lenovo=Laptop()
HP.price="100000"
HP.processor="I5"
HP.Ram="8GB"
DELL.price="100000"
DELL.processor="I5"
DELL.Ram="8GB"
Lenovo.price="10000"
Lenovo.processor="I8"
Lenovo.Ram="8GB"
print(HP.price,",",HP.processor,",",HP.Ram)
print(DELL.price,",",DELL.processor,",",DELL.Ram)
print(Lenovo.price,",",Lenovo.processor,",",Lenovo.Ram)
output:
100000 , I5 , 8GB
100000 , I5 , 8GB
10000 , I8 , 8GB
--------------------------------------------------
__init__ Function: It is also known as the constructor of the class.It is a built-in
function or default function which returns or executes when the object is created 
for the class it will be executed.It will be called automatically when the object
is created for a class.It is also called as the constructor.
--------------------------------------------------
class laptop:
    def __init__(self):
        print("hello programmer")
    def disp(self):
        print("it is display")
h=laptop()
output:
hello programmer
--------------------------------------------------
Uses of self keyword:
It is used to call the current object.It is same as this keyword in java
programming.
--------------------------------------------------

class laptop():
    def __init__(self):
        price=0
        ram=""
        print("Laptop details:")
    def disp(self):
        print("Price:",self.price)
        print("Ram:",self.ram)
hp=laptop()
hp.price=100000
hp.ram="8gb"
hp.disp()
dell=laptop()
dell.price=100000
dell.ram="8gb"
dell.disp()
ouput:
Laptop details:
Price: 100000
Ram: 8gb
Laptop details:
Price: 100000
Ram: 8gb   
--------------------------------------------------
class student:
    def __init__(self):
        name=""
        reg=""
    def disp(self):
        print("Name:",self.name)
        print("Registered number:",self.reg)
st1=student()
st1.name="nithin"
st1.reg=25
st1.disp()
output:
Name: nithin
Registered number: 25
--------------------------------------------------
class student:
    def __init__(self,name):
        self.na=name
st1=student("nithin")
print(st1.na)
output:
nithin
--------------------------------------------------
class student:
    def __init__(self,name):
        self.na=name
name=input()
st1=student(name)
print(st1.na)
output:
nithin 
nithin
--------------------------------------------------
Exercise problems:
--------------------------------------------------
class calculator:
    def add(self,a,b):
        print("Addition:",a+b)
    def sub(self,a,b):
        print("Subtraction:",a-b)
    def mul(self,a,b):
        print("Multiplication:",a*b)
    def div(self,a,b):
        print("Division:",a/b)
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
ob1=calculator()
ob1.add(a,b)
ob1.sub(a,b)
ob1.mul(a,b)
ob1.div(a,b)
--------------------------------------------------
output:
Enter first value:10
Enter second value:2
Addition: 12
Subtraction: 8
Multiplication: 20
Division: 5.0
--------------------------------------------------
#Example
class teacher:
    def __init__(self,name,register):
        self.na=name
        self.reg=register
    def disp(self):
        print("Name:",self.na)
        print("Registered number:",self.reg)
n1=input()
r1=input()
t1=teacher(n1,r1)
n2=input()
r2=input()
t2=teacher(n2,r2)
t1.disp()
t2.disp()
output:
raju
22
nithin 
22
Name: raju
Registered number: 22
Name: nithin
Registered number: 22
--------------------------------------------------
#Updating the object value
class student:
    def __init__(self,na,age):
       self.name=na
       self.age=age
    def disp(self):
        print("Name:",self.name)
        print("Registered number:",self.age)
st1=student("raju",99)
st1.age=100
st1.disp()
output:
Name: raju
Registered number: 100
--------------------------------------------------
#deleting object
class student:
    def __init__(self,na,age):
       self.name=na
       self.age=age
    def disp(self):
        print("Name:",self.name)
        print("Registered number:",self.age)
st1=student("raju",99)
del st1
st1.disp()
------------------------
output:
Traceback (most recent call last):
  File "/home/main.py", line 2019, in <module>
    st1.disp()
NameError: name 'st1' is not defined. Did you mean: 'str'?
--------------------------------------------------
#write your code here
class Innings:
    def __init__(self,nu,bt,ru):
        self.num=nu
        self.bt=bt
        self.ru=ru
    def dispin(self):
        print("Innings Details:\n")
        print("Innings number:",self.num)
        print("BattingTeam:",self.bt)
        print("Runs Scored:",self.ru)
class Main:
    nu=input("Enter the innings number\n")
    bt=input("Enter the BattingTeam\n")
    ru=int(input("Enter the runs scored\n"))
    ob=Innings(nu,bt,ru)
    ob.dispin()
--------------------------------------------------

Inheitance:The class acquiring the other class properties is called inheritance.
There are 5 types of inheritance.
They are:
--------------------------------------------------------------------------------
1.Single Inheritance:In this the child class inherit all the properties of the
parent class.
--------------------------------------------------
Example:
#single Inheritance
class dad:
    def dadphone(self):
        print("daD PHONE")
class son(dad):
    def soonphone(self):
        print("son phone")
s=son()
s.dadphone()
ouput:
daD PHONE
--------------------------------------------------------------------------------   
2.Multiple Inheritance:In this inheritance there will be two parent classes and
the properties of the two parent classes is inherited by the child class.
     
     parent1        parent2
        |           |
        |           |
        _____________
             |
            child
---------------------------------
Example:
#Multiple Inheritance
class dad:
    def dadphone(self):
        print("daD PHONE")
class mom:
    def momphone(self):
        print("mom phone")
class son(dad,mom):
    def soonphone(self):
        print("son phone")
s=son()
s.dadphone()
s.momphone()
ouput:
daD PHONE
mom phone  
--------------------------------------------------------------------------------
3.Multilevel Inheritance: The child inherits the properties of both the parent and 
as well as the Grandparent. 

                    Grandparent class
                          |
                          |
                      Parent class
                          |
                          |
                       Child class 
---------------------------------------
Example:
#Multilevel Inheritance
class Grandparent:
    def Grandparentphone(self):
        print("Grandparent PHONE")
class dad(Grandparent):
    def dad(self):
        print("dad phone")
class son(dad):
    def sonphone(self):
        print("son phone")
s=son()
s.Grandparentphone()
ouput:
Grandparent PHONE
--------------------------------------------------------------------------------
4.Hierarchial Inheritance:Two or more child classes acquires the properties of 
class.


                          Parent
                            |
                      ______________ 
                     |      |       |
                  child1  child2  child3
--------------------------------------------------
Example:
#Hierarchial Inheritance
class dad():
    def dadphone(self):
        print("dad phone")
class son(dad):
    def sonphone(self):
        print("son phone")
class son2(dad):
    def sonphone(self):
        print("son phone")
class son3(dad):
    def sonphone(self):
        print("son phone")
s=son()
s2=son2()
s3=son3()
s.dadphone()
s2.dadphone()
s3.dadphone()
Output:
dad phone
dad phone
dad phone
--------------------------------------------------------------------------------
5.Hybrid Inheritance:
It is a combination of single,multiple,hierarchial or multilevel inheritance is 
called Hybrid Inheritance.
                Grand Parent 1            Grand Parent2
                     |                          |
                     ----------------------------
                                   |
                                 parent
                                   |
                     ----------------------------
                    |                           |
                  child1                      child2
-----------------------------------------------------------------
Example:
#Hybrid inheritance
class gp1():
    def gp1(self):
        print("gp1")
class gp2():
    def gp2(self):
        print("gp2")
class parent(gp1,gp2):
    def parent(self):
        print("parent")
class son1(parent):
    def sonphone(self):
        print("son phone")
class son2(parent):
    def sonphone(self):
        print("son phone")
ob=parent()
ob.gp1()
ob.gp2()
ob2=son2()
ob2.gp1()
ob2.gp2()
Output:
gp1
gp2
gp1
gp2
--------------------------------------------------------------------------------

Super():It is used to call the method in the parent class.By using super ()
we can acces the functions,variables in the parent class.
--------------------------------------------------------------------------------
Example:
#demonstrating the super keyword
class A:
    def __init__(self):
        print("A")
    def disp(self):
        print("class a")
class B(A):
    def __init__(self):
        super().__init__()
        super().disp()
        print("B")
b=B()
ouput:
A
class a
B
--------------------------------------------------------------------------------
                                Polymorphism
Polymorphism: It is a greek word which means poly menas many and morphism means 
forms.Single action performed in many ways is known as Polymorphism.
In programming Polymorphism means the same function is being used to different types.
--------------------------------------------------------------------------------
example:
A person is the example for Polymorphism.Single person performing many roles.
--------------------------------------------------------------------------------
There are four types of Polymorphism:
1.Operator Over loading 
2.Class Polymorphism
3.Compile time Polymorphism(method overloading)
4.Run Time Polymorphism(method overriding)
--------------------------------------------------------------------------------
1.Operator Over loading :
Operator overloading is a type of Polymorphism in which the same operator perfrom
various operation based on the operands.
----------------------------
Example:
#demonstration of operator overloading
a="GOPAL"
b="Kumar"
c=a+b
k=10
z=1010
t=k+z
print(c)
print(t)
example:
GOPALKumar
1020
--------------------------------------------------------------------------------
Function Over loading:
----------------------------
a="Gates"
b=[1,2,3]
print(len(a))
print(len(b))
Output:
5
3
----------------------------
2.Class Polymorphism: It is a type of Polymorphism in which two or more classes
having same method name. As we have same method name for both classes.So we can 
print both classes methods at a single time by using for loop.
----------------------------
Example: 
#Demonstrating Class Polymorphism
class Tiger:
     def name(self):
         print("I am tiger")
     def color(self):
         print("Orange")
class Elephant:
     def name(self):
         print("I am Elephant")
     def color(self):
         print("Grayish black")
ob1=Tiger()
ob2=Elephant()
for i in (ob1,ob2):
    i.name()
    i.color()
Output:     
I am tiger
Orange
I am Elephant
Grayish black
----------------------------
3.Compile time Polymorphism(method overloading):A single class which have two or
more method with same name but different in number of parameter or different in
datatype.Basically method overloading will not supported by python. If there are
multiple methods with same name the method which you have gave last will be 
overided by the earlier one.
----------------------------
Example:
#Demonstrating Method overloading in python which is not possible
class calc:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
c=calc()
c.add(1,2)
Output:
Traceback (most recent call last):
  File "/home/main.py", line 2302, in <module>
    c.add(1,2)
TypeError: calc.add() missing 1 required positional argument: 'c'
----------------------------
4.Run Time Polymorphism(method overriding):Usually method overriding is associated 
with inheritance.Method overriding means two different classes have same method name
with same number of parameter.
Example:
#Demonstrating Method overriding
class A:
    def display(self):
        print("HI this is A")
class B(A):
    def display(self):
        print("Hi this is B")
ob=B()
ob.display()
Output:
Hi this is B
----------------------------
Access modifiers: Access modifiers are used to restrict the variable and method 
in the class. Access modifier in python have an Important role in securing the data 
from unauthorised access.In python we use "_" to determine the access modifier.
Typed of accessmodifier:
1.Public- variable
2.Private(__variable)
3.Protected(_variable)
----------------------------
1.Public : The variable or function which is declared as public can able to access
any part of the program.By default all the variables and function in the python
are public.
----------------------------
#demonstrating the public 
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:"+self.name)
        print("Age:",self.age)
ob=student("nithin",9)
ob.display()
Output:
Name:nithin
Age: 9
--------------------------------------------------------------------------------
2.Private:I f we declare any function or variable as private then the particular 
function and variable can able to access those variables and function only in 
the particular class.
--------------------------------------------------------------------------------
#demonstrating the private and accessing the private method 
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __display(self):
        print("Name:"+self.name)
        print("Age:",self.age)
    def dis(self):
        self.__display()
ob=student("nithin",9)
ob.dis()
Output:
Name:nithin
Age: 9
--------------------------------------------------------------------------------
3.Protected:The members of a class that are declared as a protected can able to 
access inside the class and inside the package and in the sub classes.Not outside 
the package.As per the statement we can able to use the protected method only in
c++ and java.Beacuse in python the concept is looser.The use of single underscore 
is the way of indicating the variable is for internal use but it is not truely
protecting in the sense of access restriction.
--------------------------------------------------------------------------------
example:
class student:
    _name="kethu"
stu=student()
print(stu._name)
output:
kethu
--------------------------------------------------------------------------------
                                Encapsulation
Encapsulation:-Encapsulation means wrapping the data and coding into a single unit.
It is used to put the restriction on accessing the variable and method directly.
And it can prevent the accidental modification of the data.To achieve encapsulation
we need to create all the variables as the private.To access those private variables
we need to use two methods.
1.Setter methods:-It is used to set the value for the private variable.
2.Getter methods:-It is used to get the setted value.
--------------------------------------------------------------------------------
# demonstrating encapsulation
class details:
    __name=""
    __regno=0
    __dept=""
    def setter(self,name,regno,dept):
        self.__name=name
        self.__regno=regno
        self.__dept=dept
    def getter(self):
       print(self.__name) 
       print(self.__regno)
       print(self.__dept)
    
obj=details()
obj.setter("kesav",123,"CSD")
obj.getter()
output:
kesav
123
CSD
--------------------------------------------------------------------------------
Abstraction:Hiding the uneccessary details and showing the functionality and essential
detail.In python the abstraction is achieved by using abstrect class and abstract
method Abstract class cant able to access directly by creating the object.It is 
used as base class for another class.Abstract class must need one abstract method
with multiple non abstract methods.
Abstract Method:
Abstract method is declared inside the abstract class but it doesnot have any body.
Subclass must override the abstract method.

-Python provides Abc module to define abstract class and abstract method.You need 
to use abc class to create abstract class and abstract  method.
--------------------------------------------------------------------------------
#abstraction implementation
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep(self):
        print("This animal is sleeping")
class Lion(Animal):
    def sound(self):
        print("roar")
class cat(Animal):
    def sound(self):
        print("meow")
a=Lion()
a.sound()
output:
roar
--------------------------------------------------------------------------------
*******************************Data Structures**********************************
Data strcture is used to organise the data.We have to types of data structures 
they are 
1:Linear strcture
2:Non linear structure
->Array stores the value in a continuous manner.
->Linkedlist stores randomly but it have link to it.
Linkedlist:The data in the linked list are linked eeach other by using pointer.
The linked list contain nodes and each node contain data and pointer.If we take C
programming we have pointer but in other oop we dont have pointer instead we have 
address.
->Linkedlist must contain head and the head is used to store the address of the 
first node.

Flexibility,Insertion,and deletion is easier that memory efficient.
--------------------------------------------------------------------------------
#demonstrating the creation of a node 
class node:
    data=None
    next=None
    def __init__(self,data):
      self.data=data
      self.next=None
n1=node(1)
print(n1.data)
print(n1)
n2=node(2)
print(n2.data)
output:
1
<__main__.node object at 0x7d5810758370>
2
--------------------------------------------------------------------------------
'''
#Implementing linked list insert at the beginning
class node:
    def __init__(self,data):
      self.data=data
      self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def inserAtBegin(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node.next
        else:
            new_node.next=self.head
            self.head=new_node
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
LL=Linkedlist()
LL.inserAtBegin(1)
LL.inserAtBegin(2)
LL.display()












































































































































































































































































































































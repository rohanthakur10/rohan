#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter the year"))
if(year%4==0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")

#Take length and breadth input from user and check whether the dimensions are of square or rectangle.
length=int(input("Enter length"))
breadth=int(input( "Enter breadth"))
if length==breadth:
  print (" square")
else:
  print (" Rectangle")
				  
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("Enter first age"))
b=int(input("Enter second age"))
c=int (input("enter third age"))
if a>=b and a>=c:
  print("Oldest is",a)
elif b>=a and b>=c:
  print("Oldest is",b)
elif c>=a and c>=b:
  print("Oldest is",c)
else:
  print("All are equal")
#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR".
age=int(input("Enter age"))
sex=input( "SEX? (M or F)")
marry=input("MARRIED? (Y or N)")
if sex == "F":
  print("Urban areas only")
elif sex == "M" and age>=20 and age<=40:
  print("You can work anywhere")
elif sex == "M" and age>40 and age<=60:
  print("Urban areas only")
else:
  print("ERROR")
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity=input("Enter quantity")
if quantity*100>1000:
    print("Cost is",((quantity*100)-(.1*quantity*100)))
else:
    print ("Cost is",quantity*100)

#loops
#Q.1- Take 10 integers from user and print it on screen. 

sum = 0
i = 10
while i>0:
  num=int(input("Enter number"))
  sum = sum + num
  i = i-1
print("average is",sum/10.0)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while True:
  print("INFINITE")
#Q.3-Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
m=list(map(int.input().split()))
m_square=[]
for i in 1:
    m_square.append(i**2)
print(m_square)
print('-'*50)

# Q.4- From a list containing ints, strings and floats, make three lists to store them separately 
my_list=[3,7,a,k,l,d,9.8,6.7]
from collections import defaultdict
r=deafaultdict(list)
for x in my_list:
    r[type(x)].append(x).append(x)

print(r[int])
print(r[str])
print(r[float])
#Q.5- Using range(1,101), make a list containing only prime numbers.
for i in range(1,101):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
    if not flag:
        num.append(i)
print(num)
#Q.6- Print the following patterns: 
#* 
#** 
#*** 
#****
def printIncreasing(symbol,n):
    count=1
    while count<=n:
        print(symbol*count)
        count=count+1
    return
printIncreasing('*',4)
#7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
a=list(map(int.input("enter the elements").split()))
element=int(input("enter the element to search"))
if element in a:
    print("element found")
    del.1[a.index(element)]
    print(a)

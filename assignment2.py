#list
#Q.1- Create a list with user defined inputs
lst=list(input().split())
print(lst)

#Q.2- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
lst2=lst+['java','python','perl','php','php','c']
print(lst2) 

#Q.3 - Count the number of time an object occurs in a list.
print(lst2.count('php'))

#Q.4 - create a list with numbers and sort it in ascending order.
lst1=[12,15,44,57,9,2,13]
lst1.sort()
print(lst1)
#Q.5 Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
a=[3,95,47,89,65]
b=[12,54,63,18,20]
c=a+b
c.sort()
print(c)

#Q.6 - Count even and odd numbers in that list.
lst3=[1,15,44,7,9,12]
no_even=0
no_odd=0
for i in lst3:
    if i%2==0:
        no_even +=1
    else:
        no_odd +=1
print('count of even numbers:'+str(no_even))
print('count of odd numbers:'+str(no_odd))

#tuples
#Q.1-Print a tuple in reverse order.
tup1=(2,5,16,10,8)
print(tup1[::-1])

#Q.2-Find largest and smallest elements of a tuples.
tup2=(11,10,67,35,22)
print('largest:',max(tup2),"smallest",min(tup2))

#Strings
#Q.1- Convert a string to uppercase.
x="hello python"
x=x.upper()
print(x)

#Q.2- Print true if the string contains all numeric characters.
y="567827"
print(y.isnumeric())

#Q.3- Replace the word "World" with your name in the string "Hello World".
z="hello world"
z=z.replace("world","Rohan")
print(z)




#Q.1- Reverse the whole list using list methods.
lst=[11,22,33,'microsoft','computer','c',62]
lst.reverse()
print(lst)
#Q.2- Print all the uppercase letters from a string.
s="My Name is Rohan"
for i in s:
    if i==i.upper():
        print(i,end="|")

#Q.3- Split the user input on comma's and store the values in a list as integers.
lst3=list(map(int,input("\nenter the elements").split(",")))
print(*lst3)

#Q.4- Check whether a string is palindrome or not.
a="computer"
if a[::-1]==a:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
#shallo copy
a=[10,20,30]
b=a
print("original list:",a,"id=",id(a))
print("shallow copylist:",b,"id=",id(b))
#deep copy
c=a.copy()
print("original list",a,"id=",id(a))
print("deep copy list",c,"id=",id(c))

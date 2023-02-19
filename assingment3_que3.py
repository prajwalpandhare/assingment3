a=input("enter the string")
u=0
l=0
for i in a:
    if a.isupper():
        u=u+1
    elif a.islower():
        l=l+1
print("The number of upper case letter",u) 
print("The number of lower case letter",l)
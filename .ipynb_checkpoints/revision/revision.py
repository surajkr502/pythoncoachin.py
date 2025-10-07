# import keyword
# x=keyword.kwlist
# print(len(x))
# import string
# punctuators=string.punctuation
# print("punctuators=",punctuators)


# x,y,z="suraj","niraj","saroj"
# print(x)
# print(y)
# print(z)


# city={"bhopal","ranchi","jabalpur"}
# x=y=z=city
# print(x)
# print(y)
# print(z)



# my_range = range(1,11,-1) 
# print(list(my_range))

# import my_module
# print(my_module.greet("suraj"))
# print(my_module.pi_value)



# floor division 
# print(10/3)
# print(10//3)
# print(7.5//2)
# print(-10/3)
# print(-10//3)


# find greater no. 
# x=int(input("enter any no.:"))
# y=int(input("enter any no.:"))
# z=int(input("enter any no.:"))
# if x>y:
#     if x>z:
#         print("Greater no. is x")
#     else:
#         print("Greater no. is z")
# else:
#     if y>z:
#         print("Greater no. is y")
#     else:
#         print("Greater no. is z")


# range 

# x=int(input("enter a no.:"))
# while x<=5:
#     print(x)
#     x+=1

# x=int(input("enter a no.:"))
# while x<=5:
#     if x<5:
#         print(x,end=",")
#     else:
#         print(x,end=" ")
#     x+=1

# while loop 

# print n natural no.
# num=int(input("enter natural no.:"))
# i=0
# while i<=num:
#     if i!=num:
#         print(i,end=",")
#     else:
#         print(i,end="")
#     i+=1


# for loop

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# n=int(input("enter a no.:"))
# for i in range(1,n+1):
#     char='A'
#     for j in range(1,i+1):
#         print(char,end='')
#         char=chr(ord(char)+1)
#     print()


# n=int(input("enter a no.:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(2*j,end='')
#     print()

# n=int(input("enter a no.:"))
# for i in range(1,n+1):
#     print('*'*i)

# n=int(input("enter no. of rows:"))
# for i in range(1,n+1):
#     print(' '*(n-i),'* '*i)

n=int(input("enter row count:"))
for i in range(1,n+1):
    print(" "*(n-i),'*'*(2*i-1))

# #1.Factorial using nested function

# def fact(n):
#
#     def inner_fact():
#         f = 1
#         if n==0:
#             return 1
#         else:
#             for i in range(1,n+1):
#                 f=f*i
#             return f
#     return inner_fact()
#
# n=int(input("Enter the num : "))
# print("Factorial of ",n,"is",fact(n))

# #2.Sum of 2 num
# def num1(x):
#   def num2(y):
#     return x + y
#   return num2
#
# print(num1(10)(5))

# #3 concatenating 2 strings  by taking input from user
# def greet(first, last):
#     def FullName():
#         return (first + " " + last)
#
#     print("Hi, " ,FullName() , "Have a fun filled day!")
# first=input("Enter the first name : ")
# last=input("Enter the last name : ")
# greet(first,last)


# #4.wap to show inner function is able to access variables which are available in the outer function.

# def num1(x):
#    def num2(y):
#       return x * y
#    return num2
# res = num1(10)
# print(res(5))
# print(num1(5)(2))

# #5.To find exponent of a num
# def generate_power(exponent):
#     def power(n):
#         return n ** exponent
#     return power
# res=generate_power(2)
# print("3 raise to 2 is: ",res(3))
# p_3=generate_power(3)
# print("2 raise to 3 is: ",p_3(2))
# print(generate_power(3)(2))


#6.importance of variable intializAtion inside nested functions
def fun1(a):
    x=2
    def fun2():
        x=3
        print("Inside inner func x value is :",x+a)
    print("Inside outer func x value is :",x)
    return fun2()
fun1(3)

#7.Factorial
def fact(n):
    if n<=0:return (print("Enter a positive num"))
    def inner():
        p=1
        for i in range(1,n+1):
            p=p*i
        return p
    return inner()
print(fact(2))




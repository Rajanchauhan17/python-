
userName="Rajan"

# def func():
    # global userName
#     userName="rahul"
#     print(userName)
    
    
# print(userName)
# func()

x=99
# def func2(y):
#     z=x+y
#     return z
    
    
# result=func2(5)
# print(result)

# def func3():
#     global x
#     x=5

       
# func3()  
# print(x)    
    

# def f1():
#     x=88
#     def f2():
#         print(x) #bag theory or closure bhe khete hai jb hm kisi fun ke andar ke fun ko return karte h aur jb hm return karte h tb fun m use ho rhe variable  ke variable ka reference bhi rheta h
#     return f2
# # f1()   


# result=f1()

# result()

# print(x)
# f1()

# closure aur factory function
def chaicoder(num):
    
    def actual(x):
        return x**num          #Closure = a function that remembers variables from its outer scope even after that scope has finished execution.
    return actual

f=chaicoder(2)  #this is used to find square 
g=chaicoder(3)  #this is used to find cube 

print(f(3))
print(g(3))


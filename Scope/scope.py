
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
gi
def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f=chaicoder(2)
g=chaicoder(3)

print(f)
print(g)

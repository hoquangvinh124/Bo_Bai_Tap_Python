#Bai tap 99
def fibonacci(n):
   fn1 = 1
   fn2 = 1
   for i in range(2,n):
       fn = fn1 + fn2
       fn2 = fn1
       fn1 = fn
   return fn1


def listfibo(n):
 for i in range(1,n+1):
    print(fibonacci(i),end='\t')


print(fibonacci(10))


listfibo(14)

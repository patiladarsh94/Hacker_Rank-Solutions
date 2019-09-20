#Fibonacci series : To print n fibonacci numbers
 
def fibonacci(n):
    fib1,fib2=0,1
    for i in range (n):
        print(fib1,end=" ")
        temp=fib1+fib2
        fib1=fib2
        fib2=temp
        
fibonacci(10)


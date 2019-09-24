#Fibonacci series : To print n fibonacci numbers
 
#Using loops
def fibonacci(n):
    fib1,fib2=0,1
    for i in range (n):
        print(fib1,end=" ")
        temp=fib1+fib2
        fib1=fib2
        fib2=temp
        
fibonacci(10)


#Using recurssion
def fibonacci(n):
	if n<=1:
		return n
	else:
		return (fibonacci(n-1)+fibonacci(n-2))
nterms=int(input("Enter the no. of terms in series :"))
for i in range (nterms):
	print(fibonacci(i))


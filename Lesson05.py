#Fibonacci
a = 100

def fibo(n,d):
    ''' Inputs: 1: nth Fibonacci Number to determined
                2: Initial Fibonacci Number
        Output: Returns nth Fibonacci Number'''
    if n in d:
        return d[n]
    else:
        fib = fibo(n-1,d) + fibo(n-2,d)
        d[n] = fib
        return fib


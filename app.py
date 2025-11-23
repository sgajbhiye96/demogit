def even_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
    
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            next_fib = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_fib)
        return fib_seq
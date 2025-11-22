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
    

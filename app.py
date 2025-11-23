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

def prime_check(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  
print("done")

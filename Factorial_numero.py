def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial (n-1)
    
#ejemplo
num = 5
print (f"el factorial de {num} es : {factorial (num)}")
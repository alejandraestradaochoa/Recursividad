def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
#ejemplo 
num = 10 
print (f"el termino {num} de la serie fibonacci es: {fibonacci(num)}")
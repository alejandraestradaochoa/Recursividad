def contador_digitos (n):
    if n < 10:
        return 1
    return 1 + contador_digitos(n // 10)

#ejemplo
num = 48372857625
print (f"La cantidad de digitos es : {contador_digitos(num)}")
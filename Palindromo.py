def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

#ejemplo
palabra1 = "radar"
palabra2 = "python"
print(f"¿Es 'radar' un palindromo? {palindromo(palabra1)}" )
print(f"¿Es 'python' un palindromo? {palindromo(palabra2)}")


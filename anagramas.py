
def generar_anagramas(palabra, prefijo=""):
    if len(palabra) == 0:
        return [prefijo]
    
    anagramas = []
    for i in range(len(palabra)):
        nueva_palabra = palabra [:i] + palabra [i+1:]
        anagramas.extend(generar_anagramas(nueva_palabra, prefijo + palabra[i]))

    return anagramas
    
#ejemplo
entrada = "abc"
resultado = generar_anagramas(entrada)
print (resultado)


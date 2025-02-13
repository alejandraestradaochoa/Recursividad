def hanoi(n, origen, aux, final):
    if n == 1:
        print  (f"mover disco 1 de {origen} a {final}")
        return
    
    hanoi(n-1, origen, final, aux)
    print(f"Mover disco {n} de {origen} a {final}")
    hanoi(n-1, aux, origen, final)

#ejemplo
n = 4 
hanoi(n, 'A', 'B','C')
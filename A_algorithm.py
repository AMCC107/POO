def maximovalor(A):
    count_for=0
    count_if=0 
    maxval = A[0]  # Inicializar maxval con el primer elemento de la lista
    for i in range(len(A)):
        count_for+=1
        if A[i] > maxval:
            count_if+=1
            maxval = A[i]  # Actualizar maxval si el elemento actual es mayor
    print(f"Iteraciones del ciclo for: {count_for}")
    print(f"Condición if evaluada como verdadera: {count_if}")
    return maxval
B = [0, 1, 2, 3, 4, 5]
print(maximovalor(B))  # Esto imprimirá 5, que es el valor máximo
class Sort():
    def BubbleSort(self, lista):
        n = len(lista)
<<<<<<< HEAD
=======
        i = 0
>>>>>>> 908be912e2f06a2db1dbef498019d1ccf5675100
        for i in range(1, n):
            for j in range(n-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
<<<<<<< HEAD
        return lista
=======
        return lista 
        
>>>>>>> 908be912e2f06a2db1dbef498019d1ccf5675100

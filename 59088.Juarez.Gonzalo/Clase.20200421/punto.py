class Punto2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def mostrar_coordenadas(self):
        print("Coordenadas (" + str(self.x) + ", " + str(self.y) + ")")

if __name__ == "__main__":
    punto = Punto2D()
    otro_punto = Punto2D(3, 4)
    punto.mostrar_coordenadas()
    otro_punto.mostrar_coordenadas()
print(" ")
print(" ")

class Punto2D(): 
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d,%s)" % (self.x, self.y)

if __name__ == "__main__":

    p1 = Punto2D(1,2)
    print(p1)

    p2 = Punto2D(3,4)
    print(p2)    



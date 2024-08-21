class Papeleria:

    def __init__(self,color,genero):

        self.color=color
        self.genero=genero

librohist=Papeleria("Libro Amarillo", "Historia")
libroRoman=Papeleria("Libro Rojo", "Romance")

print(type(librohist))
print(type(libroRoman))

print(librohist.color, librohist.genero)
print(libroRoman.color, libroRoman.genero)
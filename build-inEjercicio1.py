# Pedimos al usuario que escriba los paises separados por comas
paises = input("escribe una lista de paises separados por coma:")
lista_paises = list(set(paises.split(","))) #agregamos los paises separados por comas y certificamos que no se repiten
# set lo transforma en un conjunto la cual no permite duplicado
# list transforma el conjunto en una lista
#split para dividir la cadena de entrada en una lista mediante la ","
lista_paises.sort() # los ordena de manera alfabetica
lista_paises = " ,".join(lista_paises) #join() toma una lista de strings y devuelve un string único que contiene todos los elementos de la lista unidos por el separador especificado.
print(lista_paises)

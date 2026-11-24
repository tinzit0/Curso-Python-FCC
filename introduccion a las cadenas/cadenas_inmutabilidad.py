#una cadena es una secuencia de caracteres rodeada por comillas simples o dobles
#Python trata ambas formas como cadenas, asi que puedes usar cualquiera de las dos
#ejemplo
my_str_1 = 'hello'
my_str_2 = "world"

#si necesitas una cadena multilinea, puedes usar comillas dobles triples o comillas simples triples
my_str_3 = """Multiline string"""
my_str_4 = '''Another multiline string'''

#si tu cadena contiene comillas simples o dobles, entonces dos opciones:
#usar el tipo compuesto de comillas dobles para envoler la cadena, y viceversa

msg_1 = "it's a sunny day"
quote_1 = 'she said, "Hello World!"'

#escapa la comilla simple o doble en la cadena con una barra invertida(\). Con este metodo
#puedes usar comillas simples o dobles para envolver la cadena en si:

msg_2 = 'it\'s a sunny day'
quote_2 = "she said, \"hello!\""
#la barra invertida tambien puede combinarse con otros caracteres
#para representar caracteres que son dificiles de escribir directamente en una cadena.
#estas combinaciones se llaman secuencias de escape. aqui tienes algunas comunes
#\n: un salto de linea , \t: una tabulacion, \\: una sola barra invertida

#A veces puede que se necesite verificar si una cadena contiene uno o mas caracteres.
#Para eso, python proporciona el operador in, que devuelve un booleano que especifica si el caracter o
#los caracteres existen en la cadena o no.
my_str_5 = 'Hello World'
#print('hey' in my_str_5) #False
#print('Hi' in my_str_5) #False
#print('e' in my_str_5) #True
#print('f' in my_str_5) #False

#para obtener la longitud de una cadena y trabajar con los caracteres individuales en una cadena,
#un proceso llamado indexacion. para obtener la longitud de una cadenam puedes usar la funcion integrada len().
my_str_6 = 'hello world'
#print(len(my_str_6)) #11

#cada caracter en una cadena tiene una posicion llamada indice.
#el indice es cero basado, lo que significa que el indice del primer caracter de una cadena es 0,
#el indice del segundo caracter es 1, y asi sucesivamente. Para acceder a un caracter por su indice, usas corchetes ([])
#con el indice del caracter que deseas acceder dentro.
my_str_7 = "Hello World"
#print(my_str_7[0]) #H
#print(my_str_7[6]) #W

#la indexacion negativa, sirve para empezar de atras hacia adelante
my_str_8 = 'hello world'
#print(my_str_8[-1]) # d
#print(my_str_8[-5]) #w

#Un valor mutable puede cambiarse de ser creado, mientras que un valor inmutable no puede
#puedes apuntar una variable a un nuevo valor, lo que se llama reasignacion,
#pero no puedes cambiar un valor inmutable agregado, eliminado o reemplazando alguno de sus elementos

#las cadenas son inmutables en python, pero aun puedes reasignar una variable a una cadena diferente

greeting = 'hello'
#print(greeting) #hello

#pero no se permite la modificacion directa de una cadena
#greeting_2 = 'hi'
#greeting_2[0] = 'h'
#los enteros, los floats y los booleanos tambien son inmutables

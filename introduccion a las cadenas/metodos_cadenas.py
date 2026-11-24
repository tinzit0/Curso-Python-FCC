#Un metodo es una funcion que llamas sobre un valor.
#Para llamar a un metodo de cadena, escribe la cadena o el nombre de su variable.
# seguido de un punto y la llamada al metodo. aprenderas mas sobre metodos cuando estudiemos clases y objetos.
#Aqui algunos metodos comunes
my_str = 'Hello World'
uppercase_my_str = my_str.upper()
print(uppercase_my_str) #HELLO WORLD

#lower(): devuelve una nueva cadena con todos los caracteres convertidos a minuscula

lowercase_my_str = my_str.lower()
print(lowercase_my_str) #hello world

#strip(): devuelve una cadena con los caracteres especificados de inicio y final eliminados.
#si no se pasa ningun argumento, elimina los espacios en blanco de inicio y final.

my_str = ' Hello World  '
trimmed_my_str = my_str.strip()
print(trimmed_my_str)#Hello World

#replace(old, new): devuelve una nueva cadena con todas las ocurrencias de old reemplazadas por new.
my_str = 'Hello World'
replaced_my_str = my_str.replace('Hello', 'Hi')
print(replaced_my_str)#hi World

#split(separator): divide una cadena en un separador especificado en una lista de cadenas.
#Una lista agrupa valores entre corchetes.Si no especifica un separador, split() divide en espacios en blancos
#ejemplo

my_str = 'Hello World'
split_words = my_str.split()
print(split_words) # ['Hello', 'World']

#join(): Une las cadenas en una coleccion en una sola cadena con un separador.
my_list = ['Hello', 'World']
joined_my_str = ' '.join(my_list)
print(joined_my_str) # hello world

#startswith(prefix): devuelve un booleano que indica si una cadena comienza con el prefijo especificado

my_str = 'hello world'
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello) # True

#endswith(suffix): Devuelve un booleano que indica si una cadena termina con el sufijo especificado
my_str = 'hello world'
ends_with_hello = my_str.endswith('world')
print(ends_with_hello) #world

#find(substring): devuelve el indice de la primera ocurrencia de substring, o -1 si no la encuentra.
my_str = 'hello world'
world_index = my_str.find('world')
print(world_index) # 6

#count(substring): devuelve el numero de ocurrencias no superpuestas de una cadena en una cadena
my_str = 'hello world'
o_count = my_str.count('o')
print(o_count) # 2

#captilize(): devuelve una nueva cadena con el primer caracter en mayuscula y los demas caracteres en minuscula
my_str = 'hello World'
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str) #Hello world

#isupper(): devuelve True si la cadena contiene al menos un caracter con distincion de mayusculas y todas las letras con
#distincion estan mayusculas. De lo contrario, devuelve false
my_str = 'hello world'
is_all_upper = my_str.isupper()
print(is_all_upper) #False

#islower(): Devuelve True si la cadena contiene al menos un caracter con distincion de minusculas y todas las letras con distincion estan en minusculas. de lo contrario, devuelve false
my_str = 'hello world'
is_all_lower = my_str.islower()
print(is_all_lower) #True

#titlle(): devielve una cadena con la primera letra de cada palabra en
#mayusculas y las letras restantes en minusculas
my_str = 'hello world'
title_case_my_str = my_str.title()
print(title_case_my_str) #Hello World


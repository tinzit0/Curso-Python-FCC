#lecciones anteriores aprendimos a
my_str = "hello world"
print(my_str[0])#h
print(my_str[3])#l
print(my_str[-1]) #d

#el corte de cadenas permite extraer una porcion de una cadena o trabajar solo con una parte especifica de ella
#string[start:stop]
my_str = "hello world"
print(my_str[1:7]) #ello w
#el indice stop no es inclusivo, por lo que [1:4] solo extrae
#los caracteres desde el indice 1, y hasta, pero sin incluir el caracter en el indice 4

#tambien se puede omitir los indices de start y stop, Python tomara predeterminadamante 0
#o el final de la cadena, respectivamente.
#Por ejemplo, esto es lo que ocurre si omites el indice start

my_str = 'Hello World'
print(my_str[:7])#hello w
#esto extrae #lodo desde el indice 0 hasta (pero sin incluir) el caracter en el indice 7
#y esto es lo que sucede si omites el indice stop:

my_str = 'Hello World'
print(my_str[8:])#rld
print(my_str)# hello world

#al igual se pueden omitir tanto los indices de start como de stop
my_str = 'Hello World'
print(my_str[:]) #hello world

#ademas de los incides start y stop, tambien existe el parametro opcional step, que se usa para especificar el incremento entre
#cada indice en el slice
#string[start:stop:step]
#en el ejemplo acontinuacion, la division comienza en el indice 0, se detiene
#antes del 11, y extrae cada segundo caracter:
my_str = 'Hello World'
print(my_str[0:11:2]) #hlowrd

#un truco util que puedes hacer con el parametro step es invertir una cadena
#configurando step en -1 y dejando start y stop en blanco
my_str = 'Hello World'
print(my_str[::-1]) # dlrow olleh

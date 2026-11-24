

developer = 'Devin'

#para ver que tipo es developer, se puede usar la funcion type()
print(type(developer)) #<class 'str'>
#la salida de <class 'str'> significa que developer es un tipo cadena.

#aqui estan los tipos de datos que haz aprendido hasta ahora,
#junto con lo de funcion type() imprime para cada uno:

my_integer_var = 10
print(type(my_integer_var))#<class 'int'>

my_float_var = 20.5
print(type(my_float_var))#<class 'float'>

my_string_var = 'hello'
print(type(my_string_var))# <class 'str'>

my_boolean_var = False
print(type(my_boolean_var))# <class 'bool'>

#para ver si account_balance es un entero, puedes verificarlo usando
#la funcion isinstance() asi:
account_balance = '12'
print(isinstance(account_balance, int)) #False

#la funcion integrada isinstance() permite verificar si una variable
#coincide con un tipo de dato especifico. toma un valor y el tipo contra el
#que quieres comprobarlo, y luego devuelve un booleano. En este caso, como
#account_balance es una cadena, devolvera False

#la funcion isinstance() tambien te permite verificar multiples tipos
#a la vez.
#ejemplo: si account_balance es un int o float:

account_balance = 12
print(isinstance(account_balance, (int,float))) #True

#en este ejemplo, account_balance es un entero, por lo que
#isinstance() devuelve True.Si account_balance fuera 12.0,
#isinstance() aun devolveria True porque estas verificando enteros o floats





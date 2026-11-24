#concatenar cadenas
#combnar multiples cadenas juntas con el operador mas (+) este proceso se llama concatenacion de cadenas
my_str_1 = 'Hello'
my_str_2 = 'World'
str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) #Hello world

#repetir cadenas
#se puede repetir una cadena multiplicandola por un entero usando el operador * la cadena se repite el numero especificado de veces
#sound = 'ha'
#repeat_sound = sound * 3
#print(repeat_sound) #hahaha

#concatenar cadenas con numeros
#la concatenacion solo funciona con cadenas. si intentas concatenar una cadena
#con un numero obtendras un typeError
#name = 'John Doe'
#age = 25
#name_and_age = name + ' '+ age
#esto sucede porque Python no convierte automaticamente otros tipos
#de datos como enteros en cadenas cuando los concatenas. Python requiere que todos
#los elementos sean cadenas antes de poder concatenarlos. Para solucionar esto, puedes convertir el numero en cadena con la funcion str()
name = 'Jhon Doe'
age = 20
name_and_age = name + ' ' + str(age)
print(name_and_age) #Jhon Doe 20

#tambien se puede usar el operador de asignacion aumentada para la concatenacion.
sound_2 = 'ha'
sound_2 *= 3
print(sound_2)
#aqui, sound *= 3 es equivalente a sound = sound * 3

#INTERPOLACION DE CADENAS
#El proceso de insertar variables y expresiones en una cadena se llama interpolacion de cadenas. Python tiene
#una categoria llamada f-strings(abreviatura de literales de cadena formateados), que te permite manejar la interpolacion con una sintaxis compata y legible

#Las cadenas f comienzan con f(ya sea minusculas o mayusculas) antes de las comillas, permite insetar variables o expresiones dentro de campos de reemplazo indicados por llaves ({})
#ejemplo :
name_3 = 'Martin Bustamante'
age_3 = 23
name_and_age_3 = f'My name is {name_3} and i am {age_3} years old'
print(name_and_age_3)
num1 = 5
num2 = 10
print(f'the sum of {num1} and {num2} is: {num1+num2}')
#no se necesita convertir tipos no cadena con la funcion str().

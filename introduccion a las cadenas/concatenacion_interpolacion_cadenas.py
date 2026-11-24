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

#tambien


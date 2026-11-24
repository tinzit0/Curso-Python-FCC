#paso 1
name = 'Alice'
#creamos una variable llamada name que tiene una cadena que dice 'Alice'

#paso 2
#ahora imprimimos en pantalla la variable name
#print(name), lo eliminamos por el paso 6

#paso 3
#python proporciona una funcion llamada type() que puedes usar para verificar el tipo de un valor.
print(type(name))

#paso 4
#agregar el estado de inscripcion del estudiante a los datos de la boleta de calificaciones.
#Esto puede representarse usando un valor booleano.

is_student = True

#paso 5
#la funcion print() puede mostrar mas de un valor a la vez. Separa los valores con una coma (,) para imprimirlos en
#en una misma linea
#imprime tanto is_student como type(is_student) en una sola linea separandolos con coma

print(is_student, type(is_student))

#paso 6
#el nombre del estudiante debe seguir el mismo formato que otros detalles
#elimina las salidas de la variable name. luego, imprime name y type(name) juntos en una linea separados por una coma en el paso anterior
print(name,type(name))

#paso 7
#agregar la edad del estudiante a los datos de la boleta de calificaciones.
#Para eso, Usaras un entero, uno de los tipos de datos numericos en python
#declarar una variable llamada age y asignale el valor entero 20.
#luego imprimir el valor y el tipo de dato de age juntos separados por una coma
age = 20
print(age, type(age))#20 <class 'int'>

#paso 8
#añadir puntuacion del estudiante
#declara una variable llamada score y asignale el valor 80.5.
#aunque tanto age como score son numeros, pueden no ser del mismo tipo.
#python proporciona una funcion llamada isinstance() para verificar esto
score = 80.5
#print(isinstance(score, int)) #False #paso 9

#paso 9
#la salida es False, lo que muestra que score no es un int.
#otro tipo comun de numero en Python es float, que representa un numero con decimales,
#remplaza int con float en la llamada existente a isinstance() para confirmar esto
print(isinstance(score, float)) #True

#paso 10
#la salida es True, confirmando que score es un float.
#para completar la boleta, imprime el valor de score junto con su tipo de dato en una sentencia print
print(score, type(score)) #80.5 <class 'float'>

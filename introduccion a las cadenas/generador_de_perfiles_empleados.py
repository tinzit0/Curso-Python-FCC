#paso 1:
#piden crear una variable first_name que almacene
#la cadena Jhon y una variable last_name que almacene
#la cadena Doe. luego imprime first_name y last_name

first_name = 'John'
last_name = 'Doe'
#print(first_name)
#print(last_name)

#Paso 2
#crea una variable full_name concatenando first_name
#y last_name. luego imprime full_name

full_name = first_name + last_name
#print(full_name)

#paso 3
#actualizar la variable full_name para que concatene la variable first_name
#un espacio ' ' y a la variable last_name

full_name = first_name + ' ' + last_name
#print(full_name)

#paso 4 y paso 5
#una continuacion, cra una variable address para alcanzar la direccion
#del empleo. asignale la cadena 123 Main Street y finalmente imprime address
address = '123 Main Street '
address += ', Apartment 4B'
#print(address)

#paso 7
#Ahora crea una variable llamada employee_age y asingnale el entero 28
employee_age = 28

#paso 8
#crear variable employee_info y asigna el resultado de concatenar, usando el operador +:
#la variable full_name
#una cadena que consiste en los personajes is precedentes y seguidos por un espacio
employee_info = full_name + ' ' + str(employee_age) + ' years old'
print(employee_info)
#paso 12
experience_years = 5
experience_info = 'Experience: '+str(experience_years) + ' years'
print(experience_info)

#paso 13
#Python 3.6 introdujo las f-strings para resolver esto. Al agregar la letra f
#antes de la comilla de apertura, puedes poner variables y expresiones dentro de campos de reemplazo
#representados por {}.

employee_card = f'Employee: {full_name}'
print(employee_card)

#paso 14
#actualizar employee_card para incluir la edad del empleado.
#la cadena final debe verse asi: Employee: [] | Age: [age] con [name]
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)


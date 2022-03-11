import enum


x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name']='Bryant'
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes["fútbol"][0]='Andres'
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30

"""iterar a traves de una lista de diccionarios"""
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(estudiantes_list):
    for index, value in enumerate(estudiantes_list):
        print('\n'+str(index)+' : '+value['first_name']+' - '+value['last_name'])
#iterateDictionary(estudiantes)
"""Obtener valore de una lista de diccionarios"""
def iterateDictionary2(key_name, some_list):
    for index, value in enumerate(estudiantes):
        print(value[key_name])
clave="first_name"
#iterateDictionary2(clave, estudiantes)
"""Iterar a traves de un diccionario con valores lista"""
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dictionary):
    for index, value in enumerate(some_dictionary):
        if(value=='ubicaciones'):
            print(len(value),value.upper(), '->')
            for key in (some_dictionary[value]):
                print(key)
        if(value=='instructores'):
            print(len(value),value.upper(), '->')
            for key in (some_dictionary[value]):
                print(key)
printInfo(dojo)
 
x = [ [5,2,3], [10,8,9] ] 
alumnos = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_de_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x = [[5,2,3], [10,8,9]]
x[1][0]=15
print(x)
alumnos[0] ['last_name'] = 'Bryant'
print(alumnos)

directorio_de_deportes ['fútbol'] [0] = "Andrés"
print (directorio_de_deportes)
z [0] ['y'] = 30
print (z)

 
alumnos = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_in_Dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_in_Dictionary(alumnos)  

def iterate_in_Dictionary2(key_name, list):
    for i in range (0, len (list)):
    
        for key, val in list [i].items():
            if key ==key_name:
                print (val)

iterate_in_Dictionary2('first_name',alumnos)
iterate_in_Dictionary2('last_name',alumnos)


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_Info(dict):
    for key,val in dict.items():
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_Info(dojo)




x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.Update values in Dictionaries and Lists
x[1][0]=15
students[0]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y']=30
print(x)
print(students)
print(sports_directory)
print(z)

#2.Iterate Through a List of Dictionaries 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - " + students[i]['first_name'] + ", last_name - " + students[i]['last_name'])
iterateDictionary(students)

#3.Get Values from a List of Dictionaries 
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name' ,students)
iterateDictionary2('last_name' ,students)

print("----------")
#4.Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for j in some_dict:
        print(len(some_dict[j]),j)
        for i in range(len(some_dict[j])):
            print(some_dict[j][i])
        print("----------")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
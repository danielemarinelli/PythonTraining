import json

# this is a JSON file in string format:
myFile = '{"name":"Daniele","languages":["Java","Python"]}'
#loads method parse json string and it returns dictionary
dict_myFile = json.loads(myFile)  # it's a dictionary
print(dict_myFile)
print(dict_myFile['name'])
print(dict_myFile['languages'])  # it's a LIST
#HOW TO get first language --> JAVA (line 13)
list_languages = dict_myFile['languages']
print(type(list_languages))  # it's a LIST
print(list_languages[0])
# or in one line -->
print(dict_myFile['languages'][0])

# ****** Parse content in a JSON file *******
with open('C:\\Users\\dmarinel\\OneDrive - Capgemini\\Documents\\API_training\\data_set.json') as file:
    # data_set.json has 2 keys (dashboard+courses), value of dashboard is dictionary because {} and value of courses is a list because []
    data = json.load(file) # it's a dictionary
    print(data)
    print(type(data))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))
#price of course Tosca (index can change if we add a new course)
    print(data['courses'])
    for c in data['courses']:
        print(c) # c now it is a dictionary
        if c['title'] == 'Tosca':
            print(c['price'])
            assert c['price'] == 35

#COMPARE TWO JSON FILES
with open('C:\\Users\\dmarinel\\OneDrive - Capgemini\\Documents\\API_training\\data_set1.json') as file1:
    data1 = json.load(file1)
    assert data == data1

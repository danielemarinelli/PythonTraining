import json

import requests

#following the API document developed by dev team
response = requests.get('http://216.10.245.166/Library/GetBook.php',
             params={'AuthorName':'Rahul Shetty2'},)
#print(response.text)
#print(type(response.text))
#dict_response = json.loads(response.text)

jsonResponse = response.json()
print(type(jsonResponse))
print(jsonResponse)
print(jsonResponse[0]['isbn'])
print(response.status_code)
assert response.status_code == 200
print(response.headers)
#validate the headers
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'

#Retrive the book details with book_name = Learn Appium Automation with Java
# jsonResponse --> is a List af all books, and books are inside dictionary
for actualBook in jsonResponse:
    if actualBook['book_name'] == 'Learn Appium Automation with Java':
        print(actualBook)
        break

expectedBook = {
        "book_name": "Learn Appium Automation with Java",
        "isbn": "KM201",
        "aisle": "227"
    }

print(expectedBook)
print(actualBook)
assert expectedBook == actualBook

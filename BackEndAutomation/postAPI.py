import requests

from BackEndAutomation.utilities.resources import ApiResources
from utilities.configurations import *
from utilities.resources import *
from payloads import *

# ALL DOCUMENTATION is at ---->  https://requests.readthedocs.io/en/latest/
# performing a POST hitting the endpoint (URL is not hardcoded, but getting it from properties.ini file) to add a book: with a Payload and headers
URL_addBook = getConfig()['API']['endpoint']+ApiResources.addBook
URL_deleteBook = getConfig()['API']['endpoint']+ApiResources.deleteBook
headers = {"Content-Type":"application/json"}
action_addBook = requests.post(URL_addBook,json=addBookPayload("1978dm"), headers=headers,)

print(action_addBook.json())
print(type(action_addBook.json())) # response is a dictionary
response_json = action_addBook.json()
bookID = response_json['ID']
print("book created with ID -->> " , bookID)
print("Status Code for POST request: " , action_addBook.status_code)
# delete the book just created
response_delete = requests.post(URL_deleteBook,  #URL_deleteBook instead of hardcoding the URL --> 'http://216.10.245.166//Library/DeleteBook.php',
                json=addIDtoDelete(bookID), headers=headers,
              )

assert response_delete.status_code == 200
#convert response into JSON
res_json = response_delete.json()
print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

"""
# AUTHENTICATION example
url_github = "https://api.github.com/user"
github_response = requests.get(url_github, verify=False, auth=('danielemarinelli', getPassword()))
print(github_response.status_code)

url_github_repos = "https://api.github.com/user/repos"
github_repos_response = requests.get(url_github_repos, verify=False, auth=('danielemarinelli', getPassword()))
print(github_response.status_code)

# to avoid to repeat the auth for each requests I write in framework, I can use session() method:

se = requests.session()
se.auth = auth=('danielemarinelli', getPassword())
url_github_repos = "https://api.github.com/user/repos"
github_repos_response = se.get(url_github_repos)
print(github_response.status_code)

#Attachment . How to send a file to API
url_petStore = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
f = {'file': open('C:\\Users\\dmarinel\\OneDrive - Capgemini\\Documents\\API_training\\bit.jpg', 'rb')} # from the documentated website
r=requests.post(url_petStore, files=f)
print(r.status_code)
print(r.text)
"""


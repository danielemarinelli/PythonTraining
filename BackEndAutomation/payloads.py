

def addBookPayload(isbn):
    body ={
        "name": "Learn API RestAssured Automation with Java",
        "isbn": isbn,
        "aisle": "78227",
        "author": "Jim Kelly"
    }
    return body

def addIDtoDelete(id_book):
    body_when_sending_delete ={
        "ID": id_book,
    }
    return body_when_sending_delete


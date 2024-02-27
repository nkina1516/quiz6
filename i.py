class Library:
    def borrowBook(self):
        raise NotImplementedError
    def returnBook(self):
        raise NotImplementedError

class SpecialAccess:
    def generateReport(self):
        raise NotImplementedError
    def addBookToCatalog(self):
        raise NotImplementedError
    def removeBookFromCatalog(self):
        raise NotImplementedError

class Browse:
    def searchForBook(self, direction):
        raise NotImplementedError
    
class Librarian(Library, SpecialAccess, Browse):
    print ("Librarian has access to everything")

class Member(Library):
    print ("Member has access to the Library")

class Guest(Browse):
    print ("Guest has the ability to lookaround")

def userAccess(user):
    if isinstance(user, Library):
        user.borrowBook()

def user_wants_specialAccess(user):
    if isinstance(user, SpecialAccess):
        user.generateReport()

userAccess(Guest)  # Would raise error, as Library doesn't implement browse functionality
userAccess(Librarian)  # No error

user_wants_specialAccess(Guest)  #Error, as Guest doesn't implement SpecialAccess
user_wants_specialAccess(Librarian)  # No error, as Librarian implements SpecialAccess

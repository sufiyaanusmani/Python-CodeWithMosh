# to allow us to pass variable number of key value pairs
def saveUser(**user):
    print(user)
    print(user["name"])


saveUser(id=1, name="Sufiyaan", age=18)

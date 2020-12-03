from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

class UserDoesNotExist(Exception):
    pass

class UserAccessExpired(Exception):
    pass

class UserNoPermission(Exception):
    pass



def get_secret_token(username):
    names = {item.name for item in USERS}
    roles = {'Julian': USER, 'Bob': USER, 'PyBites': ADMIN}
    expirations = {'Julian': False, 'Bob': True, 'PyBites': False}
    
    try:
        for item in USERS:
            if username == item.name and item.role == ADMIN:
                if item.expired == False:
                    return SECRET
    except:
        pass

    else:
        if username not in names:
            raise UserDoesNotExist
        if roles.get(username) != ADMIN and expirations.get(username) == True:
            raise UserAccessExpired
        if roles.get(username) != ADMIN:
            raise UserNoPermission
        if expirations.get(username) == True:
            raise UserAccessExpired
    
    
print(get_secret_token('PyBites'))


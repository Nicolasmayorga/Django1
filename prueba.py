users = [
    {
        'email': 'nicolas@gmial.com',
        'first_name': 'Nicolas',
        'last_name': 'Mayorga',
        'password' : '123456',
        'is_admin' : True,
        'country' : 'Colombia',
        'city' : 'Bogotá'
    },

    {
        'email': 'David@gmial.com',
        'first_name': 'David',
        'last_name': 'Jimenez',
        'password' : '123456',
        'is_admin' : True,
        'country' : 'Colombia',
        'city' : 'Bogotá'
    },

    {
        'email': 'samanta@gmial.com',
        'first_name': 'Samanta',
        'last_name': 'Jimenez',
        'password' : '123456',
        'is_admin' : False,
        'country' : 'Colombia',
        'city' : 'Pacho'
    },

    {
        'email': 'ana@gmial.com',
        'first_name': 'Ana',
        'last_name': 'Mayorga',
        'password' : '123456',
        'is_admin' : False,
        'country' : 'Colombia',
        'city' : 'Soacha'
    },

    {
        'email': 'tata@gmial.com',
        'first_name': 'Tatiana',
        'last_name': 'Solano',
        'password' : '123456',
        'is_admin' : True,
        'country' : 'Colombia',
        'city' : 'Soacha'
    }

]

from posts.models import User 

for user in users:
    obj = User(**user)
    print(obj.pk, ':', obj.email)













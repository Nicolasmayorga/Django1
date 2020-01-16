nicolo = User.objects.create(
email = 'nicolas@gmial.com',
first_name = 'Nicolas',
last_name = 'Mayorga',
password = '123456',
is_admin = True,
country = 'Colombia',
city = 'Bogotá'
)

nicolo.save()


davo = User.objects.create(
email = 'David@gmial.com',
first_name = 'David',
last_name = 'Jimenez',
password  = '123456',
is_admin  = True,
country  = 'Colombia',
city  = 'Bogotá'
)

davo.save()

sami = User.objects.create(
email = 'samanta@gmial.com',
first_name = 'Samanta',
last_name = 'Jimenez',
password  = '123456',
is_admin  = True,
country  = 'Colombia',
city  = 'Pacho'
)

sami.save()


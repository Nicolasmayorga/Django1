"""Vistas de Platzigram"""

#Django
from django.http import HttpResponse

#Utilidades
from datetime import datetime
import json



def hello_world(request):
    
    return HttpResponse('Hola, la hora del servidor es {now}'.format(now = datetime.now().strftime('%b %dth, %Y, %H:%M hrs')))
    
    """Retorna lo que queremos que diga en la URL. Siempre debe tener el atributo request"""


def sort_integers(request):

    """retorna enteros ordenados en formato JSON"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
 
    }

    return HttpResponse(json.dumps(data, indent = 4), content_type = 'application/json')


def say_hi(request, name, age):
    """Retorna información personal"""
    if age < 12:
        message = 'Lo lamento {} tu ingreso no es permitido'.format(name)
    else:
        message = 'Hola, {} bienvenido a Platzogram'.format(name)

    return HttpResponse(message)

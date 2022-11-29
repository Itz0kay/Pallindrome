from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response

from simple_app.models import *
from simple_app.serializer import *


# Create your views here.
@api_view(['GET', 'POST'],)
@permission_classes((permissions.AllowAny,))
def home(request):
    if request.method == 'POST':
        serials = plndSerializer(data=request.data)

        if serials.is_valid():
            serials.save()

            return Response(serials.data, status=status.HTTP_201_CREATED)

    else:
        plnd_all = Pallindrome.objects.all()
        # print(plnd_all)

        serials = plndSerializer(plnd_all, many=True)
        # print(serials.data)

        return JsonResponse({'plds':serials.data})

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def pal(request):
    pid = request.GET.get('id',None)
    try:
        plnd = Pallindrome.objects.filter(id=pid)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if pid != None:
        if request.method == 'GET':
            serial = plndSerializer(plnd, many=True)
            return Response(serial.data)

        elif request.method == 'PUT':
            serials = plndSerializer(data=request.data)
            if serials.is_valid():
                serials.save()
                return Response(serials.data, status=status.HTTP_201_CREATED)
            return Response(serials.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            plnd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




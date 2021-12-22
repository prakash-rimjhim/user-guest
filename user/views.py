from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import user
from .serializers import UserSerializer

from .models import User


@api_view(['GET'])
def api_overview(request):
    return JsonResponse('API BASE POINT', safe=False)


@api_view(['GET'])
def user_list(request):
    tasks = User.objects.all().order_by('id')
    serializer = UserSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def user_update(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def user_delete(request, pk):
    task = User.objects.get(id=pk)
    task.delete()

    return Response('Item successfully delete!')

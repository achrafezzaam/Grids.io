from django.http import JsonResponse
from .models import Grid
from .serializers import GridSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def grid_list(request):
    grids = Grid.objects.all()
    serializer = GridSerializer(grids, many=True)
    return JsonResponse({"grids": serializer.data})

@api_view(['POST'])
def add_grid(request):
    serializer = GridSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_grid(request):
    return 'Hello'

@api_view(['DELETE'])
def del_grid(request):
    return 'Hello'

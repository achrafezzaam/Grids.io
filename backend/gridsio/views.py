from .models import Grid, Component
from .serializers import GridSerializer, ComponentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def grid_list(request):
    grids = Grid.objects.all()
    serializer = GridSerializer(grids, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def grid_info(request, id):
    try:
        grid = Grid.objects.get(pk=id)
    except Grid.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GridSerializer(grid)
    return Response(serializer.data)

@api_view(['POST'])
def add_grid(request):
    serializer = GridSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_grid(request, id):
    try:
        grid = Grid.objects.get(pk=id)
    except Grid.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GridSerializer(grid, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def del_grid(request, id):
    try:
        grid = Grid.objects.get(pk=id)
    except Grid.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    grid.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def component_list(request):
    components = Component.objects.all()
    serializer = ComponentSerializer(components, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def component_info(request, id):
    try:
        component = Component.objects.get(pk=id)
    except Component.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ComponentSerializer(component)
    return Response(serializer.data)

@api_view(['POST'])
def add_component(request):
    serializer = ComponentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_component(request, id):
    try:
        component = Component.objects.get(pk=id)
    except Component.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ComponentSerializer(component, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def del_component(request, id):
    try:
        component = Component.objects.get(pk=id)
    except Component.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    component.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

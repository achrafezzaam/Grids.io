''' Defining the Grid and Component API views '''
from .models import Grid, Component
from .serializers import GridSerializer, ComponentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def grid_list(request):
    ''' Get all the Grids from database '''
    grids = Grid.objects.all()
    serializer = GridSerializer(grids, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def grid_info(request, id):
    ''' Research for a specific grid by id '''
    try:
        grid = Grid.objects.get(pk=id)
    except Grid.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = GridSerializer(grid)
    return Response(serializer.data)

@api_view(['POST'])
def add_grid(request):
    ''' Create a new Grid '''
    serializer = GridSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_grid(request, id):
    ''' Update a Grid by id '''
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
    ''' Delete a specified Grid '''
    try:
        grid = Grid.objects.get(pk=id)
    except Grid.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    grid.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def component_list(request):
    ''' Get all the Components from database '''
    components = Component.objects.all()
    serializer = ComponentSerializer(components, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def component_info(request, id):
    ''' Research for a specific Component by id '''
    try:
        component = Component.objects.get(pk=id)
    except Component.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ComponentSerializer(component)
    return Response(serializer.data)

@api_view(['POST'])
def add_component(request):
    ''' Create a new Component '''
    serializer = ComponentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_component(request, id):
    ''' Update a Component by id '''
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
    ''' Delete a specified Component '''
    try:
        component = Component.objects.get(pk=id)
    except Component.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    component.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

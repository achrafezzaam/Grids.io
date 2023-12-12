''' Using Serializers to convert the Grid and Component models to json'''
from rest_framework import serializers
from .models import Grid, Component


class GridSerializer(serializers.ModelSerializer):
    ''' Grid model serializer '''
    class Meta:
        model = Grid
        fields = ['id', 'name', 'description']


class ComponentSerializer(serializers.ModelSerializer):
    ''' Component model serializer '''
    class Meta:
        model = Component
        fields = ['id', 'name', 'component_type', 'value', 'grid']

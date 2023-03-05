from dataclasses import field
from rest_framework import serializers
from .models import State, Terminal, Trips

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('id','name',)

class TerminalSerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')

    class Meta:
        model = Terminal
        fields = ('id','name', 'state', 'description')


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = ('image_url', 'departure', 'arrival','transport_fee')


class ParkTerminalSerializer(serializers.ModelSerializer):
    # state = serializers.SlugRelatedField(queryset=State.objects.all(), slug_field='name')

    class Meta:
        model = Terminal
        fields = ('name', 'description')

from rest_framework import serializers
from api.models import Hangman

class Hangmanserializer(serializers.ModelSerializer):
    class Meta:
        model = Hangman
        fields = ('id','question', 'answer')
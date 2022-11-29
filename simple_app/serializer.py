from rest_framework import serializers
from simple_app.models import *

class plndSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pallindrome
        fields = ['id', 'name', 'p_or_not']
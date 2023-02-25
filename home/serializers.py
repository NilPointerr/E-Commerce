from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.Serializer):
    class meta:
        models = Login
        template_name ='login.html' 
        fields = "__all__"
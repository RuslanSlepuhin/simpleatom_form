from rest_framework import serializers
from .models import *

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAnswerModel
        fields = '__all__'

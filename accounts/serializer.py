from rest_framework import serializers 
from .models import *

class StudentSerializer(serializers.Serializer):
    school_id= serializers.CharField()
    #Guardian= serializers.CharField()
    Name = serializers.CharField()
    Class = serializers.CharField()
    #Gender = serializers.CharField(source='get_gender_display')
    debt_owed = serializers.IntegerField()


    def create(self, data):
        return Student.objects.create(**data)
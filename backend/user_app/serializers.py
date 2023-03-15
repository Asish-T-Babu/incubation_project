from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','username','email','password','is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class Company_registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_register
        fields ="__all__"

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields ="__all__"
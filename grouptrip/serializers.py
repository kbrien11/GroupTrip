from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .models import Plan,Message,Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name','is_active']
        extra_kwargs = {'password': {'required': False},'first_name':{'required':False},'last_name':{'required':False},'email':{'required':False}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        print(Token)
        return user


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id','date','title','description','type','time','group_name']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','date','message','username','group_name']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id','name']
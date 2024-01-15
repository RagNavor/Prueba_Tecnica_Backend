from rest_framework import serializers
from django.contrib.auth.models import User



class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields: ('username','email','password')
        

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def create(self, validated_data:dict)->User:
        new_user = User()
        new_user.first_name:str = validated_data.get('first_name')
        new_user.last_name:str = validated_data.get('last_name')
        new_user.username = new_user.first_name[0] + new_user.last_name
        new_user.email = validated_data.get('email')
        new_user.set_password(validated_data.get('password'))
        new_user.save()
        return new_user
    
    def validate_username(self, data):
        user = User.objects.filter(email= data).first()
        if user:
            raise serializers.ValidationError('Este usuario ya existe')
        return data
    
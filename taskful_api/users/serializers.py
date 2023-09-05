from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    def create(self, **validated_data):
        passowrd = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(passowrd)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['url','id','username','email','first_name','last_name', 'password']
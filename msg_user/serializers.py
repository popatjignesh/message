from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from msg_user.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message

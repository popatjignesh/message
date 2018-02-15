from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from msg_user.models import *
from msg_user.serializers import *
from rest_framework.views import APIView


class que_14(APIView):
	def get(self, request, format=None):
		msg = Message.objects.order_by('-created_on')
		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class que_15(APIView):
	def get(self, request, format=None):
		msg1 = Message.objects.all()[:5]
		msg2 = Message.objects.all()[5:10]
		msg = []

		for x in msg1:
			msg.append(x)
		for x in msg2:
			msg.append(x)

		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class que_16(APIView):
	def get(self, request, format=None):
		msg = Message.objects.filter(message__iexact='Good morning')
		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class que_17(APIView):
	def get(self, request, format=None):
		msg = Message.objects.filter(message='')
		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class que_18(APIView):
	def get(self, request, format=None):
		msg = Message.objects.all().exclude(message__icontains='nice')
		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class que_19(APIView):
	def get(self, request, format=None):
		msg = Message.objects.filter(message__startswith='who')
		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class que_20(APIView):
	def get(self, request, format=None):
		msg = Message.objects.filter(message_from__first_name='Pratik')
		serializer = MessageSerializer(msg, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import json



from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django_filters.rest_framework import DjangoFilterBackend



from accounts.models import Profile
from api.serializers import *

class ProfileCreateAPI(CreateAPIView):
	serializer_class =  UserSerializer
	queryset = User.objects.all()


class LoginAPI(generics.GenericAPIView):
	serializer_class = LoginSerializer

	def get_serializer_context(self):
		return {'request': self.request}

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			print("***")
			print(new_data)
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
		

class LogoutAPI(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request):
		logout(request)
		return Response(status=HTTP_200_OK)

class MyAPI(generics.ListAPIView):
	serializer_class = MyUserSerializer
	permission_classes = [permissions.IsAuthenticated]
	queryset = User.objects.all()


class ProfileRetrieveUpdateAPI(generics.RetrieveUpdateAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [permissions.IsAuthenticated]


	def get_object(self):
		user = self.request.user
		obj = get_object_or_404(Profile, user=user)
		return obj


class ProfileListAPI(generics.ListAPIView):
	serializer_class = ProfileListSerializer
	permission_classes = [permissions.IsAuthenticated]
	filter_backends = (DjangoFilterBackend,)
	filterset_fields = ('gender',)

	def get_serializer_context(self):
		return {'my_user': self.request.user }

	def get_queryset(self):
		serializer = self.get_serializer()
		return Profile.objects.exclude(user=self.request.user)




class AddFriendAPI(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request):
		id = request.data['id']
		friend_user = get_object_or_404(Profile, id=id)
		my_user = request.user
		my_user_profile = Profile.objects.get(user=my_user)

		if my_user_profile == friend_user:
			return Response({"Fail": "Cannot be friends with yourself"}, status=HTTP_400_BAD_REQUEST)

		for f in my_user_profile.friends.all():
			if f==friend_user:
				return Response({"Fail": "User alreay a friend"}, status=HTTP_400_BAD_REQUEST)

		my_user_profile.friends.add(friend_user)

		return Response({"Success": "User added as friend"}, status=HTTP_200_OK)



class RemoveFriendAPI(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request):
		id = request.data['id']
		friend_user = get_object_or_404(Profile, id=id)
		my_user = request.user
		my_user_profile = Profile.objects.get(user=my_user)
		for f in my_user_profile.friends.all():
			if f==friend_user:
				my_user_profile.friends.remove(friend_user)
				return Response({"Success": "User removed from friends"}, status=HTTP_200_OK)


		return Response({"Fail": "User already not a friend"}, status=HTTP_400_BAD_REQUEST)


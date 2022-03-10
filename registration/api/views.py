from django.shortcuts import render
#from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterationSerializer, UserInfoSerializer
from .models import UserInfo
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics
from rest_framework import status
import uuid
# Create your views here.


class RegisterationAPIView(generics.GenericAPIView):
    serializer_class = RegisterationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User Successfully",
                "User": serializer.data}, status=status.HTTP_201_CREATED
            )
        return Response({"Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class UserInfoAPIView(APIView):
    permissions_class = [IsAuthenticated]
    def get(self, request):
        one = UserInfo.objects.filter(user=request.user)
        serializer = UserInfoSerializer(one,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class UserDetail(APIView):
     def put(self, request, pk):
        user = UserInfo.objects.get(id=pk)
        serializer = UserInfoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, pk):
        user = UserInfo.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
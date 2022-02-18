from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterationSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import serializers
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
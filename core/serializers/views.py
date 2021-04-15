from django.shortcuts import render
from .serializers import credSerializer
from rest_framework import viewsets
from core.models import creds
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter


class credsapi(viewsets.ModelViewSet):
    queryset=creds.objects.all()
    serializer_class=credSerializer
    filter_backends=[SearchFilter]
    search_fields=['project_name']
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminUser]


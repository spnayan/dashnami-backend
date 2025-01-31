from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,PersonSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
# Add this in your views.py for debugging purposes
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from django.core.management import call_command
from .models import Person

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [AllowAny]

# Add this in your views.py for debugging purposes
def show_db_settings(request):
    return JsonResponse(settings.DATABASES)
# Add this in your views.py for manual migration


def run_migrations(request):
    call_command('migrate')
    return HttpResponse('Migrations completed')


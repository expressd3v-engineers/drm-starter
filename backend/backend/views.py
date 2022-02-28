from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from backend.serializer import UserSerializer, GroupSerializer
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', context={'title': 'DRM Starter'})


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request,  *args, **argv):
    return render(request, '500.html', status=500)


def error_403(request,  exception):
    data = {}
    return render(request, '403.html', data)


def error_400(request,  exception):
    data = {}
    return render(request, '400.html', data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

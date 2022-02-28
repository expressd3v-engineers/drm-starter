from django.urls import re_path
from backend.views import home
from document.views import index
urlpatterns = [
    re_path('document', index, name='document'),
]

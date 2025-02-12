from django.urls import path
from .views import jpgtoexcel


urlpatterns = [
    path('', jpgtoexcel, name='jpgtoexcel')
]
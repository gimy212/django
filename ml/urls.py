from django.urls import path
from .views import predict2

urlpatterns = [
   
    path('predict2/', predict2, name='predict2_image'),
    
    
]
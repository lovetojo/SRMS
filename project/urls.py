
from django.urls import path
from .views import signin

urlpatterns = [
    path('signin/', signin, name='signin'),
    # Add other URL patterns as needed
]

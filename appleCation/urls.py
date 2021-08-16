from django.urls import path
from .views import create_account, login_access

urlpatterns = [
    path('CreateCat', create_account),
    path('Login', login_access),
]

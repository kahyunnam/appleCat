from django.urls import path
from .views import create_account, login_access, new_apple, update_apple

urlpatterns = [
    path('CreateCat', create_account),
    path('Login', login_access),
    path('NewApple', new_apple),
    path('UpdateApple/<str:accessKey>/<int:id>', update_apple)
]

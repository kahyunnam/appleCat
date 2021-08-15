from django.contrib import admin
from .models import Cat, Apple

# Register to admin site
admin.site.register(Cat)
admin.site.register(Apple)
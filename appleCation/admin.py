from django.contrib import admin
from .models import Cat, Apple, AppleOA, AppleInterview

# Register to admin site
admin.site.register(Cat)
admin.site.register(Apple)
admin.site.register(AppleOA)
admin.site.register(AppleInterview)

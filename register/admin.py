from django.contrib import admin

# Register your models here.
from .models import Login,Posts
admin.site.register(Login)
admin.site.register(Posts)
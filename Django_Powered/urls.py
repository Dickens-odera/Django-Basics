from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url(r'^$',include('portfolio.urls')),
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('register/',include('register.urls')),
    path('blog/',include('blog.urls')),
    path('portfolio/',include('portfolio.urls')),
    path('register/',include('register.urls')),
]

"""
URL configuration for BackendIntimia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views import home_view, auth_view, verify_view
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "MiniBlog Header"
admin.site.site_title = "MiniBlog Title"
admin.site.index_title = "MiniBlog Index Title"
from chats.views import index, chatPage



liste=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('chat/<str:username>/', chatPage, name='chat'),
    path('', home_view, name='home-view'),
    path('', index, name='home'),
    path('blogApp/', include('blogApp.urls')),
    path('login/', auth_view, name= 'login-view'),
    path('api/', include('users.urls')),
    path('verify/', verify_view, name= 'verify-view'),
]+static(settings.STATIC_URL,documenmt_root = settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
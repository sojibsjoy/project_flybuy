"""project_flybuy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('', include('flybuy.urls')),
    path('home/', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('catalog/', include('catalog.urls')),
    path('checkout/', include('checkout.urls')),
    path('contacts/', include('contacts.urls')),
    path('faq/', include('faq.urls')),
    path('gallery/', include('gallery.urls')),
    path('login/', include('login.urls')),
    path('signup/', include('signup.urls')),
    path('admin/', admin.site.urls),
]

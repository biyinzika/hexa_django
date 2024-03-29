"""phoenix_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from momo.views import homepage_view, about_page
from listing.views import list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listing', list_view, name='listing')
#     path('momo/', include('momo.urls')),
#     path('home/', homepage_view, name='home'),
#     path('about/', about_page, name='about'),
    
    
#     url(r'^admin/', admin.site.urls),
#     url(r'home', views.homepage_view, name='home'),
]

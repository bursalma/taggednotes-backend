"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path

# from . import views


urlpatterns = [
    path('api/', include('taggednotes.urls')),
    path('admin/', admin.site.urls),
    # path('', views.IndexView.as_view()),
    # path('manifest.json', views.ManifestView.as_view()),
    # path('logo192.png', views.Logo1View.as_view()),
    # path('logo512.png', views.Logo5View.as_view()),
    # path('favicon.ico', views.IconView.as_view())
]
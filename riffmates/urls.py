"""
URL configuration for riffmates project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('credits/', home_views.credits, name='credits'),
    path('about/', home_views.about, name='about'),
    path('version/', home_views.version, name='version'),
    path('news/', home_views.news, name='news'),
    path('news2/', home_views.news2, name='news2'),
    path('news3/', home_views.news3, name='news3'),
    path('news_bootstrap/', home_views.news_bootstrap, name='news_bootstrap'),
    path('news_adv/', home_views.news_advanced, name='news_adv'),
    path('bands/', include('bands.urls')),
]

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

from django.urls import path, include
from home import views

urlpatterns = [
    path('credits/', views.credits, name='credits'),
    path('about/', views.about, name='about'),
    path('version/', views.version, name='version'),
    path('news/', views.news, name='news'),
    path('news2/', views.news2, name='news2'),
    path('news3/', views.news3, name='news3'),
    path('news_bootstrap/', views.news_bootstrap, name='news_bootstrap'),
    path('news_adv/', views.news_advanced, name='news_adv'),
]

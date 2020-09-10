"""newApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from board.views import (ListView, DetailAndDeleteView,
                         CreateUpdateView, DeleteCompView)
from user.views import(SignupView, SigninView, SignoutView)

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('signin/', SigninView.as_view()),
    path('article/signout', SignoutView.as_view()),
    path('article/', ListView.as_view()),
    path('article/create', CreateUpdateView.as_view()),
    path('article/delete', DeleteCompView.as_view()),
    path('article/<article_id>/update', CreateUpdateView.as_view()),
    path('article/<article_id>', DetailAndDeleteView.as_view()),
    path('admin/', admin.site.urls),
]

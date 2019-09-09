from django.urls import path, include
from django.contrib import admin
from django.urls import path


from . import views
urlpatterns =[

    path('', views.home, name='home'),
    path('login/', include('Chamada.urls')),
]



from django.urls import path, include
from . import views

urlpatterns = [
    # /mainapp/home/
    path('home/', views.home, name='home'),

    # /mainapp/Prezydenckie/
    path('<str:rodzaj_wyborow>/', views.lista, name='lista'),

    # /mainapp/Prezydenckie/kandydat/3/
    path('<str:rodzaj_wyborow>/kandydat/<int:pk>/', views.kandydat, name='kandydat'),

    # /mainapp/Prezydenckie/raport/
    path('<str:rodzaj_wyborow>/raport/', views.raport, name='raport'),
]
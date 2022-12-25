from django.urls import path
from . import views

#20
urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser')
]
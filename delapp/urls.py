from django.urls import path
from delapp import views
urlpatterns = [
        path('', views.index, name='index'),
]
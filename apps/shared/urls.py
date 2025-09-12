from django.urls import path
from apps.shared import views

app_name = 'shared'
urlpatterns = [
    path('', views.index, name='index'),
]

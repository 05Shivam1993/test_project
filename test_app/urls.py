from django.urls import path
from test_app import views

urlpatterns = [
    path('add', views.add_data, name="add_data"),
    path('list', views.list_data, name="list_data"),
]

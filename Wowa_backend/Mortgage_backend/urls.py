from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_view, name='api-overview'),
    path('get_mortgage_data/', views.get_mortgage_data, name='get-mortgage-data'),
    path('insert_json', views.insert_json_data, name='insert_json_data')
]

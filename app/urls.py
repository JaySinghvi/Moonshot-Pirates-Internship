from django.urls import path, include
from . import views
from .views import DisasterDetail, ResourceDetail
urlpatterns = [
    path('', views.home, name='home'),
    path('disaster', views.disaster_page, name='disaster'),
    path('create_disaster/', views.create_disaster, name='create_disaster'),
    path('resource', views.resources_page, name='resource'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('disaster/<slug:slug>', DisasterDetail, name='disaster_detail'),
    path('resource/<slug:slug>', ResourceDetail, name='resource_detail'),
]
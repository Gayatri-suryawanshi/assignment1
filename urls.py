
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('cse',views.cse,name="cse"),
    path('etc',views.etc,name="etc"),
    path('mech',views.mech,name="mech"),
    path('civil',views.civil,name="civil"),
]

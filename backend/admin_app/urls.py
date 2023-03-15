from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('view_company',view_company,name='view_company'),
    path('update_company_application/<int:id>',update_company_application,name='update_company_application'),
    path('view_slot',view_slot,name='view_slot'),
    path('use_slot/<int:sid>/<int:cid>',use_slot,name='use_slot'),
    path('view_company_slot',view_company_slot,name='view_company_slot'),
]

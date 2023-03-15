from django.contrib import admin
from django.urls import path,include
from user_app.views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register',register,name='register'),
    path('company_register',company_register,name='company_register'),
    path('view_register_company/<int:id>/', view_register_company, name='view_register_company'),
    path('token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

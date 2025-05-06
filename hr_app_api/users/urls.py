from django.urls import path
from . import views
from .views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView 

urlpatterns = [
    path('register/',views.register_view, name='register'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password', views.change_password, name='change-password'),
    path('update-profile', views.update_profile, name='update-profile'),
    path('logout/', views.logout, name='logout')
]

from django.urls import path
from .views import CompanyAPIView, LoginAPIView, RefreshTokenAPIView, RoleAPIView, UserAPIView , CompanyCreateAPIView, PermissionAPIView, PasswordChangeAPIView, UserInfoAPIView


urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('token/refresh', RefreshTokenAPIView.as_view()),
    path('users', UserAPIView.as_view()),
    path('users/<str:pk>', UserAPIView.as_view()),
    path('company', CompanyAPIView.as_view()),
    path('company/create', CompanyCreateAPIView.as_view()),
    path('roles', RoleAPIView.as_view()),
    path('permissions', PermissionAPIView.as_view()),
    path('password/update', PasswordChangeAPIView.as_view()),
    path('user/info', UserInfoAPIView.as_view())
]

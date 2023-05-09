from django.urls import path, include
from .views import Register, ProfileDetail, profile_error


urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
    path('profile/<slug:slug>/', ProfileDetail.as_view(), name='profile'),
    path('profile-error/', profile_error, name='profile-error')
]

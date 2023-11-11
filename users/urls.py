from django.urls import path
from users.views import UserLoginView, UserLogoutView


urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout')
]

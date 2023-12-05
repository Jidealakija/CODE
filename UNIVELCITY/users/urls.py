from django.urls import path
from .views import CreateUserView, HomePage

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='user_registration'),
    path('home/', HomePage.as_view(), name='home')
]

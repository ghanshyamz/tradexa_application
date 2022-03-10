from user import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('post/',views.post, name='post'),
    path('logout/',views.logout, name='logout'),
]
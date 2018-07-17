from django.urls import path

from authentication import views

urlpatterns = [
    path('user', views.index, name="user"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout")
]
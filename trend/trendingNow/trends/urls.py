from django.urls import path
from . import views

urlpatterns = [
    path('tweeter/', views.tweeter, name="tweeter"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('create-message/', views.createMessage, name="create-message"),
    path('room/', views.room, name="room"),
    path('update-message/<str:pk>/', views.updateMessage, name="update-message"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('delete-comment/<str:pk>/', views.deleteComment, name="delete-comment"),
    path('update-user/', views.updateUser, name="update-user"),

    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
]

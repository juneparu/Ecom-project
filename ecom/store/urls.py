from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/' ,views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout_view'),
    path("show/", views.show, name="show"),
    path("insert/", views.insert, name="insert"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("updatepage/<int:pk>", views.updatePage, name="updatepage"),
    path("update/<int:pk>", views.update, name="update"),
    path("check/<int:pk>", views.checkb, name="check"),
]

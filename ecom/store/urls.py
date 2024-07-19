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
    path('about_us/', views.about_us, name='about_us'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # Optional URL for removing items
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/', views.single_product, name='single_product')
]

<<<<<<< HEAD
from django.urls import path, include
from . import views
from .views import home
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/' ,views.register, name='register'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout_view'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('home/', views.home, name='home'),
    path('home/', home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # Optional URL for removing items
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('success/', views.success_view, name='success'),  # Define success_view
    path('failure/', views.failure_view, name='failure'),  # Define failure_view
    path('pet/', views.pet, name='pet'),
    path('shop/', views.shop, name='shop'),
    path('captcha/', include('captcha.urls')),
     path('profile/', views.profile, name='profile'),
]
=======
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
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('account/', views.account, name='account'),
]
>>>>>>> 2ae262a36bac2affb99cf190835927092bd84717

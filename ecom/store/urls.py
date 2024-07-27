from django.urls import path, include
from store import views
from .views import home
# from django.contrib.auth.views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/' ,views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('home/', home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # Optional URL for removing items
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('captcha/', include('captcha.urls')),
    path('profile/', views.profile, name='profile'),
]

<<<<<<< HEAD

from urllib import request
from django.shortcuts import get_object_or_404, render ,redirect
from django.views import View
from .models import CartItem, Category, Product
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from decimal import Decimal
from django.conf import settings
from .forms import CustomUserCreationForm, CustomAuthenticationForm
import stripe
import requests

stripe.api_key = settings.STRIPE_SECRET_KEY

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            user.save()
            #login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login(request):
    error = None
    form = CustomAuthenticationForm()
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            captcha_token = request.POST.get('g-recaptcha-response')
            if verify_recaptcha(captcha_token):
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')  # Redirect to a success page.
                else:
                    error = "Invalid username or password."
            else:
                error = "Invalid CAPTCHA. Please try again."
        else:
            error = "Invalid form submission."
    return render(request, 'store/login.html', {'form': form, 'error': error})

def verify_recaptcha(token):
    secret_key =  '6LeaFBgqAAAAACcpJhAzZiYZ0_8AcbtgI2LhO3lO' # Replace with your actual secret key
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': secret_key,
        'response': token
    }
    response = requests.post(url, data=data)
    result = response.json()
    return result.get('success', False)

def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('home')
    
def profile(request):
    return render(request, 'store/profile.html', {'user': request.user})



def home(request): 
    products = Product.objects.all()  # Get all products
    foodie_category = Product.objects.filter(category=5)  
    context = {'products': products, 'foodie_products': foodie_category}
    return render(request, 'store/home.html', context)

def about_us(request):
    context = {}  # Create an empty context dictionary to pass data to the template (optional)
    return render(request, 'store/about_us.html', context)  

def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = request.session.get('cart', {})  # Fallback to session cart (optional)
    
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    total_price = sum(Decimal(item.product.price) * item.quantity for item in cart_items)
    tax = total_price * Decimal('0.10')
    total = total_price + tax
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'tax': tax,
        'total': total
    }

    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
  product = Product.objects.get(pk=product_id)

  if request.user.is_authenticated:
    # Get or create cart item for the user
    cart_item, created = CartItem.objects.get_or_create(
      user=request.user, product=product, defaults={'quantity': 1}
    )
    if not created:
      # Update quantity if the item already exists in the cart
      cart_item.quantity += 1
      cart_item.save()
  else:
    # Handle adding to session cart (optional)
    cart = request.session.get('cart', {})
    cart_item_id = str(product.id)  # Use a unique identifier for session cart items
    if cart_item_id in cart:
        cart[cart_item_id]['quantity'] += 1
    else:
        cart[cart_item_id] = {'product_id': product.id, 'quantity': 1}
        request.session['cart'] = cart
  return redirect('cart')

# Optional: view for removing items
def remove_from_cart(request, item_id):
  if request.user.is_authenticated:
    CartItem.objects.filter(user=request.user, id=item_id).delete()
  else:
    # Handle removing from session cart (optional)
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
      del cart[str(item_id)]
      request.session['cart'] = cart
  return redirect('cart')


def single_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)  # Retrieve product by ID
    except Product.DoesNotExist:
        # Handle case where product with the given ID doesn't exist (e.g., display 404)
        return render(request, '404.html')  # Replace with your error handling logic

    context = {'product': product} 
    return render(request, 'store/single_product.html', context) 


class PaymentView(View):
    def get(self, request):
        cart_items = request.session.get('cart_items', [])

        return render(request, 'store/payment.html', {
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            'cart_items': cart_items
        })

    def post(self, request):
        token = request.POST.get('stripeToken')
        amount = int(request.POST.get('amount'))  # Amount in cents

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='My E-commerce Payment'
            )
            return redirect('success')
        except stripe.error.StripeError:
            return redirect('failure')
        
def success_view(request):
    return render(request, 'store/success.html')

def failure_view(request):
    return render(request, 'store/failure.html')  

def pet(request):
    products = Product.objects.all()  # Get all products
    foodie_category = Product.objects.filter(category=5)  
    context = {'products': products, 'foodie_products': foodie_category}
    return render(request, 'store/pet.html',context) 

def shop(request):
    products=Product.objects.all()
    context = {'products': products}
    return render(request, 'store/shop.html', context)

    
=======

from django.shortcuts import get_object_or_404, render ,redirect
from .models import CartItem, Category, Product, wishlist
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            user.save()
            #login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                #login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def home(request):
    products = Product.objects.all()  # Get all products
    foodie_category = Product.objects.filter(category=5)  
    context = {'products': products, 'foodie_products': foodie_category}
    return render(request, 'store/home.html', context)
 
def insert(request):
    if request.method == "POST":
        # Assuming 'addwish' contains the product ID
        product_id = request.POST.get('addwish')
        if product_id:
            # Assuming you have a Product model with id field
            product = Product.objects.get(pk=product_id)
            # Create a new WishlistItem for the authenticated user
            wishlist.objects.create(user=request.user, product=product)
            return redirect("store:show")
    return redirect("store:home")

def show(request):
        items = wishlist.objects.all()
        return render(request, "store/show.html", {"items": items})

def delete(request, pk):
    item = get_object_or_404(wishlist, pk=pk)
    if request.method == "POST":
        # Delete the item if the request method is POST
        item.delete()
        messages.success(request, "Item successfully deleted.")
    else:
        messages.error(request, "Deletion can only be performed via POST request.")
    return redirect("store:show")

def updatePage(request, pk):
    update_data = wishlist.objects.get(pk=pk)
    return render(request, "store/update.html", {"updatedata": update_data})

def update(request, pk):
    update_data = wishlist.objects.get(pk=pk)
    update_data.wishlist = request.POST['updatewish']
    update_data.save()
    return redirect("store/show.html")

def checkb(request, pk):
    checkbox = wishlist.objects.get(pk=pk)
    checkbox.is_checked = request.POST.get('check') == "on"
    checkbox.save()
    return redirect('store/show.html')   

def about_us(request):
    context = {}  # Create an empty context dictionary to pass data to the template (optional)
    return render(request, 'store/about_us.html', context)  

def cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = request.session.get('cart', {})  # Fallback to session cart (optional)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
  product = Product.objects.get(pk=product_id)

  if request.user.is_authenticated:
    # Get or create cart item for the user
    cart_item, created = CartItem.objects.get_or_create(
      user=request.user, product=product, defaults={'quantity': 1}
    )
    if not created:
      # Update quantity if the item already exists in the cart
      cart_item.quantity += 1
      cart_item.save()
  else:
    # Handle adding to session cart (optional)
    cart = request.session.get('cart', {})
    cart_item_id = str(product.id)  # Use a unique identifier for session cart items
    cart[cart_item_id] = {'product_id': product.id, 'quantity': 1}
    request.session['cart'] = cart

  return redirect('store/cart')

# Optional: view for removing items
def remove_from_cart(request, item_id):
  if request.user.is_authenticated:
    CartItem.objects.filter(user=request.user, id=item_id).delete()
  else:
    # Handle removing from session cart (optional)
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
      del cart[str(item_id)]
      request.session['cart'] = cart
  return redirect('cart')


def single_product(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)  # Retrieve product by ID
    except Product.DoesNotExist:
        # Handle case where product with the given ID doesn't exist (e.g., display 404)
        return render(request, '404.html')  # Replace with your error handling logic

    context = {'product': product} 
    return render(request, 'store/single_product.html', context) 


def account(request):
    
    login(request)
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                #login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    logout(request)
    return render(request, 'store/account.html', {'form': form})
    
  


>>>>>>> 2ae262a36bac2affb99cf190835927092bd84717

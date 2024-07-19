
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

    

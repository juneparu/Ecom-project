
from django.shortcuts import get_object_or_404, render ,redirect
from .models import Product, wishlist
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
    products=Product.objects.all()
    return render(request, "store/home.html", {'products': products})

def insert(request):
    if request.method == "POST":
        wishlist = request.POST.get('addwish')
        new_data = wishlist.objects.create(wishlist=wishlist)
        return redirect("store/show.html")
    else:
        return redirect("store/home.html")

def show(request):
    if request.user.is_authenticated:
        items = wishlist.objects.all()
        return render(request, "store/show.html", {"items": items})
    else:
        return redirect('login')

def delete(request, pk):
    delete_data = get_object_or_404(wishlist, pk=pk)
    if request.method == "POST":
        delete_data.delete()
        messages.success(request,"Items succesfully deleted.")
        return redirect("store/show.html")
    else:
        messages.error(request, "Deletion can only be performed via POST request.")
        return redirect("store/show.html")
   
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
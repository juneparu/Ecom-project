from django.shortcuts import render ,redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm  

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Use your custom form
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the home page (or another view)
    else:
        form = UserCreationForm()  # Create an empty form

    context = {'form': form}
    return render(request, 'store/register.html', context)

def home(request):
    products=Product.objects.all()
    return render(request ,"store/index.html",{'products':products})


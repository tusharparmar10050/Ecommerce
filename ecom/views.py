from django.shortcuts import render,redirect
from .models import Category,Sub_Category,Product

from django.contrib.auth import authenticate,login
from ecom.models import UserCreateForm
# Create your views here.
def home(request):
    category = Category.objects.all()
    
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')
    else:
        product = Product.objects.filter()

    context = {
        'categorys' : category,
        'product' : product

    }

    return render(request,'index.html' , context)


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)


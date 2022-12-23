from django.shortcuts import render,redirect,HttpResponse
from .models import Category,Sub_Category,Product,Contact_us,Order

from django.contrib.auth import authenticate,login
from ecom.models import UserCreateForm

# for cart 
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

from django.contrib.auth.models import User

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


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def Contact_Us(request):
    if request.method== "POST":
        contact = Contact_us(
            name = request.POST.get("name"),
            email = request.POST.get("email"),
            subject = request.POST.get("subject"),
            message = request.POST.get("message"),
        )
        contact.save()
        
    return render(request, 'contact.html')


def CheckOut(request):
    if request.method== "POST":
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)        
        
        for i in cart:
            a = int(cart[i]['price'])
            b = cart[i]['quantity']
            total = a * b

            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total,
                )
            order.save()
        request.session['cart'] = {}
        return redirect('home')
    return HttpResponse("Chackout page is here")
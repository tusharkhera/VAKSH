from django import contrib
from django.shortcuts import redirect, render, HttpResponseRedirect, resolve_url
from .models import Customer, DailyAwareness, OrderPlaced, Product, Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views import View
from myapp.forms import ProfileForm, SignUpForm, LogInForm, MyPasswordChangeForm, CustomerProfileForm
from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.
def home(request):
    items = DailyAwareness.objects.all()
    return render(request, 'home.html', {'active':'color: #00aff0; background-color: white; border-radius: 2rem; padding: 1rem;', 'items':items})

def products(request):
    return render(request, 'products.html', {'active':'color: #00aff0; background-color: white; border-radius: 2rem; padding: 1rem;'})

def contact(request):
    return render(request, 'contact.html', {'active':'color: #00aff0; background-color: white; border-radius: 2rem; padding: 1rem;'})

def about(request):
    return render(request, 'about.html', {'active':'color: #00aff0; background-color: white; border-radius: 2rem; padding: 1rem;'})

def groceryProduct(request):
    items = Product.objects.filter(category = 'groceries')
    return render(request, 'categories/groceryProducts.html', {"items":items})

def milkProduct(request):
    items = Product.objects.filter(category = 'milk products')
    return render(request, 'categories/milkproducts.html', {"items":items})

def clayProduct(request):
    items = Product.objects.filter(category = 'clay vessels')
    return render(request, 'categories/clayProducts.html', {"items":items})

def ayurvedicProduct(request):
    items = Product.objects.filter(category = 'ayurvedic herbs and herbal juices')
    return render(request, 'categories/ayurvedic.html', {"items":items})

def glutenProduct(request):
    items = Product.objects.filter(category = 'gluten free products')
    return render(request, 'categories/glutten.html', {"items":items})

def readyProduct(request):
    items = Product.objects.filter(category = 'ready to eat')
    return render(request, 'categories/ready.html', {"items":items})

def beveragesProduct(request):
    items = Product.objects.filter(category = 'beverages')
    return render(request, 'categories/beverages.html', {"items":items})

def personalProduct(request):
    items = Product.objects.filter(category = 'personal care products')
    return render(request, 'categories/personal.html', {"items":items})

def organicProduct(request):
    items = Product.objects.filter(category = 'organic Teas')
    return render(request, 'categories/organic.html', {"items":items})

def miscellaneousProduct(request):
    items = Product.objects.filter(category = 'miscellaneous')
    return render(request, 'categories/miscellaneousProducts.html', {"items":items})

def naturalProduct(request):
    items = Product.objects.filter(category = 'natural air purifiers')
    return render(request, 'categories/natural.html', {"items":items})

def vegetableProduct(request):
    items = Product.objects.filter(category = 'vegetable and fruits')
    return render(request, 'categories/vegetable.html', {"items":items})

class ProductDetailView(View):
    def get(self,request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'productdetail.html', {'product':product})

class SignUpView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request, 'signUp.html', {'form':fm, 'active':'color: #00aff0; background-color: white; border-radius: 2rem; padding: 1rem;'})
    def post(self,request):
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created successfully !!')
            fm.save()    
        return render(request, 'signUp.html', {'form':fm, 'active':'color: #00aff0; background-color: white; border-radius: 2rem; padding: 1rem;'})
        

class MyLoginView(LoginView):
    template_name='login.html'
    authentication_form=LogInForm

class PasswordChange(PasswordChangeView):
    template_name = 'passwordChange.html'
    authentication_form = MyPasswordChangeForm      

class AddAddressView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = CustomerProfileForm()
            return render(request, 'addAddress.html', {'form':form})
        else:
            return HttpResponseRedirect('/login/')    
    def post(self,request):
        fm = CustomerProfileForm(request.POST)
        if fm.is_valid():
            usr = request.user
            name = fm.cleaned_data['name']
            contact = fm.cleaned_data['contact']
            locality = fm.cleaned_data['locality']
            city = fm.cleaned_data['city']
            zipcode = fm.cleaned_data['zipcode']
            state = fm.cleaned_data['state']
            reg = Customer(user=usr, name=name, contact=contact, locality=locality, city=city, zipcode=zipcode, state=state)
            reg.save()
            messages.success(request, 'Address Saved successfully !!')  
        return render(request, 'addAddress.html', {'form':fm})

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product_title = request.GET.get('prod_title')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product, title=product_title).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        if cart_product :
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            return render(request, 'cart.html', {'carts':cart, 'totalamount':amount + shipping_amount, 'amount':amount})
        else:
            return render(request, 'emptyCart.html')
    else:
        return HttpResponseRedirect('/login/')

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 50.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        data = {
            'amount' : amount,
            'totalamount' : amount + shipping_amount
        }
        return JsonResponse(data)

def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 50.0
    totalamount = 0.0
    # cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_items :
        for p in cart_items:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'checkout.html', {'add':add, 'totalamount':totalamount, 'amount':amount, 'items':cart_items})

def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    # p = Product.objects.filter(id=custid)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity, title=c.title, discounted=c.product.discounted, price=c.quantity*c.product.discounted_price).save()
        c.delete()
    return redirect('orders')

def orders(request):
    op = OrderPlaced.objects.filter(user = request.user)
    return render(request, 'orders.html', {'op':op})

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            fm = ProfileForm(instance=request.user)
            return render(request, 'pro.html', {'form':fm})
        else:
            fm = ProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile Updated successfully !!')  
            return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/login/')

def payment(request):
    return render(request, 'payment.html')
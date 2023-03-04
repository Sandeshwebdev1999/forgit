from django.shortcuts import render , HttpResponse , redirect

from app3.models import Category, Products, Contact, Order, Brand
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login

from app3.models import UserCreateForm

from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from django.contrib import messages




# Create your views here.

def index(request):

    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    products = Products.objects.all()
    categoryID = request.GET.get('category')

    if categoryID:

        products = Products.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        products = Products.objects.filter(brand=brandID).order_by('-id')

    else:

        products = Products.objects.all()



    context = {

        'category': category,

        'products': products,
        'brand' : brand,

    }


    return render(request,"index.html",context)


def master(request):


    return render(request,"master.html")



def signup(request):

    if request.method == 'POST':

        form = UserCreateForm(request.POST)

        if form.is_valid():

            new_user = form.save()

            new_user = authenticate(

                username = form.cleaned_data['username'],

                password = form.cleaned_data['password1'],
            )

            login(request, new_user)
            return redirect('app3')
            messages.success(request, "Sign-Up Successfull ! Please Log-in")

    else:

        form = UserCreateForm()


    context = {

        'form':form,

    }
       
    return render(request, "registration/signup.html", context)
   



#Add to cart


@login_required(login_url="/accounts/login/")

def cart_add(request, id):

    cart = Cart(request)

    product = Products.objects.get(id=id)
    cart.add(product=product)

    return redirect("app3")
    messages.success(request, "Sign-Up Successfull ! Please Log-in")



@login_required(login_url="/accounts/login/")

def item_clear(request, id):

    cart = Cart(request)

    product = Products.objects.get(id=id)

    cart.remove(product)

    return redirect("cart_detail")



@login_required(login_url="/accounts/login/")

def item_increment(request, id):

    cart = Cart(request)

    product = Products.objects.get(id=id)
    cart.add(product=product)

    return redirect("cart_detail")



@login_required(login_url="/accounts/login/")

def item_decrement(request, id):

    cart = Cart(request)

    product = Products.objects.get(id=id)
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



def contact(request):

    if request.method == 'POST':

        contact = Contact(

            name = request.POST.get('name'),

            email = request.POST.get('email'),

            subject = request.POST.get('subject'),

            message = request.POST.get('message'),

        )  

        contact.save()
        messages.success(request, 'Profile details updated.')


    return render(request,"contact.html")


def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        size =  request.POST.get('size')
        Full_Name = request.POST.get('Full_Name')
        City = request.POST.get('City')
        state = request.POST.get('state')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)


        print(address,phone,pincode,cart,user)
        for i in cart:
            a = int(cart[i]['price'])
            b = cart[i]['quantity']
            total = a * b
            order = Order(
                user = user,
                products =  cart[i]['name'],
                price = cart[i]['price'],
                Quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total,
                size = size,
                Full_Name = Full_Name,
                City = City,
                state = state,
 

                
            )
            order.save()
            request.session['cart'] = {}
        return redirect("app3")
    return HttpResponse("This is checkout")

def your_order(request): 
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk = uid)

    order = Order.objects.filter(user = user)
    context = {
        'order' : order,
    }

   
    # print(user)
    return render(request,"order.html",context)

def product(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        products = Products.objects.filter(brand=brandID).order_by('-id')
    else:
        products = Products.objects.all()


    context = {
        'category': category,
        'brand' : brand,
        'products' : products,
    }
    return render(request,"product.html",context)




def product_detail(request,id):
    products = Products.objects.filter(id = id).first()
    context = {
        'products' : products,
    }
    return render(request,"product_detail.html",context)


def search(request):
    query = request.GET['query']
    products = Products.objects.filter(name__icontains = query)
    context = {
        'products' : products
    }
    return render(request,"search.html",context)

def whishlist(request):
    return render(request,"wishlist.html")
from django.shortcuts import render, redirect
from .models import User, Admin
from django.contrib import messages
import bcrypt
from django.apps import apps

# Create your views here.
def index(request):
    return render(request, "index.html")

def marketplace(request):
    if 'user_id' in request.session:
        shop_items = apps.get_model('marketplace.Item').objects.all()
        if shop_items:
            user_items = apps.get_model('marketplace.User_Item_Count').objects.filter(user=User.objects.get(id=request.session['user_id']))
            if user_items:
                total_carbon_offset = 0
                for item in user_items:
                    total_carbon_offset += item.item.carbon_offset_in_trees * item.orders
                context = {
                    'items': reversed(shop_items),
                    'user': User.objects.get(id=request.session['user_id']),
                    'user_items': user_items,
                    'total_carbon_offset': total_carbon_offset
                }
                return render(request, 'marketplace.html', context)
            else:
                context = {
                    'items': reversed(shop_items),
                    'user': User.objects.get(id=request.session['user_id']),
                }
                return render(request, 'marketplace.html', context)
        else:
            context = {
                'user': User.objects.get(id=request.session['user_id'])
            }
            return render(request, 'marketplace.html', context)
    else:
        return redirect('index')

def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('index')
    else:
        User.objects.create(
            first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(
                request.POST["password"].encode(), bcrypt.gensalt()
            ).decode()
        )
        request.session['user_id'] = User.objects.last().id
        return redirect('marketplace')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('index')
    else:
        user = User.objects.filter(email=request.POST['email_login'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['pw_login'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('marketplace')
            else:
                messages.error(request, "Incorrect password.", extra_tags="login")
                return redirect('index')
        else:
            messages.error(request, "Incorrect email.", extra_tags="login")
            return redirect('index')

def logout(request):
    del request.session['user_id']
    return redirect('index')

def admin_index(request):
    return render(request, 'admin_index.html')

def admin_page(request):
    if 'admin_id' in request.session:
        shop_items = apps.get_model('marketplace.Item').objects.all()
        if shop_items:
            user_items = apps.get_model('marketplace.User_Item_Count').objects.all()
            if user_items:
                context = {
                    'admin': Admin.objects.get(id=request.session['admin_id']),
                    'items': reversed(shop_items),
                    'user_items': user_items,
                    'users': User.objects.all()
                }
                return render(request, 'admin_page.html', context)
            else:
                context = {
                    'admin': Admin.objects.get(id=request.session['admin_id']),
                    'items': reversed(shop_items)
                }
                return render(request, 'admin_page.html', context)
        else:
            context = {
                'admin': Admin.objects.get(id=request.session['admin_id'])
            }
            return render(request, 'admin_page.html', context)
    else:
        return redirect('admin_index')

def add_admin(request):
    errors = Admin.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='register')
        return redirect('admin_index')
    else:
        Admin.objects.create(
            first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(
                request.POST["password"].encode(), bcrypt.gensalt()
            ).decode()
        )
        request.session['admin_id'] = Admin.objects.last().id
        return redirect('admin_page')

def admin_login(request):
    errors = Admin.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="login")
        return redirect('admin_index')
    else:
        admin = Admin.objects.filter(email=request.POST['email_login'])
        if admin:
            logged_admin = admin[0]
            if bcrypt.checkpw(request.POST['pw_login'].encode(), logged_admin.password.encode()):
                request.session['admin_id'] = logged_admin.id
                return redirect('admin_page')
            else:
                messages.error(request, "Incorrect password.", extra_tags="login")
                return redirect('admin_index')
        else:
            messages.error(request, "Incorrect email.", extra_tags="login")
            return redirect('admin_index')

def admin_logout(request):
    del request.session['admin_id']
    return redirect('admin_index')
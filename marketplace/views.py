from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from django.apps import apps
from .models import Item, User_Item_Count, Cart, Cart_Item_Count

# Create your views here.
def add_item(request):
    errors = Item.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='item')
        return redirect('admin_page')
    else:
        Item.objects.create(
            name=request.POST['item_name'], description=request.POST['item_description'],
            carbon_offset_in_trees=request.POST['item_carbon_offset'], cost=request.POST['item_cost']
        )
        # Item.objects.last().categories.add(Category.objects.get(id=request.POST['item_category']))
        Item.objects.last().save()
        return redirect('admin_page')

def edit_item(request, item_id):
    # categories = Category.objects.all()
    # if categories:
    #     context = {
    #         'item': Item.objects.get(id=item_id),
    #         'categories': categories
    #     }
    #     return render(request, 'edit_item.html', context)
    # else:
        context = {
            'item': Item.objects.get(id=item_id)
        }
        return render(request, 'edit_item.html', context)

def update_item(request, item_id, same_item_id):
    errors = Item.objects.validate_edit(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('edit_item', item_id)
    else:
        item = Item.objects.get(id=same_item_id)
        item.name = request.POST['item_name']
        item.description = request.POST['item_description']
        item.carbon_offset_in_trees = request.POST['item_carbon_offset']
        item.cost = request.POST['item_cost']
        # item.categories.add(Category.objects.get(id=request.POST['item_category']))
        item.save()
        # category = Category.objects.get(id=request.POST['item_category'])
        # category.items.add(item)
        # category.save()
        return redirect('admin_page')

def delete_item(request, id):
    Item.objects.get(id=id).delete()
    return redirect('admin_page')

def buy_items(request, user_id):
    user = apps.get_model('login_app.User').objects.get(id=user_id)
    # user_item = User_Item_Count.objects.filter(user=apps.get_model('login_app.User').objects.get(id=user_id), item=Item.objects.get(id=item_id))
    # if not user_item:
    #     User_Item_Count.objects.create(
    #         user=apps.get_model('login_app.User').objects.get(id=user_id), item=Item.objects.get(id=item_id), orders=request.POST['purchase_quantity']
    #     )
    #     return redirect('marketplace')
    # else:
    #     user_item[0].orders += int(request.POST['purchase_quantity'])
    #     user_item[0].save()
    #     return redirect('marketplace')
    cart_items = Cart_Item_Count.objects.filter(cart=Cart.objects.get(user=user))
    if cart_items:
        for cart_item in cart_items:
            # for user_item in user_items:
            #     if cart_item.item.id == user_item.item.id:
            #         user_item.orders += int(request.POST['purchase_quantity'])
            #         user_item.save()
            #     else:
            #         User_Item_Count.objects.create(
            #             user=apps.get_model('login_app.User').objects.get(id=user_id), item=Item.objects.get(id=request.POST['item_id'],
            #             orders=request.POST['purchase_quantity'])
            #         )
            # if cart_item.item.purchases
            print(cart_item.item.purchases.all())
            # if user in cart_item.item.purchases.all():
                # User_Item_Count.objects.get(user=user, item=Item.objects.get(id=cart_item.item.id)).purchases += int(request.POST['purchase_quantity'])
                # User_Item_Count.objects.get(user=user, item=Item.objects.get(id=cart_item.item.id)).save()
                # return redirect('cart')
            # else:
                # User_Item_Count.objects.create(
                #         user=user, item=Item.objects.get(id=request.POST['item_id'],
                #         orders=request.POST['purchase_quantity'])
                #     )
                # return redirect('marketplace')
        return redirect('marketplace')
    else:
        return redirect('cart')

def add_to_cart(request, item_id, user_id):
    cart = Cart.objects.get(user=apps.get_model('login_app.User').objects.get(id=user_id))
    cart_item = Cart_Item_Count.objects.filter(cart=cart, item=Item.objects.get(id=item_id))
    if not cart_item:
        Cart_Item_Count.objects.create(
            cart=cart, item=Item.objects.get(id=item_id), quantity=request.POST['purchase_quantity']
        )
        return redirect('marketplace')
    else:
        cart_item[0].quantity += int(request.POST['purchase_quantity'])
        cart_item[0].save()
        return redirect('marketplace')

def view_cart(request, user_id):
    cart = Cart.objects.get(user=apps.get_model('login_app.User').objects.get(id=user_id))
    cart_items = Cart_Item_Count.objects.filter(cart=cart)
    if cart_items:
        total_cost = 0
        for item in cart_items:
            total_cost += item.item.cost * item.quantity
        context = {
            'user': apps.get_model('login_app.User').objects.get(id=user_id),
            'cart_items': cart_items,
            'total_cost': total_cost
        }
        return render(request, 'cart.html', context)
    else:
        context = {
            'user': apps.get_model('login_app.User').objects.get(id=user_id)
        }
        return render(request, 'cart.html', context)

# def add_category(request):
#     errors = Category.objects.validate(request.POST)
#     if len(errors) > 0:
#         for key, value in errors.items():
#             messages.error(request, value, extra_tags='category')
#         return redirect('admin_page')
#     else:
#         Category.objects.create(
#             name=request.POST['category_name'], description=request.POST['category_description']
#         )
#         return redirect('admin_page')

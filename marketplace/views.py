from django.contrib import messages
from django.shortcuts import render, redirect
from django.apps import apps
from .models import Item, User_Item_Count, Category

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
        Item.objects.last().categories.add(Category.objects.get(id=request.POST['item_category']))
        Item.objects.last().save()
        return redirect('admin_page')

def edit_item(request, item_id):
    categories = Category.objects.all()
    if categories:
        context = {
            'item': Item.objects.get(id=item_id),
            'categories': categories
        }
        return render(request, 'edit_item.html', context)
    else:
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
        category = Category.objects.get(id=request.POST['item_category'])
        category.items.add(item)
        category.save()
        return redirect('admin_page')

def delete_item(request, id):
    Item.objects.get(id=id).delete()
    return redirect('admin_page')

def buy_items(request, item_id, user_id):
    user_item = User_Item_Count.objects.filter(user=apps.get_model('login_app.User').objects.get(id=user_id), item=Item.objects.get(id=item_id))
    if not user_item:
        User_Item_Count.objects.create(
            user=apps.get_model('login_app.User').objects.get(id=user_id), item=Item.objects.get(id=item_id), orders=request.POST['purchase_quantity']
        )
        return redirect('marketplace')
    else:
        user_item[0].orders += int(request.POST['purchase_quantity'])
        user_item[0].save()
        return redirect('marketplace')

def add_category(request):
    errors = Category.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags='category')
        return redirect('admin_page')
    else:
        Category.objects.create(
            name=request.POST['category_name'], description=request.POST['category_description']
        )
        return redirect('admin_page')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from profiles.models import UserProfile, SavedItem
from django.contrib.auth.models import User

from django.db import IntegrityError, transaction

# Create your views here.

def view_bag(request):
    bag_items = []
    session_bag = request.session.get('bag', {})

    for item_id, quantity in session_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        bag_items.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity,
            'item_id': item_id,
        })

    saved_items = []
    if request.user.is_authenticated:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        print(f"UserProfile: {profile}, Created: {created}")  # Debugging output
        saved_items = SavedItem.objects.filter(profile=profile)
        print("Saved items in view_bag:", saved_items)  # Debugging output

    context = {
        'bag_items': bag_items,
        'saved_items': saved_items,
        'grand_total': sum(item['total'] for item in bag_items)
    }

    return render(request, 'bag/bag.html', context)



def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quanity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """ Remove a quantity of the specified product from the shopping bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        
        if item_id in bag:
            if bag[item_id] > 1:
                bag[item_id] -= 1
                messages.success(request, f'Decreased quantity of {product.name} in your bag.')
            else:
                del bag[item_id] 
                messages.success(request, f'Removed {product.name} from your bag.') 
                
            request.session['bag'] = bag
        
        return redirect('view_bag')
        
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

def move_to_bag(request, product_id):
    """
    Move an item from 'Save for Later' back to the shopping bag.
    """
    if request.user.is_authenticated:
        # Get the user's saved item and delete it from 'Save for Later'
        saved_item = get_object_or_404(SavedItem, product_id=product_id, profile__user=request.user)
        saved_item.delete()

        # Add the item back to the shopping bag session
        bag = request.session.get('bag', {})
        bag[product_id] = bag.get(product_id, 0) + 1  # Increment quantity by 1, or add item if not present
        request.session['bag'] = bag

    return redirect('view_bag')


def remove_saved_item(request, item_id):
    """
    Remove an item from the 'Saved for Later' list.
    """
    if request.user.is_authenticated:
        # Get the saved item for the user and delete it
        saved_item = get_object_or_404(SavedItem, id=item_id, profile__user=request.user)
        saved_item.delete()
    return redirect('view_bag')  # Redirect back to the shopping bag page


@login_required
def save_for_later(request, product_id):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    saved_item, created_saved_item = SavedItem.objects.get_or_create(profile=profile, product=product)

    saved_item.save()
    
    if created_saved_item:
       bag = request.session.get('bag', {})
       if str(product_id) in bag:
          del bag[str(product_id)]
          request.session['bag'] = bag

    return redirect('view_bag')


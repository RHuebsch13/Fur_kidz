from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

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

    
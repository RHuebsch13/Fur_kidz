from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product  # Change the import to the correct app

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0

    # Retrieve the bag from the session
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, id=item_id)
        item_total = product.price * quantity  # Calculate total for the current item

        # Append item details to bag_items list
        bag_items.append({
            'id': product.id,
            'name': product.name,  # Adjust this based on your product model
            'quantity': quantity,
            'price': product.price,
            'total': item_total,
        })

        total += item_total  # Update total price
        product_count += quantity  # Update product count

    # Prepare context to return
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': total,  # Since delivery is removed, grand total is just total
    }

    return context



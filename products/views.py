from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm
from .forms import ReviewForm


# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = Category.objects.all()  # Fetch all categories
    sort = None
    direction = None
    selected_category = None  # Initialize selected_category

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            category_id = request.GET['category']
            selected_category = get_object_or_404(Category, id=category_id)  # Fetch the selected category
            products = products.filter(category=selected_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'selected_category': selected_category,  # Pass the selected category to the template
    }

    return render(request, 'products/products.html', context)


@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        # Check if a delete request has been made
        if 'delete_review_id' in request.POST:
            review_id = request.POST.get('delete_review_id')
            review = get_object_or_404(Review, id=review_id, user=request.user)
            review.delete()
            messages.success(request, 'Review deleted successfully!')
            return redirect('product_detail', product_id=product_id)

        # Check if an edit request has been made
        elif 'edit_review_id' in request.POST:
            review_id = request.POST.get('edit_review_id')
            review = get_object_or_404(Review, id=review_id, user=request.user)
            edit_form = ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, 'Review updated successfully!')
                return redirect('product_detail', product_id=product_id)
            else:
                messages.error(request, 'Failed to update review. Please ensure the form is valid.')
        else:
            # Handle new review submission
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, 'Review submitted successfully!')
                return redirect('product_detail', product_id=product_id)
            else:
                messages.error(request, 'Failed to submit review. Please ensure the form is valid.')

    else:
        form = ReviewForm()  # For new review
        edit_form = None  # Initialize edit_form as None for GET requests

    # For GET requests, fetch reviews and prepare edit forms
    reviews = product.reviews.all()
    
    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
        'edit_form': edit_form,
    }
    return render(request, 'products/product_detail.html', context)





@login_required 
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))




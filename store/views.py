from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import Product, Collection, ContactMessage, Order, ProductRating, Newsletter

def home(request):
    collection_id = request.GET.get('collection')
    if collection_id:
        products = Product.objects.filter(collection_id=collection_id)
    else:
        products = Product.objects.all()
    collections = Collection.objects.all()
    return render(request, 'store/home.html', {'products': products, 'collections': collections, 'page': 'home'})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    collections = Collection.objects.all()
    related_products = Product.objects.filter(collection=product.collection).exclude(id=product.id)[:4]
    likes = ProductRating.objects.filter(product=product, is_like=True).count()
    dislikes = ProductRating.objects.filter(product=product, is_like=False).count()
    return render(request, 'store/product_detail.html', {
        'product': product,
        'collections': collections,
        'related_products': related_products,
        'likes': likes,
        'dislikes': dislikes
    })

def rate_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        is_like = request.POST.get('is_like') == 'true'
        ProductRating.objects.create(product=product, is_like=is_like)
        likes = ProductRating.objects.filter(product=product, is_like=True).count()
        dislikes = ProductRating.objects.filter(product=product, is_like=False).count()
        return JsonResponse({'likes': likes, 'dislikes': dislikes})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    collections = Collection.objects.all()
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        notes = request.POST.get('notes', '')
        
        if customer_name and phone and location:
            Order.objects.create(
                product=product,
                customer_name=customer_name,
                phone=phone,
                location=location,
                notes=notes
            )
            return render(request, 'store/order_success.html', {'product': product, 'collections': collections})
    
    return render(request, 'store/order.html', {'product': product, 'collections': collections})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                Newsletter.objects.create(email=email)
                return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
            except:
                return JsonResponse({'success': False, 'message': 'Email already subscribed'})
        return JsonResponse({'success': False, 'message': 'Please enter a valid email'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def contact(request):
    collections = Collection.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return render(request, 'store/contact.html', {'collections': collections, 'page': 'contact', 'success': True})
    return render(request, 'store/contact.html', {'collections': collections, 'page': 'contact'})

def about(request):
    collections = Collection.objects.all()
    return render(request, 'store/about.html', {'collections': collections, 'page': 'about'})
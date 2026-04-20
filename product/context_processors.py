from .models import Category
from home.models import Contact
from accounts.cart_wishlist import get_cart_products, get_wishlist_products


def company(request):
    return {
        "company_logo": "/static/assets/images/logo/logo.webp",
        "company_name": "Printora 3D",
        "company_desc": """India's trusted store 3D printers.
        Expert guidance, fast delivery, and warranty-backed machines—so you can print with confidence.""",
        "address": "Patna",
        "mobile": "9661054866",
        "email": "printoracontact@gmail.com",
    }


def categories_context(request):
    categories = Category.objects.filter(is_publish=True)
    return {'categories': categories}


def contact_context(request):
    contact_message = Contact.objects.all()
    return {'contact_message': contact_message}


def product_in_cart(request):
    product = get_cart_products(request)
    totalamount = 0
    for queryset in product:
        if queryset.quantity:
            totalamount = totalamount + (queryset.dis_price * int(queryset.quantity))
    return {'product_in_cart': product, 'totalamount': totalamount, 'cart_count': len(product)}


def product_in_wishlist(request):
    product = get_wishlist_products(request)
    return {'product_in_wishlist': product, 'wishlist_count': len(product)}

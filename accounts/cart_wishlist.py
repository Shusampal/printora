from accounts.models import CartItem, WishlistItem
from product.models import Product


def _normalize_quantity(quantity):
    try:
        quantity = int(quantity)
    except (TypeError, ValueError):
        quantity = 1
    return max(quantity, 1)


def get_cart_products(request):
    products = []
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user).select_related("product")
        for item in cart_items:
            product = item.product
            product.quantity = item.quantity
            products.append(product)
        return products

    cart = request.session.get("cart", {})
    for uid, quantity in cart.items():
        try:
            product = Product.objects.get(uid=uid)
        except Product.DoesNotExist:
            continue
        product.quantity = _normalize_quantity(quantity)
        products.append(product)
    return products


def get_wishlist_products(request):
    products = []
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user).select_related("product")
        for item in wishlist_items:
            products.append(item.product)
        return products

    wishlist = request.session.get("wishlist", {})
    for uid in wishlist.keys():
        try:
            products.append(Product.objects.get(uid=uid))
        except Product.DoesNotExist:
            continue
    return products


def get_cart_total(request):
    totalamount = 0
    for product in get_cart_products(request):
        totalamount += product.dis_price * int(product.quantity)
    return totalamount


def add_cart_product(request, product, quantity):
    quantity = _normalize_quantity(quantity)
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={"quantity": quantity},
        )
        if not created:
            cart_item.quantity = quantity
            cart_item.save()
        return

    cart = request.session.get("cart", {})
    cart[str(product.uid)] = quantity
    request.session["cart"] = cart
    request.session.modified = True


def add_wishlist_product(request, product):
    if request.user.is_authenticated:
        WishlistItem.objects.get_or_create(user=request.user, product=product)
        return

    wishlist = request.session.get("wishlist", {})
    wishlist[str(product.uid)] = ""
    request.session["wishlist"] = wishlist
    request.session.modified = True


def remove_cart_product(request, product_uid):
    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user, product_id=product_uid).delete()
        return

    cart = request.session.get("cart", {})
    cart.pop(str(product_uid), None)
    request.session["cart"] = cart
    request.session.modified = True


def remove_wishlist_product(request, product_uid):
    if request.user.is_authenticated:
        WishlistItem.objects.filter(user=request.user, product_id=product_uid).delete()
        return

    wishlist = request.session.get("wishlist", {})
    wishlist.pop(str(product_uid), None)
    request.session["wishlist"] = wishlist
    request.session.modified = True


def clear_cart(request):
    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user).delete()
        return

    request.session["cart"] = {}
    request.session.modified = True


def merge_session_data_for_user(request, user):
    cart = request.session.get("cart", {})
    wishlist = request.session.get("wishlist", {})

    for uid, quantity in cart.items():
        try:
            product = Product.objects.get(uid=uid)
        except Product.DoesNotExist:
            continue
        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product=product,
            defaults={"quantity": _normalize_quantity(quantity)},
        )
        if not created:
            cart_item.quantity = _normalize_quantity(quantity)
            cart_item.save()

    for uid in wishlist.keys():
        try:
            product = Product.objects.get(uid=uid)
        except Product.DoesNotExist:
            continue
        WishlistItem.objects.get_or_create(user=user, product=product)

    request.session["cart"] = {}
    request.session["wishlist"] = {}
    request.session.modified = True

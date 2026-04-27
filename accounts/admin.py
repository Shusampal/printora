from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'full_name',
                    'is_active', 'is_phone_verified')
    list_filter = ('is_active', 'is_phone_verified')
    search_fields = ('phone_number', 'email', 'full_name')
    fieldsets = (
        ('Personal Information', {
         'fields': ('full_name', 'phone_number', 'email')}),
        ('Verification', {'fields': ('is_phone_verified', 'otp')}),
        ('Status', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state', 'phone')
    list_filter = ('state', 'city')
    search_fields = ('user__phone_number', 'city', 'phone')
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Address Details', {
         'fields': ('name', 'addressline', 'locality', 'city', 'state', 'zipcode')}),
        ('Contact', {'fields': ('phone', 'email')}),
    )


@admin.register(BillAddress)
class BillAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'state', 'phone')
    list_filter = ('state', 'city')
    search_fields = ('user__phone_number', 'city', 'phone')
    fieldsets = (
        ('User', {'fields': ('user',)}),
        ('Address Details', {
         'fields': ('name', 'addressline', 'locality', 'city', 'state', 'zipcode')}),
        ('Contact', {'fields': ('phone', 'email')}),
    )


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('invoice_no', 'user', 'ordered_date',
                    'status', 'paid_amount')
    list_filter = ('status',)
    search_fields = ('invoice_no', 'user__phone_number', 'user__email')
    readonly_fields = ('ordered_date', 'invoice_no')
    fieldsets = (
        ('Order Information', {
         'fields': ('invoice_no', 'user', 'ordered_date')}),
        ('Status & Amount', {'fields': ('status', 'paid_amount', 'is_paid')}),
        ('Addresses', {'fields': ('address', 'bill_address')}),
        ('Transaction', {
         'fields': ('merchantTransactionId', 'transactionId')}),
    )


@admin.register(PursedProduct)
class PursedProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'paid_amount')
    list_filter = ('ordered_date',)
    search_fields = ('order__invoice_no', 'product__product_name')
    readonly_fields = ('ordered_date',)
    fieldsets = (
        ('Product Purchase', {
         'fields': ('order', 'product', 'color_varient', 'quantity', 'paid_amount')}),
        ('Metadata', {'fields': ('ordered_date',), 'classes': ('collapse',)}),
    )


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('product__product_name', 'user__phone_number', 'comment')
    readonly_fields = ('created_at', 'user')
    fieldsets = (
        ('Review Details', {
         'fields': ('product', 'user', 'comment', 'rating')}),
        ('Metadata', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )


@admin.register(ShipToken)
class ShipTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'date')
    list_filter = ('date',)
    search_fields = ('token',)
    readonly_fields = ('date',)
    fieldsets = (
        ('Shipping Token', {'fields': ('token', 'date')}),
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__phone_number', 'product__product_name')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Cart Details', {'fields': ('user', 'product', 'quantity')}),
        ('Metadata', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__phone_number', 'product__product_name')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Wishlist Details', {'fields': ('user', 'product')}),
        ('Metadata', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )


admin.site.register(Subscribe)

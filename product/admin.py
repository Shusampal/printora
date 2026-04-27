from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'is_publish', 'created_at')
    list_filter = ('is_publish',)
    search_fields = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    fieldsets = (
        ('Category Information', {
         'fields': ('category_name', 'slug', 'is_publish')}),
        ('Media', {'fields': ('category_image',)}),
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category', 'is_publish', 'created_at')
    list_filter = ('category', 'is_publish')
    search_fields = ('category_name', 'category__category_name')
    prepopulated_fields = {'slug': ('category_name',)}
    fieldsets = (
        ('SubCategory Information', {
         'fields': ('category_name', 'slug', 'category', 'is_publish')}),
        ('Media', {'fields': ('category_image',)}),
    )


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('brands_name', 'is_publish', 'slug', 'created_at')
    list_filter = ('is_publish',)
    search_fields = ('brands_name', 'slug')
    prepopulated_fields = {'slug': ('brands_name',)}
    fieldsets = (
        ('Brand Information', {
         'fields': ('brands_name', 'slug', 'is_publish')}),
        ('Media', {'fields': ('brands_image',)}),
    )


@admin.register(ColorVarient)
class ColorVarientAdmin(admin.ModelAdmin):
    list_display = ['color_name', 'price', 'created_at']
    list_filter = ['price']
    search_fields = ['color_name']
    fieldsets = (
        ('Color Details', {'fields': ('color_name', 'price')}),
    )


@admin.register(SizeVarient)
class SizeVarientAdmin(admin.ModelAdmin):
    list_display = ['size_name', 'price', 'created_at']
    list_filter = ['price']
    search_fields = ['size_name']
    fieldsets = (
        ('Size Details', {'fields': ('size_name', 'price')}),
    )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'sub_category',
                    'dis_price', 'mrp_price', 'is_publish', 'created_at']
    list_filter = ['is_publish', 'sub_category', 'created_at']
    search_fields = ['product_name', 'product_description']
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('product_name',)}
    fieldsets = (
        ('Product Information', {
         'fields': ('product_name', 'slug', 'sub_category', 'brands')}),
        ('Pricing', {'fields': ('mrp_price', 'dis_price')}),
        ('Details', {'fields': ('product_description',)}),
        ('Variants', {'fields': ('color_varient', 'size_varient')}),
        ('Dimensions & Weight', {
         'fields': ('length', 'breadth', 'height', 'weight')}),
        ('Publishing', {'fields': ('is_publish',)}),
        ('Metadata', {'fields': ('created_at',
         'updated_at'), 'classes': ('collapse',)}),
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('product__product_name',)
    fieldsets = (
        ('Product', {'fields': ('product',)}),
        ('Image', {'fields': ('image',)}),
    )


@admin.register(Onsale)
class OnsaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'sale_discount_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__product_name',)
    fieldsets = (
        ('Product & Discount', {'fields': ('product', 'sale_discount_price')}),
    )


@admin.register(DealOfTheDay)
class DealOfTheDayAdmin(admin.ModelAdmin):
    list_display = ('product', 'sale_discount_price',
                    'offer_date', 'created_at')
    list_filter = ('offer_date',)
    search_fields = ('product__product_name',)
    fieldsets = (
        ('Product & Deal', {'fields': ('product',
         'sale_discount_price', 'offer_date')}),
    )


@admin.register(BestSaler)
class BestSalerAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__product_name',)
    fieldsets = (
        ('Best Seller', {'fields': ('product',)}),
    )


@admin.register(HotSaler)
class HotSalerAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('product__product_name',)
    fieldsets = (
        ('Hot Seller', {'fields': ('product',)}),
    )


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('coupon_code', 'is_expired',
                    'discount_price', 'minimun_amount', 'created_at')
    list_filter = ('is_expired', 'created_at')
    search_fields = ('coupon_code',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Coupon Details', {'fields': ('coupon_code',)}),
        ('Discount', {'fields': ('discount_price', 'minimun_amount')}),
        ('Status', {'fields': ('is_expired',)}),
        ('Metadata', {'fields': ('created_at',
         'updated_at'), 'classes': ('collapse',)}),
    )

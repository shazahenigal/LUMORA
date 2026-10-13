from django.contrib import admin
from .models import Product, ProductImage, ProductVariant, PromoCode, GovernorateShipping, SiteContent, Banner, CategoryCover

# لربط الصور المتعددة والأحجام بصفحة المنتج في الـ Admin
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # يتيح لكِ إضافة 3 صور إضافية مباشرة مع المنتج

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 2  # يتيح لكِ إضافة درجات الألوان أو الأحجام مباشرة

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'sub_category', 'price', 'sale_price', 'is_best_seller', 'is_hot_sale')
    list_filter = ('category', 'sub_category', 'is_best_seller', 'is_hot_sale')
    search_fields = ('name', 'brand')
    inlines = [ProductImageInline, ProductVariantInline]  # هنا السحر! ربط الصور والـ Variants بصفحة المنتج

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'expiration_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('code',)

@admin.register(GovernorateShipping)
class GovernorateShippingAdmin(admin.ModelAdmin):
    list_display = ('governorate_name', 'shipping_cost')
    search_fields = ('governorate_name',)

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')

@admin.register(CategoryCover)
class CategoryCoverAdmin(admin.ModelAdmin):
    list_display = ('category_name',) 

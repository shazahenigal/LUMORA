from django.shortcuts import render
from .models import Product, Banner, SiteContent

def home(request):
    # 1. كل المنتجات
    all_products = Product.objects.all().order_by('-created_at')
    
    # 2. المنتجات مقسمة حسب الفئات (Category)
    makeup_products = Product.objects.filter(category='MAKEUP')
    skincare_products = Product.objects.filter(category='SKINCARE')
    haircare_products = Product.objects.filter(category='HAIRCARE')
    fragrance_products = Product.objects.filter(category='FRAGRANCE')
    
    # 3. العروض والأكثر مبيعاً
    hot_sales = Product.objects.filter(is_hot_sale=True)
    best_sellers = Product.objects.filter(is_best_seller=True)
    
    banners = Banner.objects.filter(is_active=True)
    site_content = SiteContent.objects.first()

    context = {
        'products': all_products,
        'makeup_products': makeup_products,
        'skincare_products': skincare_products,
        'haircare_products': haircare_products,
        'fragrance_products': fragrance_products,
        'hot_sales': hot_sales,
        'best_sellers': best_sellers,
        'banners': banners,
        'site_content': site_content,
    }
    return render(request, 'store/index.html', context) 
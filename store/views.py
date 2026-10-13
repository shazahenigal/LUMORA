from django.shortcuts import render
from .models import Product, Banner, CategoryCover, SiteContent

def home(request):
    # جلب البيانات من قاعدة البيانات
    banners = Banner.objects.filter(is_active=True)
    hot_sales = Product.objects.filter(is_hot_sale=True)
    best_sellers = Product.objects.filter(is_best_seller=True)
    all_products = Product.objects.all()
    site_content = SiteContent.objects.first()

    context = {
        'banners': banners,
        'hot_sales': hot_sales,
        'best_sellers': best_sellers,
        'all_products': all_products,
        'site_content': site_content,
    }
    return render(request, 'store/index.html', context) 
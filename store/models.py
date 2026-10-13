from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('MAKEUP', 'MAKEUP'),
        ('SKINCARE', 'SKINCARE'),
        ('HAIRCARE', 'HAIRCARE'),
        ('FRAGRANCE', 'FRAGRANCE'),
    ]

    SUB_CATEGORY_CHOICES = [
        ('Eye', 'Eye'),
        ('Lips', 'Lips'),
        ('Face', 'Face'),
        ('Makeup Sets', 'Makeup Sets'),
        ('Korean', 'Korean'),
        ('Cleanser', 'Cleanser'),
        ('Toner', 'Toner'),
        ('Face Mask', 'Face Mask'),
        ('Serum', 'Serum'),
        ('Cleansing Balm', 'Cleansing Balm'),
        ('Scrubs & Exfoliating', 'Scrubs & Exfoliating'),
        ('Japanese Products', 'Japanese Products'),
        ('Hair Mask', 'Hair Mask'),
        ('Shampoo', 'Shampoo'),
        ('Conditioner', 'Conditioner'),
        ('Oil', 'Oil'),
        ('For Her', 'For Her'),
        ('For Him', 'For Him'),
        ('Unisex', 'Unisex'),
        ('All', 'All'),
    ]

    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    sub_category = models.CharField(max_length=50, choices=SUB_CATEGORY_CHOICES, default='All')
    
    # السعر الأساسي أو نطاق الأسعار
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    image_url = models.URLField(max_length=500, help_text="الصورة الرئيسية للمنتج")
    is_best_seller = models.BooleanField(default=False)
    is_hot_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} - {self.name}"


# 1. جدول معرض الصور المتعددة لكل منتج (Product Images Gallery)
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500, help_text="رابط صورة إضافية للمنتج")

    def __str__(self):
        return f"Image for {self.product.name}"


# 2. جدول الأحجام والدرجات (Variants)
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100, help_text="اسم الدرجة أو الحجم (مثل: Travel Size, 50ml)")
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, help_text="فرق السعر إن وجد")
    
    def __str__(self):
        return f"{self.product.name} ({self.variant_name})"


class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.PositiveIntegerField()
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.code} ({self.discount_percentage}%)"


class GovernorateShipping(models.Model):
    governorate_name = models.CharField(max_length=100, unique=True)
    shipping_cost = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.governorate_name}: {self.shipping_cost} EGP"


class SiteContent(models.Model):
    about_us = models.TextField(default="Welcome to LUMORA Beauty Store...")
    contact_us = models.TextField(default="Support email: support@lumora.com")
    refund_exchange_policy = models.TextField(default="14-day exchange policy...")

    class Meta:
        verbose_name_plural = "Site Content"

    def __str__(self):
        return "LUMORA Site Content Management"


class Banner(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField(max_length=500, help_text="رابط صورة البانر الرئيسية")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CategoryCover(models.Model):
    CATEGORY_CHOICES = [
        ('MAKEUP', 'MAKEUP'),
        ('SKINCARE', 'SKINCARE'),
        ('HAIRCARE', 'HAIRCARE'),
        ('FRAGRANCE', 'FRAGRANCE'),
    ]
    category_name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    cover_image_url = models.URLField(max_length=500, help_text="رابط صورة الغلاف لهذا القسم")

    def __str__(self):
        return f"Cover for {self.category_name}" 

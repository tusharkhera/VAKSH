
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('organic groceries', 'organic groceries'),
    ('dairy products', 'dairy products'),
    ('cooking vessels', 'cooking vessels'),
    ('ayurvedic herbs and herbal juices', 'ayurvedic herbs and herbal juices'),
    ('poojan samagri', 'poojan samagri'),
    ('ready to eat', 'ready to eat'),
    ('beverages', 'beverages'),
    ('personal care products', 'personal care products'),
    ('sweets and snacks', 'sweets and snacks'),
    ('miscellaneous', 'miscellaneous'),
    ('natural air purifiers', 'natural air purifiers'),
    ('vegetable and fruits', 'vegetable and fruits'),
    ('Breakfast Cereals', 'Breakfast Cereals'),
    ('Oils & Ghee', 'Oils & Ghee'),
    ('Dry Fruits', 'Dry Fruits'),
    ('flour', 'flour'),
    ('rice', 'rice'),
    ('pulses', 'pulses'),
    ('millets', 'millets'),
    ('spices', 'spices'),
    ('honey/sugar/sweetner', 'honey/sugar/sweetner'),
    ('tea', 'tea'),
    ('baskets', 'baskets')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    discounted = models.CharField(blank=True, max_length=20)
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    product_image = models.ImageField(upload_to='productimg')
    prod_video = models.CharField(max_length=10000, blank=True)
    is_inStock = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.id)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='productimg')

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default="null")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=250, null=True)
    discounted = models.CharField(max_length=20, blank=True, null=True)
    price = models.FloatField(null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='Pending', max_length=50)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class DailyAwareness(models.Model):
    text = models.CharField(max_length=100000)
    image = models.ImageField(upload_to='awarenessImage')
    video = models.CharField(max_length=10000)
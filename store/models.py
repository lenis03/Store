from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categorise'


class Discount(models.Model):
    discount = models.FloatField()
    description = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    discount = models.ManyToManyField(Discount, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField(null=True, blank=True)


class Adress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address_detail = models.CharField(max_length=500)


class Order(models.Model):
    ORDER_STATUS_PAID = 'p'
    ORDER_STATUS_UNPAID = 'u'
    ORDER_STATUS_CANCELED = 'c'

    ORDER_STATUS = [
        (ORDER_STATUS_PAID, 'Paid'),
        (ORDER_STATUS_UNPAID, 'Unpaid'),
        (ORDER_STATUS_CANCELED, 'Canceled'),

    ]

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDER_STATUS_UNPAID)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    datetime_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['order', 'product']]


class Comment(models.Model):
    COMMENT_STATUS_WAITING = 'w'
    COMMENT_STATUS_APPROVED = 'a'
    COMMENT_STATUS_NOT_APPROVED = 'na'
    COMMENT_STATUS = [
        (COMMENT_STATUS_WAITING, 'Waiting'),
        (COMMENT_STATUS_APPROVED, 'Approved'),
        (COMMENT_STATUS_NOT_APPROVED, 'NotApproved'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField(max_length=500)
    datetime_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=COMMENT_STATUS, default=COMMENT_STATUS_WAITING)

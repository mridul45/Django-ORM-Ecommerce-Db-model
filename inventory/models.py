from django.db import models
from django.contrib.auth.admin import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# class PersonManagerInactive(models.Manager):
#     def get_queryset(self):
#         return super(PersonManagerInactive,self).get_queryset.filter(is_active=False)

# class PersonManagerActive(models.Manager):
#     def get_queryset(self):
#         return super(PersonManagerActive,self).get_queryset.filter(is_active=True)

# class Person(User):
#     inactive = PersonManagerInactive()
#     class Meta:
#         proxy = True
#         ordering = ("first_name",)

#     @classmethod
#     def count_all(cls,):
#         return cls.object.filter(is_active=True).count()

#     def check_active(self):
#         if self.is_active == True:
#             return "You are active"

#         else:
#             return "You are not Active"

#     def __str__(self):
#         return self.first_name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField()
    is_active = models.BooleanField()

    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    value = models.CharField(max_length=50)

    attribute = models.ForeignKey(
        Attribute, related_name="attribute", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.value
        # return f"{self.attribute.name}:{self.value}"


class Inventory(models.Model):
    is_active = models.BooleanField()
    is_default = models.BooleanField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    sku = models.CharField(
        max_length=20,
        unique=True,
    )
    # sku = models.UUIDField(default=uuid.uuid4, editable=False)

    product = models.ForeignKey(
        Product, related_name="product", on_delete=models.CASCADE
    )
    attribute_values = models.ManyToManyField(AttributeValue)

    class Meta:
        verbose_name_plural = "Inventory"

    def __str__(self):
        return self.product.name


class StockControl(models.Model):
    last_checked = models.DateTimeField(auto_now_add=False, editable=False)
    units = models.IntegerField(default=0)

    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Stock Control"


class Image(models.Model):
    url = models.ImageField(upload_to=None)
    alternative_text = models.CharField(max_length=50)
    is_feature = models.BooleanField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
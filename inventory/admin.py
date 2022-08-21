from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(Image)
admin.site.register(Inventory)
admin.site.register(Product)
admin.site.register(StockControl)